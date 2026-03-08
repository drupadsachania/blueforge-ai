# Meta section syntax

**Source:** https://docs.cloud.google.com/chronicle/docs/yara-l/meta-syntax/  
**Scraped:** 2026-03-05T09:33:24.862456Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Meta section syntax
Supported in:
Google secops
SIEM
The
meta
section of a YARA-L rule is required and must appear at the start of the query.
This section can include multiple lines, where each line defines a key-value pair. The
key
is a string value without quotes, and the
value
is a string with quotes, such as:
<key> = "<value>"
For example:
rule failed_logins_from_new_location {
  meta:
   author = "Security Team"
   description = "Detects multiple failed logins for a user from a new, never-before-seen IP address within 10 minutes."
   severity = "HIGH"

  ... rest of the rule ...
}
What's next
Events section syntax
Match section syntax
Outcome section syntax
Condition section syntax
Options section syntax
Additional information
Expressions, operators, and constructs used in YARA-L 2.0
Functions in YARA-L 2.0
Build composite detection rules
Examples: YARA-L 2.0 queries
Need more help?
Get answers from Community members and Google SecOps professionals.
