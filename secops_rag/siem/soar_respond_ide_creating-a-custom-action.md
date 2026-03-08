# Create a custom action

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/creating-a-custom-action/  
**Scraped:** 2026-03-05T09:35:31.626817Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create a custom action
Supported in:
Google secops
SOAR
In
Build a custom integration
, you created a Ping action for the Armis integration. This document outlines how to create a custom action for the Armis integration that enriches entities. It assumes you have a working knowledge of Python and object-oriented programming. For a prerequisite, refer to the SDK documentation and custom integration procedure, and explore the SDK modules.
Create a custom action
To create a custom action, follow these steps:
Go to
Response
>
IDE
; the
IDE
page appears.
Click
add
Create New Item
and select
Action
. Enter a name and select the integration.
Click
Create
. IDE creates a new template with code comments and explanations.
The Siemplify action object
A Siemplify action requires these steps:
An object must be instantiated from the
SiemplifyAction
class.
The object must use the class's
end
method to return an output message and a result value.
Result values
Every action has an
Output Name
that represents the result value returned by the SiemplifyAction's
end
method. By default, this is
is_success
, but you can change it in the Integrated Development Environment (IDE). You can also set a default
Return Value
for when an action fails.
 For example, if the action times out after five minutes (or fails for any other reason),
 the
ScriptResult
is set to
Timeout
.
JSON result value
You can also add a JSON result, which is useful for pivoting on data in
 playbooks or for manual analysis. To do this, use the
add_result_json
method on the
SiemplifyAction
result property or the
add_entity_json
method to attach a JSON result directly to an entity.
Imports and constants
The `SiemplifyAction` class from the `SiemplifyAction` module is always imported. Other common imports include:
output_handler
from
SiemplifyUtils
for debugging.
add_prefix_to_dict_keys
and
convert_dict_to_json_result_dict
for data transformation.
EntityTypes
to determine the type of entity an action will run on.
This action also reuses the `ArmisManager` created in the custom integration procedure and import the standard `json` library.
Need more help?
Get answers from Community members and Google SecOps professionals.
