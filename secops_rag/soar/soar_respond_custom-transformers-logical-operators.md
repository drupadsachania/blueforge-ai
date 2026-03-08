# Custom transformation functions and logical operators

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/custom-transformers-logical-operators/  
**Scraped:** 2026-03-05T10:08:32.702443Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Custom transformation functions and logical operators
Supported in:
Google secops
SOAR
You can create custom Python-based transformation functions and logical
operators directly within the IDE and use them in your playbooks for complex and
versatile use cases.
Extension Packs
An
extension pack
is a specialized integration type designed to act as
a container for custom transformation functions and logical operators. Unlike
standard integrations, extension packs don't require instance configuration and
can be created directly from the IDE.
Best practices for extension packs
Consolidation:
Create one main extension pack and add multiple
    transformation functions or logical operators to it.
Separation:
Create a new extension pack when you need a different
    set of Python libraries (dependencies) that might conflict with the main
    pack.
Create an Extension Pack
To create a new extension pack, follow these steps:
Go to
Response
>
IDE
.
Click
add
Create New Item
.
Select
Extension Pack
from the drop-down.
Provide a unique
Name
for the Extension Pack.
Click
Save
.
Upload dependencies
Like standard integrations, extension packs run in a virtual environment
where you can manage Python libraries.
To manage your libraries, follow these steps:
Open the
Extension Pack settings
in the IDE.
Add required Python libraries from PyPi or upload them from your
    computer.
These dependencies are available to all transformers and logical
operators contained within this specific extension pack.
Import and Export
You can manually import and export extension packs directly within the IDE
interface.
Custom Transformers
Custom Transformers
are user-defined Python functions that extend the
prebuilt functions in the
Expression Builder
. You can create them
directly within the IDE to extract and manipulate data, and they can be used
alongside existing built-in functions.
Create a custom transformer
To define a new custom transformer, follow these steps:
In the
IDE
, locate your target extension pack.
Select the target extension pack to add a new item under the pack.
Select
Custom Transformation Function
.
Give it a name.
Optional: Add a description. This is displayed when you hover over the
    custom transformer in the Expression Builder.
Define the script logic using Python. You can use the provided default
    template as a starting point.
The script must include a
main
function as shown in
            the
predefined template
.
The script must return a result to the expression builder by
            using the SDK
end
function.
The input of the custom transformer can be in different types
            (for example, string or list). Ensure you convert it to the expected
            type in your
main
function.
You can use only a subset of the SDK methods within the IDE for
            transformers:
transformer.extract_param("ParamName")
: To
                    retrieve input values.
transformer.LOGGER
: To write logs for
                    debugging.
transformer.end(result)
: To return the
                    transformed value.
Create parameters:
Each custom transformer function includes a default
Input
parameter. This parameter represents the input data, which is the
            placeholder the function applies to. You cannot delete this
            parameter.
Additionally, you can add optional parameters to be used within
            your function.
Documentation (Optional): Define in-product documentation for the
    Expression Builder:
Expected Input:
Describe the data type the function 
            expects to receive for this transformer (for example, "String" or 
            "List of strings").
Expected Output:
Describe the data type the function 
            expects to return for this transformer (for example, "boolean").
Usage Example:
Provide an example of how to invoke the
            function (for example,
if_empty("new_value")
).
You can test your custom transformation function logic directly within the 
IDE before using it in a playbook. This lets you verify that your Python script 
handles various input types and parameters correctly and returns the expected 
results.
Timeout
Default Timeout:
1 minute.
Maximum Timeout:
3 minutes.
Use custom transformers in the Expression Builder
Once saved, custom transformers appear in the Expression Builder's function
list alongside built-in functions. They are identified by the format:
ExtensionPackName.TransformerName
. Hovering over the function
displays the documentation generated from your parameter descriptions.
Support for all placeholders (JSON and non-JSON)
The Expression Builder supports every placeholder exposed in the Playbook
Designer, including non-JSON results.
For non-JSON placeholders:
You can manually enter sample data into the Expression Builder to test
    logic against various input types: string, list (comma-separated values),
    and JSON.
Testing with an input type does not guarantee the placeholder will
    return that specific type at runtime.
Most placeholders resolve as strings, except for specific types that
    resolve as a string or list based on their quantity (for example,
entity.identifier
). For these, it's recommended to always treat
    the input as a list.
Error Handling
If a custom transformation function encounters an error during execution, the 
playbook action that uses that transformer fails. The specific error message 
generated by the Python script is displayed on the screen within the 
playbook run view, allowing you to troubleshoot the logic directly.
Custom Logical Operators
Custom Logical Operators
let you define your own boolean logic for
comparing values.
Create a custom logical operator
To define a new logical operator, follow these steps:
In the
IDE
, locate your target
Extension Pack
.
Select
Custom Logical Operator
.
Give it a name.
Optional: Add a description for the logical operators menu in the
    Playbook Designer.
Define the script logic using Python. You can use the provided
    predefined template as a starting point.
The script must include a
main
function.
The script must return a boolean result to the condition by 
            using the SDK
end
function.
You can use only a subset of the SDK methods within the IDE for
            logical operators:
logical_operator.extract_param("ParamName")
: To 
                retrieve input values.
logical_operator.LOGGER
: To write logs for 
                debugging.
logical_operator.end(result)
: Result is a 
                boolean value (
true
or
false
).
You can test your custom logical operator logic directly within the IDE. This
lets you input test values for the arguments and verify that the function
returns the correct boolean (True or False) result based on your defined
conditions.
Parameters
Custom logical operators accept two parameters:
Left Side
(mandatory
and not editable) and
Right Side
(optional; can be disabled by the user).
Example 1:
if [left side] not in [right side]
.
Example 2:
if [left side] is greater than 80
(no
    right side).
Timeout
Default Timeout:
1 minute.
Maximum Timeout:
3 minutes.
Use in playbooks
Custom logical operators appear in the operator menu within
Playbook
Conditions
,
Previous Action Conditions
, and
Entity Selection
.
Custom logical operators are selectable alongside standard operators (for
example, "Equals" or "Contains").
Error Handling
If a custom logical operator function encounters an error during execution,
the playbook condition or step using that operator will fail. The error message
returned by the Python script is displayed within the playbook run view to
assist with troubleshooting.
Limitations
Custom transformation functions and logical operators are not supported
    in
Triggers
or
Webhooks
.
Need more help?
Get answers from Community members and Google SecOps professionals.
