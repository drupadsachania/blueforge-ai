# Risk Analytics dashboard

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-dashboard/  
**Scraped:** 2026-03-05T10:04:21.118256Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Risk Analytics dashboard
Supported in:
Google secops
SIEM
The
Risk Analytics
dashboard lets you view your environment through a
risk-based lens. Visualizing entity risk trends helps you identify unusual
behavior and understand the potential risk that entities pose to your
enterprise.
The
Risk Analytics
dashboard lists at-risk entities and risk factor details.
On systems that use data RBAC, only users with global scope can access
risk analytics. For more information, see
data RBAC impact on Risk analytics
.
To get to the
Risk Analytics
dashboard, follow these steps:
In the navigation bar, click
Detection
.
From
Detection
, click
Risk Analytics
.
Entity count, risk score, and entities table
Based on the filters you select, the
Risk Analytics
dashboard displays only
the top 10,000 entities with the highest risk in the enterprise.  All graphs and tables
in the dashboard represent only this set of entities.
The
Total entity count
graph to the top left displays the number of entities
being tracked in your enterprise with a risk of greater than 0. Entities with a
risk score of 0 are still being tracked, but they won't be represented in this
graph. The total count is divided between
Assets
and
Users
.
For more information on entities, see
Logical objects: Event and
Entity
.
For more information on how risk scores are calculated, see
Risk score
calculation
.
In the
Entities
table, there are multiple columns relating to the entity
risk score:
Column
Value
Entity name
Name of entity.
Entity type
Type of entity (Asset or User).
Normalized
Normalized scores are calculated across entities, scaled between 0-1000 using min-max normalization.
Normalized change
Change in the normalized entity risk score since the previous risk calculation window.
Normalized trend
Increase or decrease in the percentage change of the normalized risk score compared to the previous risk window.
Base
Base entity risk score equals the maximum finding risk score plus the weighting times the sum of remaining findings risk scores.
The weighting default is .2 and can be changed in Settings.
Base change
Change in the base entity risk score since the previous risk calculation window.
Base trend
Increase or decrease in the percentage change of the base risk score compared to the previous risk window.
Findings count
The number of findings (alerts and detections) that include this entity during the risk calculation window.
First seen in window
Timestamp when the entity was first seen in a finding (alert or detection) during the risk calculation window.
Last seen in window
Timestamp when the entity was last seen in a finding (alert or detection) during the risk calculation window.
Adjust the risk calculation window
The calculated risk posed by an entity changes depending on the period of time
under examination. Changing the
Risk Calculation Window
setting at the top
right (select either
24 Hour Window
or
7 Day Window
) changes the
calculated risk score displayed here. You might want to change this setting
depending on the type of attack you are looking for. For example, brute force
attacks are more apparent by setting the
Risk Calculation Window
to
24
Hours
. Longer time frames let you spot long-term attacks. Entity risk scores change depending on the selected risk calculation window.
Entity risk scores are recalculated multiple times daily for both 24-hour and 7-day look-back windows, based on the findings generated within those respective look-back   periods. The risk dashboard provides the most recently calculated risk scores. You can also view historical risk scores by selecting a specific date and time in the date selector next to the "Risk Calculation Window" setting. This will display the entity risks calculated for the 24-hour or 7-day window ending at the chosen date and time.
Narrow your search with quick filters
Quick filters let you narrow your search by only showing results relevant to
your specific needs.
To use Quick filters on
Risk Analytics
dashboard, follow these steps:
Click
filter_alt
above
the
Entities
table. The
Filters
window appears.
Select one of the columns:
Number of findings
Normalized entity risk score
Normalized entity risk trend
Type
Select
Show only
or
Filter out
.
Select a value (you can select more than one value to expand the range):
Number of findings
: Values from 0 to greater than 1000.
Normalized entity risk score
: Values from 0 to 1000.
Normalized entity risk trend
: Percentages from less than -99%
to greater than 199%.
Type
: Select
Assets
or
Users
.
(Optional) To add additional filters, click
Add filter
and repeat this
process from step 2.
After you have finished configuring filters, click
Apply
.
For example, if you select the
Normalized entity risk trend
, select
Show
only
, and check
>199%
, only the entities with a normalized entity risk
change greater than 199% are displayed.
Investigate an entity using the entity page
To investigate an entity, follow these steps:
Scroll through the
Entity Name
column or use the search bar to find an
entity.
Click the entity you want to investigate.
This opens the entity page. This page lets you examine just the findings
associated with that one entity. The
Findings timeline
chart at the top
tracks entity risk scores and findings over time. This chart is made of
pre-computed metrics displayed in a line graph format to show trends over time.
Anomalies can be seen as spikes on the line graph. Below the chart is the
Findings
table, showing which events and activities the selected entity has
been associated with.
There is a collapsible
View entity details
panel at the bottom right that
contains a summary of important details about the selected entity. To complete a
detailed examination of the selected entity, click
View entity details
to
view the entity in
Asset
view or
User
view depending on whether the
entity is an asset or user respectively. For more information, see
Investigate
an asset entity
or
Investigate a user
.
Investigate an entity using entity analytics
Entity analytics provides SOC analysts and threat hunters with a detailed view
of an entity's behavior, including the entity's baseline profile, anomalies, and
contextual enrichments.
From the entity page, select a time range of up to 90 days on the
Findings
timeline
, and click
View analytics for selection
. This opens a sidebar
which shows you the analytics associated with this entity within the selected
time range. Each analytic displays an aggregate of all the analytic values
within the time range. When detected, an analytic includes a list of related
alerts and detections that can be examined further by clicking
View more
to
open the corresponding
Alerts
or
Detection
view. For more information,
see
Investigate an alert
.
The following entity analytics are provided:
Alert Event Name Count
Authentication Attempts Success
Authentication Attempts Fail
Authentication Attempts Total
DNS Bytes Outbound
DNS Queries Fail
DNS Queries Success
DNS Queries Total
File Executions Success
File Executions Fail
File Executions Total
HTTP Queries Success
HTTP Queries Fail
HTTP Queries Total
Network Bytes Inbound
Network Bytes Outbound
Network Bytes Total
Workspace Authentication Attempts Total
Workspace Emails Sent Total
Workspace Network Bytes Outbound
Workspace Network Bytes Total
Workspace Total Change Actions
Workspace Total Download Actions
Modify an entity risk score
When outside information or events affect the true risk of an entity, you can
update the entity's risk score.
For example, you can temporarily decrease the risk score of an employee who just
finished a red team exercise (such as penetration testing) so analysts don't
have to waste time investigating why that employee had a risk increase. You
could also temporarily increase the risk score of an employee involved in a
court case.
From the
Entities
table on the
Risk Analytics
page, hold the
pointer over the far right column of the row. You might need to scroll your
display to the right. Click
more_vert
and select
Update entity risk score
.
From the
Update entity risk score
dialog, configure values for
following:
Multiplication factor
: Lets you increase or decrease the risk
score of an entity with a multiplying factor of 0.0 - 100.0. For
example, if you've discovered new evidence about an entity that makes
the entity twice as risky, update the multiplication factor to 50 to
reflect the entity's true risk factor.
Time period
: Period of time when the multiplication factor is
applied. You can select
Now
or between
1 day
and
14 days
. 
If you select
Now
, the multiplying factor is applied to the entity 
risk score for the current risk calculation window. Only existing 
alerts and detections are included in the calculation.
When the selected time period is over, updates to the entity risk score
stop and the risk score returns to normal.
Reason
: Lets you leave additional context for other users about
why this update was made. Choose from the following options:
New
evidence
,
Incorrect risk score
,
Changed risk profile
,
Compliance requirements
, or
Other
.
If you attempt to make a change that has already been made (for example, you
want to update an entity's multiplication factor to 25%, but another team member
has already made that change), a dialog will appear saying the change has
already been made, including information about who made the change and when.
View risk score updates in entity details
You can view all risk score updates for an entity in the
Entity profile
page.
Click the entity whose risk score update history you want to view to open
the
Entity profile
page.
In
Event timeline chart
, each time someone has changed the entity's risk
score is indicated by the
Risk Score modification
label in white text.
Hold the pointer over the text to display a dialog with the date, user, and
reason for the change.
Watchlists
The
Watchlists
page lets you monitor specific entities from across your
enterprise.
Navigate to the Watchlists tab
In the left navigation bar, click
Detection
.
From
Detection
, click
Risk analytics
.
Click the
Watchlists
tab.
Add a watchlist
To add a watchlist to your Google Security Operations account, complete the following
steps. You can configure up to 200 watchlists.
Click
Create watchlist
.
Specify a
Watchlist name
.
(Optional) Specify a
Description
.
(Optional) Specify
Multiplying factor
of between 0-100. The default is
1.
(Optional) Specify entities on the right side of the window following the
Add entities into a watchlist
section. You
can add the following entity types here:
ASSET_IP_ADDRESS
EMAIL
EMPLOYEE_ID
HOSTNAME
MAC
PRODUCT_OBJECT_ID
PRODUCT_SPECIFIC_ID
USERNAME
WINDOWS_SID
Click
Create watchlist
.
Pin a watchlist
Click
Edit display
.
Click the checkbox next to the watchlist you want to pin.
Click
Save
.
Unpin a watchlist
From the
Watchlists
dashboard, select the watchlist you want to unpin
and select
more_vert
.
Click
Remove from display
.
Edit a watchlist
From the
Watchlists
dashboard, select the watchlist you want to edit and
click the
more_vert
icon.
Click
Edit watchlist
.
Delete a watchlist
From the
Watchlists
dashboard, select the watchlist you want to delete
and click
more_vert
.
Click
Delete watchlist
.
Add entities to a watchlist
To add entities to a watchlist, you specify the entity name, type, and
(optional) namespace line by line using one of the following formats.
NAME
,
TYPE
NAME
,
TYPE
,
NAMESPACE
TYPE
can be one of the following:
ASSET_IP_ADDRESS
EMAIL
EMPLOYEE_ID
HOSTNAME
MAC
PRODUCT_OBJECT_ID
PRODUCT_SPECIFIC_ID
USERNAME
WINDOWS_SID
NAMESPACE
can only be specified for the asset
    entity types:
