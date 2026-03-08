# Watchlist Quickstart guide

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/watchlist-getting-started/  
**Scraped:** 2026-03-05T09:31:48.060710Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Watchlist Quickstart guide
Supported in:
Google secops
SIEM
Learn how to use the
Watchlist
section. Watchlists in Google SecOps 
lets you manually curate entity lists to monitor, boost, or suppress their risk 
scores in the system. Security analysts can prioritize investigations and focus 
on entities that might be particularly important, even if their automated risk 
scores are low.
Before you begin
To access the Watchlist tab, follow these steps:
In the left navigation menu, click
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
Watchlists
Watchlists in Google Security Operations allow users to manually curate lists 
of entities to monitor, boosting or suppressing their risk scores in the system. 
This enables security analysts to prioritize investigations and focus on entities 
that may be of particular concern, even if their automated risk scores are low.
Enhance risk scores with human insights
While Google SecOps' automated risk scoring provides valuable insights, watchlists 
incorporate human expertise and context into the risk assessment process. 
For example, a security analyst might have knowledge of high-value assets, 
sensitive data locations, or specific users who warrant closer monitoring. 
By adding these entities to a watchlist, analysts can ensure they receive 
appropriate attention, regardless of their computed risk scores.
The
Watchlists
page lets you monitor specific entities from across your 
enterprise according to preferences of your enterprise, regardless of the 
entity's risk score. For example:
Create a watchlist of employees about to leave the company to monitor any 
possible data exfiltration
Create a watchlist of the C-suite to monitor closely any subtle changes in 
their security posture.
Create a watchlist
To create a watchlist to your Google SecOps account, complete the 
following steps. You can configure up to 200 watchlists.
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
1
.
(Optional) Specify entities on the right side of the window following the
Add entities into a watchlist
section. You can add the following entity types here:
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
A watchlist lets you globally apply a risk score modifier to a set of entities. 
This modifier, called
Multiplying factor
, refines the risk scores for all 
entities in the watchlist. Each entity's base risk score is multiplied by the 
same factor. Enter a multiplying factor with a value from 0 -100. The default 
value is 1.
In addition to creating a watchlist, you can edit a watchlist, pin/unpin, 
delete and add entities to/ remove entities from it. 
For more on how to create watchlists, see
Add a watchlist
.
Use cases
Here are a few use cases for the Watchlist section.
Use case 1:
Create a watchlist to track activities of employees about to leave your company. 
These employees may attempt to copy internal specifications, plans, or 
presentations, particularly in highly competitive industries. For most employees, 
this type of information would be of little value, since that type of behavior 
would typically be considered to be normal.
Use case 2: Unusual activity among senior leaders
Create a watchlist to track unusual activity among senior leaders within your 
organization. Leadership is frequently targeted by spear phishing attacks. 
Sudden increases in invoices or requests for funds transfers to outside accounts
can be monitored using a watchlist, in particular when known phishing attacks 
have been identified within your enterprise.
Use case 3: internal red team
Create a watchlist for an internal red team that is active in your 
enterprise. The red team could trigger numerous alerts within your security 
infrastructure (as expected). You can specify the watchlist with a multiplying 
factor of 0 to reduce their visibility while they are in an active exercise. 
For more information, see
Add a watchlist
.
What's next
Add a watchlist
Edit a watchlist
Pin a watchlist
Unpin a watchlist
Delete a watchlist
Add entities to a watchlist
Need more help?
Get answers from Community members and Google SecOps professionals.
