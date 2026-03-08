# Create a test case

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-test-case/  
**Scraped:** 2026-03-05T09:34:02.612107Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create a test case
Supported in:
Google secops
SOAR
This document explains how to create and use a test case, which acts like a
  sandboxed version of a regular case. Any actions you perform on entities in a
  test case don't affect the same entities in other cases. A test case includes
  only the alert that triggered the event and is populated using existing data.
  You can use it to simulate a playbook or test behavior on the
IDE
page.
To create a test case, follow these steps:
In the platform, go to the
Cases
page.
Select the required case and go to the
Alert
tab.
Click
more_vert
Alert Options
next to the
Alert
tab.
In the
Alert Options
menu, click
Ingest alert as test case
.
Select the required environment and click
Simulate
.
Refresh the page.
A new test case appears in the case queue or list view. It's marked with
    the label
Test
on the case card and contains only one alert.
You can now use the test case in the Playbook Simulator, or the
IDE testing
page.
Need more help?
Get answers from Community members and Google SecOps professionals.
