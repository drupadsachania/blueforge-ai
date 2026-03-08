# GitSync

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/gitsync/  
**Scraped:** 2026-03-05T09:37:01.872902Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
GitSync
Supported in:
Google secops
SOAR
GitSync is a robust integration built by Google SecOps Professional Services team and designed to synchronize Google SecOps components with a git repository. It uses git's internal operations to write directly to the repository itself, essentially making it act as a file storage service. It provides methods to perform the following:
Migrate Assets between Google SecOps instances
Backup Google SecOps assets
Automatic Documentation
Creates a "store" to share assets/knowledge
Version Control
Use cases
The integration consists of multiple Google SecOps jobs - push and pull jobs for every supported asset, and push/pull jobs for the entire Google SecOps instance. These jobs don't need to run periodically as they were built to run manually from the IDE, but they can be used as regular jobs (For example, uploading a daily commit).
GitSync uses the Chronicle API to fetch the relevant asset, such as an integration or a visual family, and parse all the available information from that asset (This information will later be rendered to a README.md file that is usually displayed when browsing the repository). It then writes the asset JSON definition and the rendered README to the local repository and pushes it to the remote repository.
Another usage of GitSync is knowledge sharing. Using this integration, a git repository can act as a "store" for assets such as playbooks or ontology settings that were designed before and leverages Google SecOps best practices to push the platform to its best.
Security Update: Host Fingerprint Pinning (GitSync V42.0)
A security enhancement has been released in GitSync V42.0 to protect against
person-in-the-middle (PITM) attacks by adding support for host fingerprint
pinning. This feature ensures the
GitSync
integration connects only to your
verified Git server.
Need to Know and Action Required
The
Host Fingerprint
field is optional and your existing jobs will continue to
run without disruption. However, we strongly recommend that you configure this
feature immediately to enhance your integration's security.
The host fingerprint is a unique ID for your Git server. The new feature
verifies this unique fingerprint upon connection, preventing attackers from
impersonating your server and intercepting data.
Enable Host Fingerprint Pinning
To enavle host fingerprint pinning, you must obtain your Git server's
fingerprint and add it to the integration configuration.
Find your Host Fingerprint
: You can get your Git server's public key
fingerprint from its documentation or by using a trusted method. To get the
fingerprint using the
ssh-keyscan
command, run the following command in your
terminal:
ssh-keyscan
-t
rsa
<hostname>
For example, for GitHub, run
ssh-keyscan -t rsa github.com
. The output
contains the host fingerprint, which looks similar to this:
github.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC...
Add the Fingerprint to the Integration
:
Add the copied fingerprint to the
Host Fingerprint
field in your
GitSync
integration's configuration settings.
Prerequisites
Pushing/Pulling an existing repository:
Authentication method to Git. Supported is a Username/Password combination (not recommended), an access token (recommended), and a base64 encoded SSH private key (recommended). When using the latter two, the username parameter is not required.
A local Google SecOps user. Used to import assets. This user must have permission to write the target module (For example, a user without access to the IDE wouldn't be able to pull integrations).
Create a new repository
All of the points mentioned in the Pushing/Pulling an existing repository earlier.
A remote repository. It is recommended to have at least 1 file in the repository. Most Git services give an option to create a README file when creating the repository.
Configure the integration
You must configure the integration as a Shared Instance. It can't be 
connected to an existing environment in Google SecOps SOAR.
Integration Properties
Param Name
Description
Repo URL
Repository URL. When using user/password authentication, this value must start with https://. If using SSH authentication, this value must start with git@ or ssh://. (See Configuring Repo URL and Branch below).
Branch
The branch in the repository to sync with.
Git Password/Token/SSH Key
Authentication method to git. This value can be Git Password/Token/SSH Private Key. Private keys should be encoded to base64. RSA and Ed25519 are supported.
Git Username
Git username. This value is not mandatory when using SSH authentication.
Commit Author
Not mandatory. Gives the ability to specify the author of the commit. This value must be in this format: Username
Google SecOps Verify SSL
Verify SSL to Google SecOps API
Git Verify SSL
Verify SSL with the target git service
Configuring Repo URL and Branch
In this guide, we will demonstrate getting the right values in Bitbucket (note that the process is the same in GitHub.)
Locate the repository in Bitbucket.
Click the clone button at the top right corner (Code in GitHub)
SSH Authentication - The repository URL is git@bitbucket.org:siemplifyproserv/connectors.git
User/Pass or Token Authentication - The repository URL is https://bitbucket.org/siemplifyproserv/connectors.git . (Username can be ignored)
Check the current branch (master in the image below)
Example Usage
Every Job in GitSync contains the following parameters:
Name
Description
Job-specific - Connector name, Integration Identifier, playbook allowlist, etc.
These parameters are for specifying what gets pushed or pulled to the repository. In GitSync, assets are referred to by their identifiers. These values are case-sensitive.
Repo URL and Branch
Add support for multiple repositories with the same credentials. Once these parameters are set, the repository configured in the integration instance will be ignored.
Commit Message
When pushing assets to the repository, a message is required for the commit. Here you can specify the reason for pushing, indicating what was fixed, changed or added to the asset.
Readme Addon
Adds the ability to extend the documentation of the assets when pushed. In this value you can use:
Markdown Syntax - Supported in README files by Git providers like GitHub and Bitbucket
Jinja - To display information about the asset. See examples in the integration manager constants
The template is added to the end of the documentation and is saved in the metadata file GitSync.json at the root of the repository.
Pulling Assets
In this example, we'll pull a connector with the correct mappings and visual families.
First, ensure the asset is located in the configured repository. Simply browse the repository directories and copy the asset identifier (Usually it's the directory name or the title of the README file).
Example from a repository in Bitbucket, In the Connectors directory. Note that directories are the integration names, and inside them are the real identifiers for the connectors.
Find the suitable job in Google SecOps IDE. In this example, we'll use the job Pull Connector.
Note: When pulling a connector, verify that the integration of the connector is installed as well.
Click the testing tab and configure the parameters. Since we're using one repository and it's already configured in the integration instance, we'll leave the Repo URL and Branch parameters empty, and set the other parameters to the values we need.
Run the job.
See Debug Output for the log of the operation. If everything goes well, the log will indicate it.
Go to Google SecOps -> Connectors and configure the connector.
Pushing Assets
In this example, we'll push a playbook and a block to the repository.
Identify the playbooks you want to push. Here we'll push a new block called Failed Login and an updated playbook called Malicious Activity.
Find the suitable job in Google SecOps IDE. In this example, we'll use the job Push Playbook.
Click the testing tab and configure the parameters.
Since both are in the same folder (Default), You can also use Folder Allowlist instead.
Run the job.
See Debug Output for the log of the operation. If everything goes well, the log will indicate it.
Validate that the repository contains the latest versions of the playbooks.
Creating a new repository
To create a new repository, only one thing is important, and that is including a single file in the repository before configuring it with GitSync. It can be done quickly by including a README file in the root of the repository when creating the repository.
Bitbucket
GitHub
Known issues and limitations
After the repository is set for the first time, It uses a predefined directory structure to ensure that it knows where each asset is located. Failing to follow the directory structure with a custom commit or changes to the repository, the integration will malfunction. You can find the schema of the repository directory structure at the end of this document.
Be careful when using this integration with public repositories. Google SecOps assets use parameters that hold Application IDs, Client ID, Usernames, and other sensitive information. GitSync can't tell if the parameter is sensitive or not, so every parameter that is not of type "Password" will be uploaded to the repository. Also, when pushing a Google SecOps instance (Push Environment job) there's an option to Commit Passwords. This option tells GitSync to try and export all the password parameters from the integration configuration. Don't set this value to true if the repository is public, or all the credentials will be leaked online.
When pulling a Google SecOps instance (Pull Environment job), installing all the integrations might take more than 5 minutes, and the job will fail with a timeout. It is recommended to manually install all the commercial integration from the Google Security Operations Marketplace beforehand to avoid any issue, But it is also possible to re-run the job if it fails with a timeout.
Commercial integrations and custom integrations are handled differently. Custom integration will be pushed as the entire zip export of the integration, for an import/export operation. Commercial integrations will be pushed with only the custom code. Once pulled, GitSync will install the latest version of the integration from the Google SecOps Marketplace, and save the custom code in the official integration.
When pulling mappings, they won't appear in the Settings -> Ontology -> Ontology Status table until the events have actually been ingested into Google SecOps, because they are not indexed yet.
The local repository is saved in /opt/siemplify/siemplify_server/GitSyncFiles/{RepoName}. Since the integration writes Git objects and not files, this folder doesn't represent the repository and is overwritten with any changes made anytime a job is executed. It is advised to use another clone of the repository, and not the one created by GitSync.
Playbooks with restricted permissions (for example, default permissions set to
Can View
) require specific permission configuration on the source system for successful synchronization through GitSync. For more information, see
Work with playbook permissions
.
Google SecOps supports using GitSync to back up SOAR assets. However,Google SecOps doesn't support using GitSync to *distribute* SOAR assets between systems. This can lead to unexpected results because the database objects might not be unique.
Work with playbook permissions
When using GitSync to synchronize playbooks with restricted permissions (for 
example, default permissions set to
Can View
, or other non-default 
settings), you might encounter an error on the destination system if it lacks 
authorization to modify the playbook. This happens because GitSync uses an 
internal System API key with the
Administrator
SOC role to perform 
actions. To ensure successful synchronization of playbooks with restricted 
permissions, grant the
Administrator
SOC role
Can 
Edit
permissions on the source system for those playbooks.
Enable GitSync to pull playbooks with restricted permissions
On the source system:
Go to the playbook you intend to synchronize with GitSync.
Open the playbook's permissions settings.
Ensure that the
Administrator
SOC role
is added to the list of entities with
Can Edit
permissions.
After adjusting the permissions on the source system, execute the
Push 
  Playbook
action in GitSync to update the Git repository with the playbook 
  and its permissions.
On the destination system, execute the
Pull Playbook
action in 
  GitSync.
Create SSH Keys to use with GitSync
First, generate a key pair. When asked for a passphrase, hit enter:
ssh-keygen -b 2048 -t rsa -f ./id_rsa
Two files will be created, id_rsa (private key) and id_rsa.pub (public key). Keep the private key in a safe location.
Set the public key in the repository. For example, in Bitbucket, enter the settings of the repository and click on Access Keys. Click on Add Key and paste the contents of id_rsa.pub in the Key parameter.
Before the private key can be added to the integration configuration, it should be encoded to Base64.
Use these commands to encode the file:
Linux:
cat id_rsa | base64 -w 0
Windows:
Open PowerShell where id_rsa is located and paste (This is one line):
Write-Output [System.Text.Encoding]::ASCII.GetString([convert]::ToBase64String(([IO.File]::ReadAllBytes((Join-Path (pwd) 'id_rsa')))))
Copy the printed value to the integration property Password/Token/SSH Key and test the integration connectivity.
GitSync repository Directory Structure
The following is the expected directory structure in the remote repository.
* This is a tree command output for an example repository. Comments are in red.
Need more help?
Get answers from Community members and Google SecOps professionals.
