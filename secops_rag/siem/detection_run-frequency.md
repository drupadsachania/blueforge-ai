# Set the run frequency

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/run-frequency/  
**Scraped:** 2026-03-05T09:31:37.355261Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Set the run frequency
Supported in:
Google secops
SIEM
Rule run frequency impacts the latency with which detections are discovered for
each rule. Longer run frequencies increase the amount of time between when an
event occurs and when a detection is processed for that event.
For details, see
Detection latencies
.
To specify the run frequency for a rule, complete the following steps:
Navigate to the Rules Dashboard.
Open the rule options menu.
Click
Run frequency
.
Choose one of the
Run frequency
values.
Near Real-time
: Single-event rules can be executed over data in streaming
fashion. The detection engine executes rules as soon as data is processed.
10 min
: For multi-event rules, choose this frequency if you want your
detections as soon as possible.
1 hr
: Detections begin to process after 1-2 hours, after which they are
subject to normal detection latency.
24 hrs
: Detections begin to process after 24 hours, after which they
are subject to normal detection latency.
The run frequency for multi-event rules is automatically set based on the rule's match window:
For a window size of 1 to 48 hours, the run frequency is 1 hour.
For a window size greater than 48 hours, the run frequency is 24 hours.
Need more help?
Get answers from Community members and Google SecOps professionals.
