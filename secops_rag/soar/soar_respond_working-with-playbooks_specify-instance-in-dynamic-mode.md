# Specify an instance in dynamic mode

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/specify-instance-in-dynamic-mode/  
**Scraped:** 2026-03-05T10:08:11.104066Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Specify an instance in dynamic mode
Supported in:
Google secops
SOAR
This document explains how to specify an instance name when selecting the
dynamic mode
option in a playbook step.
Dynamic Mode
is primarily used when building a playbook for multiple environments
(or all environments) for the playbook to dynamically select the instance
from the target environment at runtime.
The specify instance name field is used for when you define two or more
integration instances for each environment and want the playbook to select the
correct one automatically, without having to stop and wait for the analyst to manually choose.
Specify an instance name dynamically
When you create a playbook for multiple environments, select
Dynamic
Mode
in conjunction with
Specify instance name
so that you can
dynamically define which instance to use for each
action using free text or placeholders. You can use either placeholders, which let you
define the instance name a pattern, or use flow conditions, which let you define the 
conditions of when to use each instance.
You can also specify a default fallback instance to use if the named instance
can't be found.
There are three main ways of specifying the instance name to use in the dynamic mode:
Use placeholders in the specify instance name field
Use entity placeholders in the specify instance name field
Use the static instance name and the Flow condition step
Use case: Use placeholders in the specify instance name field
If your instance names follow a predictable pattern, you can use alert placeholders
to define which instance to use.  The following example uses the alert placeholder
in the
Specify instance name
field.
Two instances are defined under 
the Active Directory integration:
ActiveDirectory_UK
and
ActiveDirectory_US
.
The ingested alert contains a field called
location
. To
use this field, use the
[alert.location]
placeholder
in the
Specify instance name
field.
Use case: Use entity placeholders in the specify instance name field
To return the correct entity when using entity placeholders in the
Specify instance name
field, you need to use the
Siemplify Power Ups Tool Buffer
action. This action scopes the entity placeholder to ensure only one result is returned.
The following procedure shows how to set up retrieving the correct entity:
In the
Tools_Buffer
action
>
Entities
list, select 
the scope that you want to use (for example,
Destination users
).
In the
Result Value
field, insert the placeholder
[Entity.location]
. 
The result of this action will be the placeholder
[Entity.location]
scoped to destination users only.
In the next playbook step, for example,
VirusTotal_Enrich Hash
, 
select
Dynamic mode
and in the
Specify instance name
field, 
select
VirusTotal_[Tools_Buffer_1.ScriptResult]
from the placeholder options.
Use case: Use the static instance name and flow condition
If your instances' names don't follow a predictable pattern, you can still
dynamically select an instance based on parameters of your alert using the
Conditions
step.
The following example shows how to set up different conditional branches to return 
the correct instance to be used. The example uses the
Alert Rule Generator
condition 
and relies on two instances having been set up under the Email integration named
Email_1
and
Email_2
. Based on the condition result, the playbook will run on different branches and therefore choose the correct instance. So if the alert rule generator equals
Cloud Email
, the playbook will run on the first branch which uses the instance named
Email_1
. To set this up, do the following:
In the flow condition step, enter the following information:
If the alert rule generator equals
Cloud Email detection
:
Go to branch one.
In the initial step of branch one, select
Dynamic Mode
>
Specify Instance name
, and enter
Email_1
.
Click
Save
.
If the Alert Rule generator equals
on-premises Email
:
Go to branch two.
In the first step of branch two, select
Dynamic Mode
>
Specify Instance name
and enter
Email_2
.
Click
Save
.
Need more help?
Get answers from Community members and Google SecOps professionals.
