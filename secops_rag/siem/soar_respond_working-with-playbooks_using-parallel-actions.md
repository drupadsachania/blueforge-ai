# Use parallel actions

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-parallel-actions/  
**Scraped:** 2026-03-05T09:35:17.510891Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use parallel actions
Supported in:
Google secops
SOAR
When you use parallel actions, it speeds up playbook execution by querying 
multiple products or running long actions at the same time. This reduces the 
wait time for enrichment information, letting analysts start an investigation 
sooner. Additionally, grouping parallel actions logically helps organize the playbook.
Before you begin, consider these guidelines:
You can't put a condition or a block in a parallel action.
You can't use actions that have been set to
manual
.
The parallel actions in each group run randomly in any order. This means you
    can't use placeholders of actions in the same group of parallel actions.
You can choose to have individual Skip actions if a step failed for an
    individual action, within a group of parallel actions.
Double-click the top of a group of parallel actions to change the name to
    help logically arrange the parallel action boxes in your playbook.
Increase the playbook's speed
To speed up the playbook, you can choose to run up to five actions at
  once.
Create a parallel action (option 1)
Drag an action from the
Step
selection on top of another existing
    action in the playbook.
Drop it on top of the action. It automatically displays one on top of the
    other in a Parallel Action container.
Create a parallel action (option 2)
Press and hold the
Shift
key to highlight an action. You can highlight up to
    five actions at a time using
Shift
+
click
. Alternatively, you can
    simultaneously highlight several actions by pressing and holding
Shift
+ mouse
    to draw a rectangle around them.
Right-click any of the actions and choose
Run in Parallel
.
Create a parallel action (option 3)
Group two parallel actions together in a box, as
    you created in the previous two options.
Right-click a separate action and click
Cut
.
Place your cursor in the
Parallel Action
box and click
Paste
to add the action to the other parallel actions.
Delete one or more parallel actions (option 4)
Highlight one of the parallel actions in the box.
Right-click and select
Delete step
to delete the highlighted parallel action,
    or select
Delete all steps
to delete the entire group of parallel
    actions.
Need more help?
Get answers from Community members and Google SecOps professionals.