ASSET_IP_ADDRESS
HOSTNAME
MAC
PRODUCT_OBJECT_ID
PRODUCT_SPECIFIC_ID
For example:
205.148.5.0,ASSET_IP_ADDRESS
website.com,HOSTNAME,chronicle
This example represents two entities added into watchlist, an asset IP address
205.148.5.0
and a hostname
website.com
under the
chronicle
namespace. You
can have up to 10,000 entities in a watchlist.
Remove entities from a watchlist
To remove entities from a watchlist, remove the lines that represent entities
you want to remove and click
Save
.
Change risk score settings
The
Entity Risk Score
page lets you define how risk scores are calculated
for entities, alerts, and detections. This page lets you tailor how risk is
calculated based on the unique needs of your search.
There are three fields in the
Entity Risk Score
page that you can update:
Entity risk score weighting
Default alert risk score
Default detection risk score
To change any of these settings, follow these steps:
From the navigation bar, select
Settings > Entity Risk Scores
.
Update the risk scores accordingly.
Click
Save
. When you return to the main
Risk Analytics
page, you
will see a message at the top of the screen confirming that a change had
been made to
Entity Risk Score
.
(Optional) To re-set any of these values, click
Reset
to the right of
the value.
Updates will only apply to new alerts and detection. It may take up to 30
minutes for the changes to take effect.
Entity risk score weighting
Weighting defines how alert and detection risk scores contribute to entity risk
score calculations. Weighting is a value from 0-1 and the default is 0.2.
Here are some examples of how different numbers impact the entity risk score
calculation:
Entity risk score weighting
0
. The raw risk score is the maximum
detection risk score among all detections for the entity.
Entity risk score weighting
1
. The raw risk score is the sum of all
the detection risk scores for the entity.
Entity risk score weighting
0.5
. The risk score gives full weight to
the detection with maximum risk score for the entity and half the weight for
all other detections.
Default risk score for detections
Default risk score for detections
lets you assign a default value for
detection risk scores. Detection risk scores are used to calculate entity risk
scores. Risk scores for detections are defined when a rule is written. If no
risk score is defined in the rule, the default value is used. The default score
is 15 and the risk score range is 0-100.
Default risk score for alerts
Similar to
Default risk score for detections
, this field lets you assign a
default value for alert risk scores. If no risk score is defined in the rule,
the default of 40 is used. The risk score range is 0-1000.
For information about defining the risk score in a rule, see
Outcome section
syntax
.
Closed Alert Coefficient
The closed alert coefficient modifies the risk score of alerts marked as closed
by analysts. It is a floating point modifier between 0 and 1 inclusive. The
default is 1.0, meaning that all open and closed alerts retain their original
scores. If the closed alert coefficient has a value of 0.0, all of the closed
alerts receive a risk score of 0 and would no longer increase the risk score of
the overall entity.
Need more help?
Get answers from Community members and Google SecOps professionals.
