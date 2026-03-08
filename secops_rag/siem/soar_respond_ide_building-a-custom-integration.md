# Build a custom integration

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/building-a-custom-integration/  
**Scraped:** 2026-03-05T09:35:32.720110Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Build a custom integration
Supported in:
Google secops
SOAR
This document explains how to create custom integrations inside the Integrated Development
  Environment (IDE) using the same structure as commercial integrations. You can find and configure custom integrations in the Content Hub for various environments. You can then use them in playbooks, manual actions, and remote agents. Import and export capability
  is also supported, similar to other IDE items.
Create a custom integration in the IDE
You can build a custom integration for the Armis product and
create a manager along with a
Ping
action. Knowledge of Python and
object-oriented programming is assumed for this procedure.
Use case: Build a custom Armis integration
To create the custom integration in the IDE, follow these steps:
In the main menu, go to
Response
>
IDE
.
Click
add
Create New Item
and select
Integration
.
Enter a name and click
Create
.
The integration is now listed with the
settings
Settings
option, indicating it's a custom integration.
Click
settings
Settings
to display the integration settings where you can define
the icon, description, Python dependencies, and integration parameters.
If a dependency package doesn't have a pre-compiled wheel (
.WHL
) 
  file available for the
manylinux_2_17_x86_64
architecture, or if 
  you need a specific source code version, you can provide a direct URL to the 
  source code (for example, a
.tar.gz
file). The platform's 
  dependency resolver,
uv
, supports defining these source URLs in 
  the
[tool.uv.sources]
table within your
pyproject.toml
file. For example:
[project]
# ... other project fields ...
[tool.uv.sources]
# The key (e.g., compressed-rtf) must match the dependency name
compressed-rtf
=
{
url
=
"https://files.pythonhosted.org/packages/.../compressed_rtf-1.0.6.tar.gz"
}
dkimpy
=
{
url
=
"https://files.pythonhosted.org/packages/.../dkimpy-1.1.8.tar.gz"
}
For more details on defining different types of dependencies using
uv
, see the
uv
documentation on
Managing dependencies
.
Create a custom manager
Managers are wrappers for third-party tool APIs. Although not mandatory,
we recommend them for integrations that interact with external tools. Managers
shouldn't import from the SDK. After creation, import them into connectors,
actions, and jobs.
To create a custom manager, follow these steps:
In the IDE, click
add
Create New Item
and select
Manager
.
Select the
Armis
integration and enter a manager's name.
Edit and run the following script:
import requests

class ArmisManager:
   def init(self, api_root, api_token):
       self.api_root = api_root
       self.api_token - api_token
       self.session = requests.session()
       self.session.headers = {"Accept": "application/json"}

   def auth(self):
       endpoint = "{}/api/vi/access_token/*"
       params = {"secret_key" : self.api_token}
       response = self.session.post(endpoint.format(self.api_root), params=params)
       self.validate_response(response)
       access_token = response.json()["data"]["access_token"]
       self.session.headers.update({"Authorization": access_token})
       return True

   def get_device_by_ip(self, device_ip):
       endpoint = "{}/api/vi/devices/"
       params = {"ip": device_ip}
       response = self.session.get(endpoint.format(self.api_root), params=params)
       self.validate_response(response)
       return response.json()["data"]["data"]

   @staticmethod
   def validate_response(res, error_msg="An error occurred"):
       """Validate a response

       :param res: (requests. Response) The response to validate
       :param error_msg: (str) The error message to display
       """
       try:
           res.raise_for_status()
       except requests.HTTPError as error:
           raise Exception("(error_msg): (error) (text)".format(
               error_msg=error_msg,
               error=error,
               text=error.response.content
           ))
Parameters, Google SecOps Content Hub configuration, and the Ping action
Parameters defined in the integration settings appear in the Google SecOps Content Hub configuration. The parameters include:
API Root
: The base URL for the service you're connecting to.
API Secret
: A confidential key used to authenticate your application with the service.
Verify SSL
checkbox: If enabled, verifies that the SSL certificate for the connection to the Armis server is valid.
Run Remotely
checkbox: A setting that determines whether the code or task will be executed on a remote server instead of locally. When this option is enabled, the system sends the necessary instructions and data to a dedicated server for processing.
To update the parameters, follow these steps:
Enter the correct credentials.
Click
Save
>
Test
.
If the
Ping
action is missing, the
Test
button fails and displays a red
X
.
Implement a Ping action
The logic of the
Ping
action acts like a successful
 authentication.
To implement a
Ping
action, do the following:
In the IDE, create a new
Action
in the Armis integration named
Ping
.
Use the
ArmisManager
auth
method to verify authentication.
Enable the integration
To enable the integration, follow these steps:
In
Response
>
IDE
, click the
Enable/Disable
toggle to the
ON
position.
Click
Save
. A green toggle confirms success. Credentials from the Content Hub are passed to ArmisManager. If
auth
completes without errors, the
Test
button shows a green checkmark.
Use the
extract_configuration_param
method to import parameters from the integration configuration. Alternatively, use
extract_action_param
to define parameters within the action itself. However, the
Ping
action should always use configuration parameters, as those are tested by the Content Hub.
View custom integrations
Go to the Content Hub and search for the custom
 integration you created.
 If you didn't create an image during the initial configuration, the
 default custom image will be assigned to it. Note that
 Content Hub updates
 don't override or delete any custom integrations.
Export and import in the IDE
Do one of the following actions:
To
import
integrations, do the following:
Upload a ZIP file with the correct folder structure; the
 integration appears in the IDE and the Content Hub.
Click
Import
. The integration appears in both the IDE and the Content Hub.
The system generates a ZIP file containing the definition, scripts, and configuration. The
Managers
folder is not included automatically.
To
export
integrations, do the following:
Click
Export
to download the package.
Need more help?
Get answers from Community members and Google SecOps professionals.
