# Understand detection limits

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/detection-limits/  
**Scraped:** 2026-03-05T10:04:06.329165Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Understand detection limits
Supported in:
Google secops
SIEM
Google Security Operations has the following limitations with regards to rule detections:
Each rule version has a limit of 10,000 detections per day. This limit
resets at midnight UTC.
For example, a rule version might generate 9,900 detections by 3 PM UTC on
January 1. If all these detections are recorded for January 1, it generates
only 100 more detections that day. On January 2, the rule version can
generate 10,000 new detections.
If the rule version is updated, the limit is reset and the rule can again
generate 10,000 detections in that same day.
For example, if a rule version produces 9,900 detections by 3 PM UTC on
January 1, and all of these detections have a detection time on January 1,
it generates only 100 more detections for that day. If rule version is
updated at 4 PM on January 1, the rule version can generate 10,000
detections with a detection time on January 1 until the end of day. On
January 2, the rule version can generate another 10,000 new detections.
The
Rules Dashboard
can display up to 50 MB of detection data. If the
total size of the detections exceeds this limit, the interface shows a
message indicating that the data is incomplete. This means the system
generated more detections than the interface can display, but the detections
still exist and are not lost.
Running a retrohunt after updating the reference list doesn't reset the
existing detections limits or generate new ones. If the existing detection
limit has already been reached, no new detections are generated.
Retrohunts
limitations:
Run a maximum of 3 concurrent retrohunt jobs for each Google SecOps instance or tenant.
The combined text size of all rules must not exceed 1 MB.
If you run multiple retrohunts in parallel, the system allocates 
resources from the same Google SecOps instance. This can lead
to slower performance or delays in job completion.
Need more help?
Get answers from Community members and Google SecOps professionals.
