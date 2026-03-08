# Image Utilities

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/image-utilities/  
**Scraped:** 2026-03-05T09:37:03.049974Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Image Utilities
A set of utility actions to assist with analyzing, extracting, and converting
image and file content during investigations. Key functions include optical
character recognition (OCR) for text extraction, rasterization (converting web
content to static images), and file format conversion. All actions require a
Remote Agent.
Actions
For more information about actions, see
Respond to pending actions from Your Workdesk
and
Perform a
manual action
.
Convert File
Use the
Convert File
action to change the format of a specified file.
Action inputs
The
Convert File
action requires the following parameters:
Parameter
Description
Input File Format
Required.
The original format of the file that the action converts.
The possible values are as follows:
PNG
PDF
The default value is
PNG
.
Input File Path
Required.
The path to the file that the action converts.
Output File Format
Required.
The resulting format of the file after the conversion process.
The possible values are as follows:
PNG
PDF
The default value is
PDF
.
Action outputs
The
Convert File
action provides the following outputs:
Action output type
Availability
Case wall attachment
Not available
Case wall link
Not available
Case wall table
Not available
Enrichment table
Not available
JSON result
Available
Output messages
Available
Script result
Available
JSON result
The following example shows the JSON result outputs received when using the
Convert File
action:
[
{
"output_format"
:
""
"file_path"
:
""
}
]
Output messages
The
Convert File
action can return the following output messages:
Output message
Message description
Successfully converted file.
The action succeeded.
Error executing action "Convert File". Reason:
ERROR_REASON
The action failed.
Check the connection to the server, input parameters, or credentials.
Script result
The following table lists the value for the script result output when using
the
Convert File
action:
Script result name
Value
is_success
true
or
false
OCR Image
Use the
OCR Image
action to perform OCR and
extract text from an image file.
Action inputs
The
OCR Image
action requires the following parameters:
Parameter
Description
Base64 Encoded Image
Optional.
The base64 encoded string of the image file.
File Path
Required.
The path to the image file.
Action outputs
The
OCR Image
action provides the following outputs:
Action output type
Availability
Case wall attachment
Not available
Case wall link
Not available
Case wall table
Not available
Enrichment table
Not available
JSON result
Available
Output messages
Available
Script result
Available
JSON result
The following example shows the JSON result outputs received when using the
OCR Image
action:
{
"extracted_text"
:
""
,
}
Output messages
The
OCR Image
action can return the following output messages:
Output message
Message description
Successfully performed OCR on the provided image.
The action succeeded.
Error executing action "OCR Image". Reason:
ERROR_REASON
The action failed.
Check the connection to the server, input parameters, or credentials.
Script result
The following table lists the value for the script result output when using
the
OCR Image
action:
Script result name
Value
is_success
true
or
false
Rasterize Content
Use the
Rasterize Content
action to convert vector or complex content into a
fixed, bitmap image format.
Remote Agent prerequisites (Debian)
To ensure the
Rasterize Content
action runs successfully on a Debian-based
Remote Agent, you must install the following packages and dependencies:
Playwright Python Library
Install the Playwright Python Library using the following command:
python3.11
-m
pip
install
playwright
Browser dependencies
Install the necessary Chromium browser dependencies for Playwright to function
correctly:
playwright
install
--with-deps
chromium
Action inputs
Parameter
Description
Input Type
Required.
The type of content that the action uses as its primary input.
The possible values are as follows:
URL
Email
HTML
The default value is
URL
.
URLs or Body
Required.
The input content to be rasterized, based on the selected
Input Type
.
If
URL
is selected, provide a comma-separated list of URLs.
If
Email
or
HTML
is selected, provide the full
    content body of that input type.
Output Type
Optional.
The resulting output format for the rasterized content.
The possible values are as follows:
PNG
PDF
Both
The default value is
PNG
.
Export Method
Optional.
The method used to output the generated content.
The possible values are as follows:
Case Attachment
File Path
Both
The default value is
Case Attachment
.
Width
Required.
The width (in pixels) used for the generated raster content.
The default value is
1920
.
Height
Required.
The height (in pixels) used for the generated raster content.
The default value is
1080
.
Full Screen
Optional.
If selected, the content is rendered across the entire browser window
    before being rasterized.
Disabled by default.
Timeout
Optional.
The maximum time (in seconds) the browser dedicates to rendering the
    content before rasterization begins.
The maximum value is
60
.
The default value is
120
.
Wait For
Optional.
The specific state the browser must reach before the action proceeds with
    rasterization or content extraction.
The
NETWORK_IDLE
state is generally the most reliable.
The possible values are as follows:
LOAD
DOM_CONTENT_LOADED
NETWORK_IDLE COMMIT
The default value is
NETWORK_IDLE
.
Wait for Selector
Optional.
A CSS selector that the action waits for to appear on the page before
    capturing the screenshot.
Action outputs
The
Rasterize Content
action provides the following outputs:
Action output type
Availability
Case wall attachment
Not available
Case wall link
Not available
Case wall table
Not available
Enrichment table
Not available
JSON result
Available
Output messages
Available
Script result
Available
JSON result
The following example shows the JSON result outputs received when using the
Rasterize Content
action:
[
{
"attachment_name"
:
""
,
"file_path"
:
""
}
]
Output messages
The
Rasterize Content
action can return the following output messages:
Output message
Message description
Successfully rasterized content based on the provided input.
Successfully rasterized content based on the following URLs:
URLS
Action wasn't able to rasterize content for the following URLs:
URLS
Action wasn't able to rasterize content for the provided URLs.
The action succeeded.
Error executing action "Rasterize Content". Reason:
ERROR_REASON
The action failed.
Check the connection to the server, input parameters, or credentials.
Script result
The following table lists the value for the script result output when using
the
Rasterize Content
action:
Script result name
Value
is_success
true
or
false
Need more help?
Get answers from Community members and Google SecOps professionals.
