# Work with the Playbook Simulator

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/working-with-playbook-simulator/  
**Scraped:** 2026-03-05T10:08:03.613591Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Work with the Playbook Simulator
Supported in:
Google secops
SOAR
The
Playbook Simulator
provides a streamlined approach to develop
   playbooks with reduced time and effort.
The Playbook Simulator offers several key features, letting you:
Work in a pre-production environment, letting you test actions and observe results without impacting live production data (especially when the playbook is deactivated).
Facilitate the testing of each individual playbook step or block to confirm that the workflow operates as intended.
Test all possible condition branches within your playbook, confirming comprehensive coverage and predictable behavior.
Use the Playbook Simulator with your playbook
When you work with playbooks—whether you're using an existing one or creating a new one—always start by turning on the Playbook Simulator. You'll see a green indicator at the top confirming it's active.
If you use the Playbook Simulator on an active playbook, it does impact all incoming alerts that trigger that playbook. This is because saving a playbook with simulated data applies that data to live cases in production, which can potentially affect real-world results.
Hold your pointer over a case alert, click
more_vert
Alert Options
, and select
Ingest alert as test case
. This action creates a test case for running your simulated playbook on. Entities modified within test cases don't have any influence on entities in regular cases.
Hold your pointer towards bottom of the
Playbooks
page and select a test case. Make sure that the selected test case is a match for the playbook you intend to run. To confirm, click
Entities
and verify that the playbook is capable of processing the entities present within that test case.
Click
Run
. The simulator processes the steps, runs the defined actions,
    and provides the results.
Interpret simulator results for each step
After you click
Run
, the first row in the console displays as if
    it was a live playbook. Each simulated step presents options, typically including
Case Data
,
View Results
, and
Pin Results
(or
Insert Results
). Manual steps prompt a button to input parameters,
    provide responses, and execute the step.
Case Data
The
Case Data
icon opens a dialog to display the case's information at that specific stage—after the current action has finished running. This dialog dynamically updates with the current step's results. If an action added enrichment to the case, you'll see it reflected here. Because it shows the case's state after a step's execution, the data varies for each step in the simulation console. Inspecting the case data across different steps helps you understand the changes applied to the case during the playbook's execution. Multiple tabs within the dialog provide additional details.
View Results
The
View Results
option displays the specific action results of the current step. The information presented is similar to a case overview or case wall, and it also includes details on any enrichments.
You can access these types of information:
The main tab shows the output message, tables, links, and attachments.
The technical details tab provides the action result and the JSON result (if present).
Similar to other options, you can click through the data for a deeper inspection. On the
View Results
page, you can also  click
Set JSON result
. This feature lets you replace the JSON sample of the current action. You can modify this JSON sample directly from the Integrated Developer Environment (IDE) and then build on it within the Expression Builder to extract specific data from the JSON result.
Pin Results
The
Pin Results
option is available when a step runs successfully. This is a highly useful feature that lets you treat the outcome of an action as fixed.
Pinning results can save you time by:
Eliminating the need to wait for results from third-party services.
Reducing the number of queries made to these services, which helps conserve credentials.
Essentially, when you rerun the playbook, any step with pinned results is "passed over": its code doesn't execute again, and the pinned results are used as they are. You can also modify this outcome by inserting your own mock data. When you enable
Pin Results
, the action enters simulate mode, and the visual representation of the step typically changes from a blue-to-gray background, clearly indicating that
Simulate
mode is active for that step.
Insert Results
The
Insert Results
option becomes available if a step has failed. This feature lets you manually insert simulation data. The next time you run this specific step, it returns the data you've manually provided as its result.
Once you click this option, the action automatically has
Simulate
mode enabled. The step's visual representation changes from a blue-to-gray background, clearly indicating that
Simulate
mode is active. The
Script Result
field is required for all steps when in
Simulate
mode.
Insert mock data
To insert mock data, you have a few use cases to consider:
Building and testing your playbook on the go
: You can run a step, view the results, and immediately understand how you can use that data further along in your playbook.
Saving time after a successful run
: You might want to pin the step's results. This saves you time by preventing the step from running repeatedly against third-party APIs during subsequent tests.
Testing different scenarios
: You can change your step results to test your playbook under various conditions. By setting different simulation data, you can influence subsequent conditions and actions that rely on previous results. For example, if your playbook has a condition that branches into two or more paths, you can experiment with simulation data to "force" the playbook to take a specific branch.
Insert simulation data
You can insert simulation (mock) data into your playbook in two main ways: through the Playbook step configuration dialog or by using
Pin Results
(or
Insert Results
) after a simulator run.
Use the Playbook step configuration dialog
Click the step configuration dialog within your playbook.
Toggle the
Simulate mode
to enable it. The action's visual representation changes to gray, indicating it's in
Simulate mode
.
In the
Action results
section, you can insert your simulation (mock) data. This includes:
Script result: Provide a mock result for script-based actions.
JSON result: Enter JSON data, potentially by extracting specific data from JSON code. You can also load a sample output by clicking
Load Sample
. This loads the action's expected JSON result, which is particularly useful if:
The simulation hasn't run yet, and the output is empty.
The simulation failed, and no results are displayed.
You want to override existing results (from previous pinning or inserting) with the sample.
Enrichments: You can use enrichments from previous simulation runs or create your own custom enrichment keys.
Use results after a simulator run
Pin Results
If a step runs successfully, you can click
Pin Results
next to that action. The following occurs after:
The step automatically opens in
Simulate
mode
.
The results from the latest successful simulation run are pinned to the step. You can use these results or you can edit them.
You can edit the JSON result using the JSON editor or click
Load Sample
to override.
You can use enrichments from previous simulation runs or create custom enrichment keys.
Insert Results
If a step has failed, you can click
Insert Results
next to that action. The following occurs after:
This data will now be returned every time the step runs.
Turn off the Playbook Simulator
When you turn off the
Playbook Simulator
, it hides the bottom console,
  and any step in
Simulate mode
reverts to regular 'live' mode. The exception is
  the playbook blocks—you must turn off the block simulator to close its
  simulation mode for it. Any inserted simulation (mock) data is saved for use the
  next time you turn on the simulator.
Work with playbook blocks
You can also use the
Playbook Simulator
to build and test a new playbook block.
  When a block is in simulation mode, all parent playbooks using this block also use
  the block's mock data.
Need more help?
Get answers from Community members and Google SecOps professionals.
