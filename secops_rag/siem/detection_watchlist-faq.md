# Watchlists FAQ

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/watchlist-faq/  
**Scraped:** 2026-03-05T09:31:53.755581Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Watchlists FAQ
Supported in:
Google secops
SIEM
What are Watchlists?
Watchlists let you manually curate lists of entities to monitor (in Risk
Analytics only) based on internal risk considerations.
Where are Watchlists located?
On the
Risk Analytics
dashboard, click the
Watchlists
tab to access 
watchlists.
Why use Watchlists?
Watchlists allow you to monitor specific entities, boosting or suppressing your 
risk scores in the system. They are useful for tracking entities that may not 
have high risk scores, but are important to monitor based on internal risk 
considerations.
How do Watchlists enhance risk scoring?
Watchlists incorporate human expertise and context into the risk assessment 
process. Analysts can ensure that high-value assets, sensitive data locations, 
or specific you receive appropriate attention. An example of this is the use of 
multiplying factors (see below).
How many Watchlists can I create?
You can configure up to 200 watchlists.
What is a Multiplying factor in Watchlists?
A Multiplying factor, with values ranging from 0-100, can be applied to each 
watchlist to modify the risk score of all entities in that watchlist. 
The default value is 1.
How do I add a Watchlist?
To add a watchlist, do the following:
1. Click
Create watchlist
.
1. Enter a
Watchlist name
, an optional
Description
, and an optional
Multiplying factor
. 
1. Add the entities to the watchlist.
What type of entities can be added to a Watchlists?
You can add entities to a Watchlists based on the following types: 
  -
ASSET_IP_ADDRESS
-
EMAIL
-
EMPLOYEE_ID
-
HOSTNAME
-
MAC
-
PRODUCT_OBJECT_ID
-
PRODUCT_SPECIFIC_ID
-
USERNAME
-
WINDOWS_SID
What actions can I perform on Watchlists?
You can create, edit, pin, unpin, and delete watchlists, and add or 
remove entities from them.
What are some use cases for Watchlists?
Watchlists can be used to monitor employees about to leave a company, track 
unusual activity, or manage the alerts triggered by an 
internal red team.
Need more help?
Get answers from Community members and Google SecOps professionals.
