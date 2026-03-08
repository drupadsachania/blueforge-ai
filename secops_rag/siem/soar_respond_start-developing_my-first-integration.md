# Create your first custom integration

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-integration/  
**Scraped:** 2026-03-05T09:35:36.339637Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create your first custom integration
Supported in:
Google secops
SOAR
This document explains how to create a custom integration in the Integrated Development Environment (IDE) with the same structure as commercial integrations. Custom integrations appear in the Content Hub where you can configure them for different environments to use in playbooks, manual actions, and remote agents. You can also import and export them, like other IDE items.
In this custom integration example, you'll build a custom integration for the
WHOIS XML
  API
product. Start by creating your first integration
  including the registration process to the WHOIS product, including registering for the product and creating the required API key.
Choose the product to integrate with
In this example, you'll integrate with the
WHOIS XML API
product, a
    free open source tool that provides API access to domain data, including
    registrant name, organization, email address, registration address, registrar
    information, domain creation, expiration, and update dates, domain
    availability, and age.
Go to
WHOIS XML API/
and register.
After you sign in, get your API key from your account page:
https://user.whoisxmlapi.com/products
Use this API key in your integration parameters.
Create the first custom integration in the IDE
To create your first custom integration in the IDE, follow these steps:
On the
Response
>
IDE
page, click
add
Add
to add a new IDE item.
Select the
Integration
radio button and enter a name for the integration.
Click
Create
. The integration appears with a custom integration icon.
Click
settings
Settings
.
In the integration dialog, define the
Icon
,
Description
,
Python Dependencies
, and
Integration Parameters
.
In this example, the following details appear:
An image of the WhoisXML API logo is uploaded.  This image appears in the Content Hub with the integration.
An SVG icon has been added next to the integration in the IDE with a brief description and one parameter, the API Key. This is the parameter that the
Who Is XML API
Product requires for the configuration of the integration.
You don't need additional Python libraries for this integration. By default, the integration is set to run on Python 3.7, and you can change the version in
Settings
.
Configure the default instance
Once you create the integration, you can view it in your Google SecOps
    Response Integrations (search the integration name in the search bar or filter
    the Integration type by
Custom Integrations
) with the image,
    description and parameter you defined for the integration.
Click
settings
Settings
>
Configure a default Instance
.
Enter your API key and click
Save
.
Optional: To configure the integration for another environment (not the default environment), click the
Configure
tab and set parameters for that instance.
Create a Ping action
In
Response
>
IDE
, click
add
Add
>
Add New IDE Item
.
Select the
Action
radio button, enter a name, and
    select the integration.
Click
Create
. Review the generated code template.
Copy the following code for the
Ping
action. The
Ping
action uses the
API
    Key
parameter you configured for the integration and puts it in
    the URL provided by the product for testing purposes. For details, see
Create custom
    actions
.
from SiemplifyAction import SiemplifyAction
from SiemplifyUtils import output_handler
import requests

INTEGRATION_NAME = "My first Integration - Whois XML API"
SCRIPT_NAME = "Whois XML API Ping"

@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = SCRIPT_NAME

    api_key = siemplify.extract_configuration_param(provider_name=INTEGRATION_NAME,
                                                    param_name="API Key")
    url = "https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={api_key}&domainName=google.com".format(api_key=api_key)

    res = requests.get(url)
    res.raise_for_status()

    if "ApiKey authenticate failed" in res.content.decode("utf-8"):
        raise Exception("Error, bad credentials")

    siemplify.end("Successful Connection", True)
if __name__ == "__main__":
    main()
Click the toggle above the action and then
Save
to test the connection to the product.
Go to the
Google SecOps Marketplace
, click
settings
Configure default instance
, and make sure that
    the integration is configured and saved.
Click
Test
to test the integration. A successful connection displays a green checkmark; a failed connection displays an X with the associated error.
After you complete authentication, create your first custom action in the custom integration. For details, see
Create custom actions
.
Need more help?
Get answers from Community members and Google SecOps professionals.
