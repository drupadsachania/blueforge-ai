# View rule error details

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/rule-errors/  
**Scraped:** 2026-03-05T09:31:40.181142Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
View rule error details
Supported in:
Google secops
SIEM
This document outlines the two primary categories of errors encountered when working with detection logic:
compilation errors
and
runtime errors
:
Compilation errors
: Identify syntax or logic issues through static analysis.
Runtime errors
: Surface specifically during active rule testing, live execution, or the performance of a retrohunt.
Compilation errors
Google Security Operations identifies compilation errors when you save or test the rule.
Click
error
to view error details in the
Runtime Error
dialog.
If there is no error in your rule, the icon is a green
done
. If the error message includes a column or line position,
that part of the rule is displayed with a red underline in the rules editor.
More complex errors don't included a position because they are caused by a combination of issues in multiple places.
If you try to save a rule or test a rule that has a compilation error, a runtime error is displayed. You cannot save a rule or run a test
until the compilation error is fixed.
Runtime errors
Runtime errors don't display during compile time. Some runtime errors prevent a rule from completing, like
query took too long to execute
, which occurs sporadically. To verify if your rule has runtime errors, click
Run test
in the rules editor.
If a runtime error occurs, a link is displayed in the
Test rule results
bar
that gives more information about the error that occurred.
It's possible to get unknown runtime errors that don't have a useful
description. This indicates that the system is encountering
this particular error for the first time and it doesn't have a user message associated with the error.
If this happens, contact your Google SecOps representative for assistance.
If a runtime error occurs during live rule or retrohunt execution, a link is
displayed on the
Detections
page that gives more information about the error that occurred.
Similarly to test the rule, runtime errors that occur during live rule or retrohunt
execution have an indicator with clickable, underlined text that gives
more information about the error that occurred.
Need more help?
Get answers from Community members and Google SecOps professionals.
