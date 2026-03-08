# TemplateEngine

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace-and-integrations/power-ups/templateengine/  
**Scraped:** 2026-03-05T09:37:04.547167Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
TemplateEngine
Supported in:
Google secops
SOAR
The
TemplateEngine
uses Jinja2 to quickly and flexibly render templates. These templates can be used for things like entity insights, emails, ticketing systems, or any action that can take in a text string. Jinja2 documentation can be found at
https://jinja.palletsprojects.com/en/3.0.x/
.
Entity Insight
Description
The
Entity Insight
action creates entity insights from a JSON object using a Jinja2 template.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
JSON Object
JSON
N/A
Yes
Raw JSON object to use to render the template.
Template
Drop-down
SMRT Table CSS
No
Jinja2 Template to display. It can be a HTML template from
Settings
>
Environment
or added in the content box.
Triggered By
String
Siemplify
Yes
Name of the integration that triggered this entity insight.
Remove BRs
Checkbox
Unchecked
No
Decision to remove all <br> html tags from the
        rendered template.
Create Insight
Checkbox
Checked
No
Determine whether to create an entity insight.
Example
In this scenario, we're creating an insight using a JSON object which
  includes entity identifier and JSON results from a previous action.
Action Configurations
Parameter
Value
Entities
All entities
JSON Object
[{"Entity": "[Entity.Identifier]", "EntityResult":
[EmailUtilities_Analyze Headers_1.JsonResult]}]
Template
Email HTML Template
Editor
<style> summaryData {
flex-direction: row;
justify-content: center;
align-items: center;
width: 100%;}
summaryData th {
font-family: Open Sans;
font-style: normal; font-weight: bold; font-size: 11px;
color: black;
line-height: 108.95%; align-items: center;
background-color: #e8e8e8; height: 40px; min-width: 55px;
border-bottom: 1px solid;
text-align: left;
padding: 0 5px;}
.summaryData td {
font-family: Open Sans;
font-style: normal; font-size: 12px; line-height: 135%; align-items: center;
color: #4E4F63; margin: Opx 5px;
height: 40px; min-width: 55px;
border-bottom: 1px solid;
padding: 0 5px;}
summaryData tr:nth-child(odd) td{ background-color: #f7f7f7;}
Action Results
Script Result
Script Result Name
Value Options
Example
ScriptResult
true
or
false
true
JSON Result
{
"entity_insight" : "<div class="dmarc-compliance"> <table width="100%"> <col style="width:20%"><col style="width:80%"> <tr> <td><img title="compliant" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAPRJREFUeNqslMENgzAMRUPEAIzQEWCEHnsqdy4wAWWShgnaC3duPXYE2KCMwAbtt+RUkSnCrfoly8iJH45NiIxQcStSuBqWw5JgaYb1sLY7dGOYEwnAGe5ktuUAahYQAAa41Og1ApTRgw0q+AZASjnPRNyDQZk4wXYillluoqp8SoBVIl5bnoIGsEcP/ISmYC23Yoykq3jbG4Cj0967OFISyzNjc8XNJnckoAAsBkCNfcpKPCgY/yrAj3gWsRJJFy2A8mNuVPkBRL7ZAJB6qqRdWSTwQ/ERtpYvk1vZkCju0Pi/u0PigFMCnAcsfgW//k9eAgwAu4ZeSnNVcOkAAAAASUVORK5CYII=" width="17" /></td> <td>DMARC Compliant</td> </tr> <tr> <td><img title="spf_align" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAPRJREFUeNqslMENgzAMRUPEAIzQEWCEHnsqdy4wAWWShgnaC3duPXYE2KCMwAbtt+RUkSnCrfoly8iJH45NiIxQcStSuBqWw5JgaYb1sLY7dGOYEwnAGe5ktuUAahYQAAa41Og1ApTRgw0q+AZASjnPRNyDQZk4wXYillluoqp8SoBVIl5bnoIGsEcP/ISmYC23Yoykq3jbG4Cj0967OFISyzNjc8XNJnckoAAsBkCNfcpKPCgY/yrAj3gWsRJJFy2A8mNuVPkBRL7ZAJB6qqRdWSTwQ/ERtpYvk1vZkCju0Pi/u0PigFMCnAcsfgW//k9eAgwAu4ZeSnNVcOkAAAAASUVORK5CYII=" width="17" /></td> <td>SPF Alignment</td> </tr> <tr> <td><img title="spf_auth" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAP1JREFUeNqsVMERgjAQhIwFUAIv31ACT1+mBKkAUwmxA0uIL5+WAG9flkAHeudsZs4QBB125ua4XLJzt0eSJgHu+11BriHTZJlIDWSO7LS9XHt5Jg0IWnLHZB6WiMyIhAg6ckWyHD0RlfyhRAW/EDAKnEtSaNBFNj3I8i+xR6kgYoiak1yyLx1xHdnbKEwhrMBRvzyNiuzMHrFDXkJzO8+YaOKgF57HfYtpp6ZEI2uDtUnxp0i4EhOsGaHRBzb4E7NAk3craIErMIgrTFJOaVAQS4I3aKHBgT1iHRmzW+c/wWWykWQ+E/s71K93dxhYsAsJrCcYPQX/vicvAQYAFFNjwfmXVA0AAAAASUVORK5CYII=" width="17" /></td> <td>SPF Authenticated</td> </tr> <tr> <td><img title="spf_auth" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAPRJREFUeNqslMENgzAMRUPEAIzQEWCEHnsqdy4wAWWShgnaC3duPXYE2KCMwAbtt+RUkSnCrfoly8iJH45NiIxQcStSuBqWw5JgaYb1sLY7dGOYEwnAGe5ktuUAahYQAAa41Og1ApTRgw0q+AZASjnPRNyDQZk4wXYillluoqp8SoBVIl5bnoIGsEcP/ISmYC23Yoykq3jbG4Cj0967OFISyzNjc8XNJnckoAAsBkCNfcpKPCgY/yrAj3gWsRJJFy2A8mNuVPkBRL7ZAJB6qqRdWSTwQ/ERtpYvk1vZkCju0Pi/u0PigFMCnAcsfgW//k9eAgwAu4ZeSnNVcOkAAAAASUVORK5CYII=" width="17" /></td> <td>Strong SPF Record</td> </tr> <tr> <td><img title="dkim_align" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAP1JREFUeNqsVMERgjAQhIwFUAIv31ACT1+mBKkAUwmxA0uIL5+WAG9flkAHeudsZs4QBB125ua4XLJzt0eSJgHu+11BriHTZJlIDWSO7LS9XHt5Jg0IWnLHZB6WiMyIhAg6ckWyHD0RlfyhRAW/EDAKnEtSaNBFNj3I8i+xR6kgYoiak1yyLx1xHdnbKEwhrMBRvzyNiuzMHrFDXkJzO8+YaOKgF57HfYtpp6ZEI2uDtUnxp0i4EhOsGaHRBzb4E7NAk3craIErMIgrTFJOaVAQS4I3aKHBgT1iHRmzW+c/wWWykWQ+E/s71K93dxhYsAsJrCcYPQX/vicvAQYAFFNjwfmXVA0AAAAASUVORK5CYII=" width="17" /></td> <td>DKIM Alignment</td> </tr> <tr> <td><img title="dkim_align" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAP1JREFUeNqsVMERgjAQhIwFUAIv31ACT1+mBKkAUwmxA0uIL5+WAG9flkAHeudsZs4QBB125ua4XLJzt0eSJgHu+11BriHTZJlIDWSO7LS9XHt5Jg0IWnLHZB6WiMyIhAg6ckWyHD0RlfyhRAW/EDAKnEtSaNBFNj3I8i+xR6kgYoiak1yyLx1xHdnbKEwhrMBRvzyNiuzMHrFDXkJzO8+YaOKgF57HfYtpp6ZEI2uDtUnxp0i4EhOsGaHRBzb4E7NAk3craIErMIgrTFJOaVAQS4I3aKHBgT1iHRmzW+c/wWWykWQ+E/s71K93dxhYsAsJrCcYPQX/vicvAQYAFFNjwfmXVA0AAAAASUVORK5CYII=" width="17" /></td> <td>ARC Verify</td> </tr> </table> </div>",
"template" : "<div class="dmarc-compliance"> <table width="100%"> <col style="width:20%"><col style="width:80%"> <tr> <td><img title="compliant" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAP1JREFUeNqsVMERgjAQhIwFUAIv31ACT1+mBKkAUwmxA0uIL5+WAG9flkAHeudsZs4QBB125ua4XLJzt0eSJgHu+11BriHTZJlIDWSO7LS9XHt5Jg0IWnLHZB6WiMyIhAg6ckWyHD0RlfyhRAW/EDAKnEtSaNBFNj3I8i+xR6kgYoiak1yyLx1xHdnbKEwhrMBRvzyNiuzMHrFDXkJzO8+YaOKgF57HfYtpp6ZEI2uDtUnxp0i4EhOsGaHRBzb4E7NAk3craIErMIgrTFJOaVAQS4I3aKHBgT1iHRmzW+c/wWWykWQ+E/s71K93dxhYsAsJrCcYPQX/vicvAQYAFFNjwfmXVA0AAAAASUVORK5CYII=" width="17" /></td> <td>DMARC Compliant</td> </tr> <tr> <td><img title="spf_align" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAPRJREFUeNqslMENgzAMRUPEAIzQEWCEHnsqdy4wAWWShgnaC3duPXYE2KCMwAbtt+RUkSnCrfoly8iJH45NiIxQcStSuBqWw5JgaYb1sLY7dGOYEwnAGe5ktuUAahYQAAa41Og1ApTRgw0q+AZASjnPRNyDQZk4wXYillluoqp8SoBVIl5bnoIGsEcP/ISmYC23Yoykq3jbG4Cj0967OFISyzNjc8XNJnckoAAsBkCNfcpKPCgY/yrAj3gWsRJJFy2A8mNuVPkBRL7ZAJB6qqRdWSTwQ/ERtpYvk1vZkCju0Pi/u0PigFMCnAcsfgW//k9eAgwAu4ZeSnNVcOkAAAAASUVORK5CYII=" width="17" /></td> <td>SPF Alignment</td> </tr> <tr> <td><img title="spf_auth" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAP1JREFUeNqsVMERgjAQhIwFUAIv31ACT1+mBKkAUwmxA0uIL5+WAG9flkAHeudsZs4QBB125ua4XLJzt0eSJgHu+11BriHTZJlIDWSO7LS9XHt5Jg0IWnLHZB6WiMyIhAg6ckWyHD0RlfyhRAW/EDAKnEtSaNBFNj3I8i+xR6kgYoiak1yyLx1xHdnbKEwhrMBRvzyNiuzMHrFDXkJzO8+YaOKgF57HfYtpp6ZEI2uDtUnxp0i4EhOsGaHRBzb4E7NAk3craIErMIgrTFJOaVAQS4I3aKHBgT1iHRmzW+c/wWWykWQ+E/s71K93dxhYsAsJrCcYPQX/vicvAQYAFFNjwfmXVA0AAAAASUVORK5CYII=" width="17" /></td> <td>SPF Authenticated</td> </tr> <tr> <td><img title="spf_auth" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAP1JREFUeNqsVMERgjAQhIwFUAIv31ACT1+mBKkAUwmxA0uIL5+WAG9flkAHeudsZs4QBB125ua4XLJzt0eSJgHu+11BriHTZJlIDWSO7LS9XHt5Jg0IWnLHZB6WiMyIhAg6ckWyHD0RlfyhRAW/EDAKnEtSaNBFNj3I8i+xR6kgYoiak1yyLx1xHdnbKEwhrMBRvzyNiuzMHrFDXkJzO8+YaOKgF57HfYtpp6ZEI2uDtUnxp0i4EhOsGaHRBzb4E7NAk3craIErMIgrTFJOaVAQS4I3aKHBgT1iHRmzW+c/wWWykWQ+E/s71K93dxhYsAsJrCcYPQX/vicvAQYAFFNjwfmXVA0AAAAASUVORK5CYII=" width="17" /></td> <td>Strong SPF Record</td> </tr> <tr> <td><img title="dkim_align" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAP1JREFUeNqsVMERgjAQhIwFUAIv31ACT1+mBKkAUwmxA0uIL5+WAG9flkAHeudsZs4QBB125ua4XLJzt0eSJgHu+11BriHTZJlIDWSO7LS9XHt5Jg0IWnLHZB6WiMyIhAg6ckWyHD0RlfyhRAW/EDAKnEtSaNBFNj3I8i+xR6kgYoiak1yyLx1xHdnbKEwhrMBRvzyNiuzMHrFDXkJzO8+YaOKgF57HfYtpp6ZEI2uDtUnxp0i4EhOsGaHRBzb4E7NAk3craIErMIgrTFJOaVAQS4I3aKHBgT1iHRmzW+c/wWWykWQ+E/s71K93dxhYsAsJrCcYPQX/vicvAQYAFFNjwfmXVA0AAAAASUVORK5CYII=" width="17" /></td> <td>DKIM Alignment</td> </tr> <tr> <td> <img 
title="dkim_align" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAP1JREFUeNqsVMERgjAQhIwFUAIv31ACT1+mBKkAUwmxA0uIL5+WAG9flkAHeudsZs4QBB125ua4XLJzt0eSJgHu+11BriHTZJlIDWSO7LS9XHt5Jg0IWnLHZB6WiMyIhAg6ckWyHD0RlfyhRAW/EDAKnEtSaNBFNj3I8i+xR6kgYoiak1yyLx1xHdnbKEwhrMBRvzyNiuzMHrFDXkJzO8+YaOKgF57HfYtpp6ZEI2uDtUnxp0i4EhOsGaHRBzb4E7NAk3craIErMIgrTFJOaVAQS4I3aKHBgT1iHRmzW+c/wWWykWQ+E/s71K93dxhYsAsJrCcYPQX/vicvAQYAFFNjwfmXVA0AAAAASUVORK5CYII=" width="17" /></td> <td>ARC Verify</td> </tr> </table> </div>"
}
Render Template
Description
The
Render Template
renders a Jinja2 template using a JSON input.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
JSON Object
JSON
N/A
No
Raw JSON object to render the template. This value is available as the variable
input_json
in the Jinja template.
{"input_json": {"Entity" :
          "0.0.0.0"}}
Jinja
Drop-down
JSON
No
Jinja template code to render. This code overrides the
        template parameter. Append | safe to disable HTML encoding.
Include Case Data
Checkbox
Unchecked
No
If enabled, entity attributes and event data are available in the
        variables
input_json[“SiemplifyEntities”]
and
input_json[“SiemplifyEvents”]
.
Template
HTML
Email HTML Template
No
Jinja2 template to display. The template can be an HTML template from
>Settings
>
Environment
or added in the content box.
Example
In this scenario, we're passing a JSON result from VirusTotal from a
  previous action and returning an entity value.
Action Configurations
Parameter
Value
Entities
All entities
JSON object
[VirusTotalV3_Enrich IP_1.JsonResult]
Jinja
HTML
Editor
{% for i in input_json['results ']%}
Entity: {{i['Entity']}}
{% endfor %}
Include Case Data
Unchecked
Template
Email HTML Template
Action Results
Script Result
Script Result Name
Value Options
Example
ScriptResult
Output Result
Entity: 0.0.0.26
Render Template from Array
Description
Similar to a Render Template, but for lists. Loops through a list and applies the Jinja
      template to each list item.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Array Input
Array
[ ]
No
Point to output from a previous Action that outputs an Array.
[“10.10.10.10”]
Jinja
Drop-down
HTML
No
The Jinja template code to render. Will override Template
            parameters. Append | safe to disable HTML encoding.
Join
String
,
No
JOIN character between loops to join together.
Prefix
String
N/A
No
Prefix string before output.
Suffix
String
N/A
No
Suffix string after output.
Example
In this scenario, we're parsing a list of JSONs and returning IP
      addresses joined by a comma.
Action Configurations
Parameter
Value
Entities
All entities
Array input
[{"ip":"0.0.0.0", "ip":"0.0.0.1"}]
Jinja
HTML
Editor
{{row.ip}}
Join
,
Prefix
Blank
Suffix
Blank
Action Results
Script Result
Script Result Name
Value Options
Example
ScriptResult
Output Result
0.0.0.0,0.0.0.1
Need more help?
Get answers from Community members and Google SecOps professionals.
