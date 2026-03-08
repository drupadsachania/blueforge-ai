# Risk analytics FAQ

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/risk-analytics-faq/  
**Scraped:** 2026-03-05T10:04:27.075370Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Risk analytics FAQ
Supported in:
Google secops
SIEM
What is Risk Analytics?
The
Risk Analytics dashboard
helps you identify unusual behavior and potential risks posed by entities within 
an enterprise. It consists of two main sections: 
Behavioral Analytics and
Watchlists
.
Who can access Risk Analytics?
Only users with the relevant privileges can access Risk Analytics. If your 
organization uses
data RBAC
, 
you need to have global scope to access risk analytics.
What is Behavioral Analytics?
The
Behavioral Analytics
section lists entities based on their
Google Security Operations
entity risk scores
.
The section offers these key components:
Summary metrics
: Shows a top-level view of entities based on Google SecOps entity risk modeling. This visualization displays up to
10,000 entities with the highest risk scores
.
Entities table
: Tracks an entity's risk over time and provides context for investigations.
How does the Risk Calculation Window work?
The
Risk Calculation Window
lets users change the timeframe for the dashboard, enabling the analysis of 
data over different periods. Shorter timeframes, such as 24 hours, help uncover 
events like brute force login attempts, while longer timeframes, such as 7 days, 
help in examining long-term malicious activity.
Can I view historical risk scores?
Yes, you can view historical risk scores by selecting a specific date and time, 
which displays risks calculated for the selected 24-hour or 7-day window.
What is a normalized risk score?
Normalized scores are set between 1 and 1,000 to distinguish entities with 
detections from those without.
What are base risk scores?
Base scores are calculated by adding the risk scores across findings (alerts and 
detections) for an entity during the risk window, with weighting applied.
How is weighting applied to risk scores?
Risk score weighting
defines how alert and detection risk scores contribute to entity risk score 
calculations, with values ranging from
0
to
1
, where a weighting of
1
has no impact on the risk 
score. The default weighting value is
0.2
and can be modified in
Settings
.
How is the base entity risk score calculated?
The formula for the base entity risk score is: 
(Maximum risk score for the finding) + (Weighting * (Sum of the remaining risk 
scores for the findings)).
What are default risk scores for alerts and detections?
The default risk score for alerts is 40 and for detections is 15. You can modify these defaults 
in
Settings
or within rules.
What is the closed alert coefficient?
If a security analyst marks an alert as
closed
, its risk score is multiplied by 
a coefficient that ranges from 0 to 1 .
How do Risk Score modifications with TTL and without TTL work?
The Base entity risk score is modified by a multiplying factor for the time range, 
and the detection risk score is modified with a multiplying factor. These factors 
are specified by Google SecOps.
How are normalized risk scores calculated?
Base entity risk scores are normalized using min-max normalization and range 
from 1 to 1,000. Entities with a 0 risk score are excluded.
What is the Entity Analytics page?
Clicking an entity name in the Entities table leads to the
Entity Analytics
page, 
which displays an Event range window, a Findings Timeline, and a detailed Findings 
table. The Event range window allows filtering up to 90 days.
What are some examples of how Risk Analytics can be used?
You can use Risk Analytics to identify high data download volumes, suspicious 
numbers of failed login attempts, or dialog messages that may indicate malware.
Need more help?
Get answers from Community members and Google SecOps professionals.
