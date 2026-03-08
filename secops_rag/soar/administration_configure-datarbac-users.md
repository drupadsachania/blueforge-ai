# Configure data RBAC for users

**Source:** https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users/  
**Scraped:** 2026-03-05T09:45:37.282779Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure data RBAC for users
Supported in:
Google secops
SIEM
This page describes how
data role-based access control
(
data RBAC
)
administrators can configure data RBAC within Google Security Operations. Through
the creation and assignment of data scopes, which are defined by labels,
you can ensure that data is only accessible to authorized users.
Data RBAC relies on
IAM
concepts including
predefined roles
,
custom roles
,
and
IAM conditions
.
The following is a high-level overview of the configuration process:
Plan your implementation:
identify the different types of data you want
to restrict user access to. Identify the different roles within your
organization and determine the data access requirements for each role.
Optional: Create custom labels:
create custom labels (in addition to the
default labels
)
to categorize your data.
Create data scopes:
define scopes by combining relevant labels.
Assign scopes to users:
assign scopes to user roles in IAM
based on their responsibilities.
Enable data RBAC:
enable data RBAC to apply the scope assignments.
You have the following two options to set up data RBAC:
Enable data RBAC
before
assigning scopes:
when data RBAC is
enabled, rules, reference lists, and data tables don't
have any scopes assigned. Only users with global access have access to the
data. Scoped users don't have access to any data by default. This prevents
unintended access and ensures a secure starting point. To grant
access, define scopes and assign them to users, rules, and reference lists based
on your requirement.
Enable data RBAC
after
assigning scopes:
setting up and assigning
scopes in advance provides immediate data access to users when data RBAC is
enabled. Additionally, since rules have scopes assigned, the generated
detections are tagged with scopes. This allows users to see detections that
were generated after the scope assignments.
Before you begin
To understand the core concepts of data RBAC, different access types, and the
corresponding user roles, the working of labels and scopes, and the impact of
data RBAC on Google SecOps features, see
Overview of Data RBAC
.
Onboard your Google SecOps instance. For more information, see
Onboarding or migrating a Google Security Operations instance
.
Make sure that you have the
required roles
.
Create and manage custom labels
Custom labels are metadata that you can add to the SIEM ingested
Google SecOps data to categorize and organize
it based on UDM-normalized values.
For example, consider you want to monitor network activity. You want to track
Dynamic Host Configuration Protocol (DHCP) events from a specific IP address
(10.0.0.1) that you suspect might be compromised.
To filter and identify these specific events, you can create a custom label with
the name Suspicious DHCP Activity with the following query:
metadata.event_type = "NETWORK_DHCP" AND principal.ip = "10.0.0.1"
The custom label works in the following manner:
Google SecOps continuously ingests network logs and events into its
UDM. When a DHCP event is ingested, Google SecOps checks if it
matches the criteria of the custom label. If the
metadata.event_type
field is
NETWORK_DHCP
and if the
principal.ip
field (the IP address of the device
requesting the DHCP lease) is
10.0.0.1
, Google SecOps applies the
custom label to the event.
You can use the Suspicious DHCP Activity label to create a scope and assign
the scope to the relevant users. The scope assignment lets you restrict access
to these events to specific users or roles within your organization.
Custom Label requirements and limitations
We recommend that you review the following limits and requirements when you define and use custom labels:
Naming and syntax requirements
Custom Label names must be unique and can have a maximum length of 63 characters.
The name can contain only lowercase letters, numeric characters, and hyphens.
A deleted label name cannot be reused after deletion.
Functional limitations
Custom Label query don't support the following advanced features:
Reference lists
Enrichment fields
Regular expressions
Data tables
Query execution time
: Custom label query is subject to a maximum execution time limit of 5 seconds.
Create custom label
To create a custom label, do the following:
Log in to Google SecOps
.
Click
Settings
>
SIEM Settings
>
Data Access
.
On the
Custom labels
tab, click
Create custom label
.
In the
UDM Search
window, type your query and click
Run Search
.
You can refine the query and click
Run Search
until the results display
the data that you want to label. For more information about running a query,
see
Enter a UDM Search
.
Click
Create label
.
On the
Create label
window, select
Save as new label
, and enter the
label name and description.
Click
Create label
.
A new custom label is created. During data ingestion, this label is applied
to data that matches the UDM query. The label is not applied to data that is
already ingested.
Modify custom label
You can only modify the label description and the query associated with a label.
Label names cannot be updated. When you modify a custom label, the changes are
applied only to new data and not to the data that is already ingested.
To modify a label, do the following:
Log in to Google SecOps
.
Click
Settings
>
SIEM Settings
>
Data Access
.
On the
Custom labels
tab, click
more_vert
Menu
against the label that you want to edit and select
Edit
.
In the
UDM Search
window, update your query and click
Run Search
.
You can refine the query and click
Run Search
until the results display
the data that you want to label. For more information about running a query,
see
Enter a UDM Search
.
Click
Save changes
.
The custom label is modified.
Delete custom label
Deleting a label prevents new data from being associated with it. Data that is
already associated with the label remains associated with the label. After
deletion, you can't recover the custom label or reuse the label name to create
new labels.
Click
Settings
>
SIEM Settings
>
Data Access
.
In the
Custom labels
tab, click the
more_vert
Menu
for the label that you want to delete and select
Delete
.
Click
Delete
.
On the confirmation window, click
Confirm
.
The custom label is deleted.
View custom label
To view a custom label details, do the following:
Click
Settings
>
SIEM Settings
>
Data Access
.
In the
Custom labels
tab, click
more_vert
Menu
against the label that you want to edit and select
View
.
The label details are displayed.
Create and manage scopes
You can create and manage data scopes within the Google SecOps user
interface, and then assign those scopes to users or groups through IAM.
You can create a scope by applying labels that define the data that a user
with the scope has access to.
Create scopes
To create a scope, do the following:
Log in to Google SecOps
.
Click
Settings
>
SIEM Settings
>
Data Access
.
On the
Scopes
tab, click
Create scope
.
In the
Create new scope
window, do the following:
Enter
Scope name
and
Description
.
In
Define scope access with labels
>
Allow access
, do the following:
To select the labels and their corresponding values that you want to
grant users the access to, click
Allow certain labels
.
In a scope definition, labels of the same type (for example, log type)
are combined using the OR operator, while labels of different types
(for example, log type and namespace) are combined using the AND
operator. For more information about how labels define data access in
scopes, see
Data visibility with allow and deny labels
.
To give access to all data, select
Allow access to everything
.
To exclude access to some labels, select
Exclude certain labels
, then
select the label type and the corresponding values that you want to deny
users the access to.
When multiple deny access labels are applied within a scope, access is
denied if they match
any
of those labels.
Click
Test scope
to verify how the labels are applied to the scope.
In the
UDM Search
window, type your query and click
Run Search
.
You can refine the query and click
Run Search
until the results display
the data that you want to label. For more information about running a query,
see
Enter a UDM Search
.
Click
Create scope
.
In the
Create scope
window, confirm the scope name and description
and click
Create scope
.
The scope is created. You must assign the scope to users to give them access to
the data in the scope.
Modify scope
You can only modify scope description and the associated labels. Scope names
cannot be updated. After you update a scope, the users associated with the scope
are restricted as per the new labels. The rules that are bound to the scope are
not re-matched against the updated one.
To modify a scope, do the following:
Log in to Google SecOps
.
Click
Settings
>
SIEM Settings
>
Data Access
.
On the
Scopes
tab, click
more_vert
Menu
corresponding to the scope that you want to edit and select
Edit
.
Click
edit
Edit
to edit the scope
description.
In the
Define scope access with labels
section, update the labels and
their corresponding values as required.
Click
Test scope
to verify how the new labels are applied to the scope.
In the
UDM Search
window, type your query and click
Run Search
.
You can refine the query and click
Run Search
until the results display
the data that you want to label. For more information about running a query,
see
Enter a UDM Search
.
Click
Save changes
.
The scope is modified.
Delete scope
When a scope is deleted, users don't have access to the data associated with
the scope. After deletion, the scope name cannot be reused to create new scopes.
To delete a scope, do the following:
Log in to Google SecOps
.
Click
Settings
>
SIEM Settings
>
Data Access
.
On the
Scopes
tab, click
more_vert
Menu
against the scope that you want to delete.
Click
Delete
.
In the confirmation window, click
Confirm
.
The scope is deleted.
View scope
To view scope details, do the following:
Log in to Google SecOps
.
Click
Settings
>
Data Access
.
In the
Scopes
tab, click
more_vert
Menu
against the scope that you want to view and select
View
.
The scope details are displayed.
Assign scope to users
Scope assignment is required for controlling data access for users with
restricted permissions. Assigning specific scopes to users determines the data
that they can view and interact with. When a user is assigned multiple scopes,
they gain access to the combined data from all those scopes. You can assign the
appropriate scopes to users who require global access so that the users can view
and interact with all the data. To assign scopes to a user, do the following:
In the Google Cloud console, go to the
IAM
page.
Go to IAM
Select the project that is bound to Google SecOps.
Click
person_add
Grant access
.
In the
New principals
field, do the following:
If you're using Workforce Identity Federation or any other third party
authentication,
add your principal identifier
as follows:
principal://iam.googleapis.com/locations/global/workforcePools/
POOL_ID
/subject/
USER_EMAIL_ADDRESS
Replace the following:
POOL_ID
: the identifier for the pool created for
your identity provider.
USER_EMAIL
: the user's email address.
If you're using Cloud Identity or Google Workspace,
add your principal identifier
as follows:
user:
USER_EMAIL
Replace the following:
USER_EMAIL
: the user's email address.
In the
Assign roles
>
Select a role
menu, select the required role.
Click
Add another role
to add multiple roles. To understand which roles need
to be added, see
User roles
.
To assign a scope to the user, add conditions to the Chronicle Restricted
Data Access role that is assigned to the user (does not apply to global access
roles).
Click
Add IAM condition
against the
Chronicle Restricted Data Access
role. The
Add condition
window appears.
Enter the condition title and the optional description.
Add the condition expression.
You can add a condition expression using either the
Condition builder
or the
Condition editor
.
The condition builder provides an interactive interface to select the
condition type, operator, and other applicable details about the expression.
The following operators let you create precise rules for controlling
access to multiple scopes with a single IAM condition:
ENDS_WITH
: checks if the scope name ends with a specific word. To match
the exact word, add a
/
before the word.
Consider an example data access scope named
projects/1234/locations/us/instances/2342-434-44-3434-343434/dataAccessScopes/scopename
.
ENDS_WITH /scopename
matches the exact name and evaluates as
true
for the example scope.
ENDS_WITH scopename
matches any name that ends with "scopename" and is evaluated as
true
for the example scope and also for
projects/1234/locations/us/instances/2342-434-44-3434-343434/dataAccessScopes/testscopename
.
STARTS_WITH
: checks if the scope name starts with a specific word. For
example,
STARTS_WITH projects/project1
grants access to all the scopes
within "project1".
EQUALS_TO
: checks if the name exactly matches a specific word or phrase.
This gives access to only one scope. For example,
EQUALS_TO projects/1234/locations/us/instances/2342-434-44-3434-343434/dataAccessScopes/scopename
evaluates as
true
for the example scope.
To add scopes to the role, we recommend the following:
Select
Name
in
Condition type
, the operator in
Operator
,
and enter the scope name in
Value
.
/<scopename>
To assign multiple scopes, add more conditions using the OR operator.
You can add up to 12 conditions for each role binding. To add more than 12
conditions, create multiple role bindings and add up to 12 conditions to
each of these bindings.
For more information about conditions, see
Overview of IAM conditions
.
Click
Save
.
The condition editor provides a text-based interface to manually enter an
expression using
CEL syntax
.
Enter the following expression:
(scope-name: resource.name.endsWith('
/SCOPENAME1
') || resource.name.endsWith('
/SCOPENAME2
') || … || resource.name.endsWith('
/SCOPENAME
'))
Replace
/SCOPENAME1
,
/SCOPENAME2
, and other placeholders with the
  scope names that you want to assign to the principle.
Click
Run Linter
to validate the CEL syntax.
Click
Save
.
Click
Test changes
to see how your changes affect the user access to
the data.
Click
Save
.
The users can now access the data that is associated with the scopes.
Enable data RBAC
Enabling data RBAC applies all assigned scopes to rules and
reference lists, making sure users see only the data relevant to their scopes. To
enable data RBAC, do the following:
Log in to Google SecOps
.
Click
Settings
>
SIEM Settings
>
Data Access
.
Navigate to the
Assignments
tab and review the scope assignments of the
rules and reference lists. To find specific items, use the filter or search
functionalities.
Click
Enforce data access
. The Enforce data access window displays the
number of rules and reference lists that will be scoped
after data RBAC is enforced.
Click
Yes, Enforce
.
Need more help?
Get answers from Community members and Google SecOps professionals.
