# Use the Gemini Case summary widget

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/using-the-gemini-case-summary-widget/  
**Scraped:** 2026-03-05T09:34:07.197749Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use the Gemini Case summary widget
Supported in:
Google secops
SOAR
The
Gemini Summary
widget analyzes the following case data to 
generate an AI-based assessment of how much attention the case might require:
Raw JSON of the event
Involved entities
Graph data for involved entities (to determine if they have appeared in 
previous malicious cases)
Similar cases
The widget also summarizes alert data to improve threat insights and recommends 
next steps for remediation.
You can provide feedback on the accuracy and usefulness of the AI-generated
classification, summary, and remediation recommendations.
The
Gemini Summary
widget appears in the
Case Overview
tab on the
Cases
page. For cases with only one alert, you must manually
click the
Case Overview
tab to view the widget.
Provide feedback for Gemini Summary
To submit feedback on the Gemini Summary, follow these steps:
Choose one of the following:
Click
thumb_up
Thumb up
if the summary is accurate and helpful. Optionally, enter comments in the
Additional Feedback
field.
Click
thumb_down
Thumb down
if the summary is inaccurate or unhelpful. Select a reason from the list and enter any relevant context in the
Additional Feedback
field.
Click
Send Feedback
to submit your response.
Remove the Gemini Summary widget
The
Gemini Summary
widget is included, by default, in the case view layout.
To remove it from the default view, follow these steps:
Go to
SOAR Settings
>
Case Data
>
Views
.
Select
Default Case View
.
Locate the
Gemini Summary
widget and click
delete
Delete
.
Need more help?
Get answers from Community members and Google SecOps professionals.
