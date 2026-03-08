# Increase Playbook resilience with automatic retries

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/retry-actions/  
**Scraped:** 2026-03-05T10:08:09.736939Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Increase Playbook resilience with automatic retries
Supported in:
Google secops
SOAR
Automated actions in playbooks can sometimes fail
due to temporary problems like network outages or API rate limits. To make sure
your playbooks are more resilient, you can configure individual actions to
automatically retry if they encounter such failures.
Action retries help your playbooks recover from temporary failures like 
network issues, API rate limits, or service unavailability. These retries apply
to standard playbook actions, such as enrichment, containment, or notifications.
The retry mechanism is triggered by the action's internal execution status,
not by standard HTTP error codes. Retries aren't attempted for actions that
encounter timeouts or actions used for flow control (like conditions or playbook
blocks), as these aren't designed to fail in the same way.
Action retry mechanism conditions
The retry mechanism is triggered only when an action fails under specific
conditions that typically indicate a transient, infrastructure, or unhandled
failure. It's not activated for failures related to timeouts or flow control
actions.
Conditions that activate a retry
The retry mechanism is activated only when the action fails under the
following circumstances:
Unhandled script errors:
Any error or exception that occurs within
  the action's Python script that you don't explicitly handle in your script.
Explicit failure status:
The action script explicitly returns the
  execution state
EXECUTION_STATE_FAILED
to the server.
Infrastructure failures:
Failures that stem from the underlying
  infrastructure, such as connection issues (for example, Python connection
  errors) that prevent a successful outcome.
Conditions that bypass a retry (no retry attempted)
Retries are bypassed in failure scenarios related to timeouts or flow control
actions:
Playbook execution timeout:
The action fails to complete and return
  a result within the configured general timeout limit for the specific playbook
  step.
Handled timeout status:
The action script explicitly reports an
  internal action timeout by returning the status
EXECUTION_STATE_TIMEOUT
. The server treats this as a
  "Handled Timeout," which lets the playbook execution continue without a retry.
Configure action retries
To configure retries for an action, follow these steps:
Double-click the relevant action in the playbook designer.
In the sidebar, click the
Settings
tab, and then click
  the
Retry on failure
toggle to the on position.
Specify the following parameters:
Number of retries:
Enter how many times the action should
      attempt to rerun if it fails.
Delay between retries:
Define the delay in seconds, minutes, or
      hours between each retry attempt.
In the
If step fails
section, select one of the following options
  if the action ultimately fails after all retry attempts:
Stop playbook
: The playbook execution stops.
Skip step
: The playbook continues to the next step.
Click
Save
.
How retries appear during playbook execution
When a playbook step with retries runs, you'll see specific statuses and
messages indicating the progress of retry attempts:
If an action fails with retries configured, its status in the
Playbooks
tab temporarily changes to
Waiting for next retry
before the next attempt.
If the action succeeds after one or more retries, its final status in the
Playbooks
tab indicates success, along with the number of retries (for
  example,
Completed after two retries
).
If the action fails after all retry attempts, its final status indicates
  failure, along with the number of retries (for example,
Failed after 3
  retries
).
Relevant information about retry attempts also appears on the
Case
  Wall
.
Need more help?
Get answers from Community members and Google SecOps professionals.
