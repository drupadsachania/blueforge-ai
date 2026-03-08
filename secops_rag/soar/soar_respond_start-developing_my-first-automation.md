# Create your first playbook

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-automation/  
**Scraped:** 2026-03-05T10:07:59.706871Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create your first playbook
Supported in:
Google secops
SOAR
This document explains how to create your first playbook using the
  actions you created in
Create custom actions
.
The playbook you'll build is for a basic phishing use case and automates the following steps:
Extract domain details
: The playbook extracts the domain from a URL found in an alert.
Enrich the domain
: It then enriches the entity with additional information.
Add an insight
: The playbook adds an insight containing the domain's country.
Check a custom list
: It checks if the country is on a custom list.
Use an
IF
condition
: An
IF
condition is used to determine if the case requires further investigation based on whether the country is on the custom list.
Enable actions in the playbook designer
To make sure that the custom actions you created are enabled in the Integrated Developer Environment (IDE), click the
Enable
toggle to the on position. Once enabled, these actions are available in the playbook designer.
Create a custom list of OECD countries
To determine if a domain's country requires further investigation, you need to create a custom list of Organisation for Economic Co-operation and Development (OECD) countries. You can then use this list in your playbook to check against the domain's country.
To create a custom list of OECD countries, follow these steps:
Go to
Settings
>
Environments
.
Click
Custom lists
.
In the
Custom lists
section, click
add
Add
.
In the
Add Custom List
dialog, enter and
Entity Identifier
,
Category
, and
Environment
.
Click
Add
.
Create an automation playbook
To create an automation playbook, follow these steps:
Go to
Playbook Designer
and
    click
add
Add
.
In the
Create New
dialog, select the
Playbook
radio button.
Choose a folder and an environment for the playbook.
Enter a name for the playbook (next to the playbook toggle) to start 
    customizing your playbook.
Import a premade playbook
To import a premade playbook, follow these steps:
In the
Playbook Designer
, click
format_list_bulleted
List
>
login
Import
.
Create my first automation playbook
Every playbook starts with a trigger. To set this playbook's trigger, drag the
All
trigger from the
Triggers
menu to the first step of the playbook. This causes the playbook to activate on every alert ingested into Google Security Operations.
Create a playbook
To create a playbook using the actions from your "WHOIS XML API" integration, follow these steps:
In the
Actions
tab, click the
WHOIS XML API
list. Your custom actions will appear under the integration name. If they're not visible, confirm that they're enabled and saved in the IDE module.
Drag the
Get Domain Details
action into the playbook, placing it right after the trigger.
Customize the action
You can customize the action to run on a specific scope. In this example, run the action on all entities that are URLs. For the domain name field, use the
Entity.Identifier
placeholder.
To make these customizations, do the following:
Insert the placeholder: click
data_array
Placeholder
and search for
Entity.Identifier
in the search bar. This action connects to
    the "WHOIS" site, extracts the details of the Domain, and presents them in
    JSON format.
Define the scope. The action connects to the "WHOIS" site, extracts domain details, and presents them in JSON format.
Check availability. The
Check Availability
parameter you defined for the action checks if the domain is available or not.
After adding the
Get Domain Details
action, drag the
Enrich Entities
action into your playbook. Customize it to run on All URLs. Because you designed this action to operate on a specific entity scope, you don't need to define the
Domain name
field, as you did with the previous action.
Add the Entity Insight action
Add the
Add Entity Insight
action which is part
    of the Google SecOps Integration:
Define the scope. For the
Entity
scope, select
All URLs
, as you did for the previous actions in the playbook.
Extract the JSON field. In the
Insight
field, open the
Google SecOps Expression builder
to extract the country field from the JSON result.
Open the expression builder for the JSON output: Click the placeholder icon (
data_array
), choose the playbook list, and select
WHOIS XML API_Get Domain Details_1.JsonResult
. This opens the expression builder for the JSON output.
Extract the country field from the JSON
The JSON sample in the expression builder is the same one you inserted in the IDE for
Create your custom action
. To extract the `Country` field, follow these steps:
Click
Country
in the JSON.
Click
arrow_right
Run
to test the placeholder, and view the result under the
Results
field.
Create an entity
To run the
Is in custom list
action, you need to create a new entity from the country related to the domain. To do this, follow these steps:
From
Google SecOps Integration
, drag the
Create Entity
action
    into the playbook.
Configure the action to run on
All URLs
.
Use the expression builder to insert the
country
placeholder in the
Entity Identifies
field. For the
Entity Type
, choose
Generic Entity
and click
Save
.
Add the
Is in Custom List
action:
Drag the action into the playbook.
Configure it to run on all generic entities (the entity you just created).
For the
Category
, add the category you configured for your custom list of OECD countries.
Add the
IF condition
to your playbook to determine
    whether the domain's country requires further investigation. The first branch checks if the script
    result for the
Is in Custom list
returned a false result and the
Else
branch will go to the opposite result.
Add the
IF Condition
action to your playbook. Two branches appear.
Customize the first branch. The first branch executes if the
Is in Custom List
action returns a false result. This means the domain's country is not in your custom list of OECD countries and requires further investigation.
For the first action in this branch, drag a
Case Tag
action from the Google SecOps  integration.
Assign the case to a higher tier
Assign the case to a higher tier to further
investigate this case. To do this, follow these steps:
Drag the
Assign Case
action to the playbook.
Choose
@Tier2
as the
Assigned User
.
Change the priority
Change the priority to
High
using
    the
Google SecOps Change Priority
action
>
click
Save
.
Customize the Else branch
After finishing the first branch, you can customize the
Else
branch.
    This branch handles cases where the domain's country is an OECD country, which you've decided doesn't require further investigation. To configure the
Else
branch, follow these steps:
Add a case tag, as you did in the first branch, with the label
In OECD countries
.
Add a
Close Case
action to this branch. Because closing a case is a sensitive action, you should configure it to run manually. In the
Settings
section of the action, select
Manual
mode.
In the
Parameters
section of the
Close Case
action, add the
Reason
,
Root Cause
, and
Comment
.
Click
Save
to save the playbook with the added parameters.
View the playbook execution
To see your customized automation in action, follow these steps:
In
Cases
, click
add
Add
>
Simulate Cases
.
Select
Phishing Email
case
>
click
Create
.
Select the
Environment
>
click
Simulate
to simulate the playbook execution.
View the playbook running on the alert and see the results of each action in the playbook.
Need more help?
Get answers from Community members and Google SecOps professionals.
