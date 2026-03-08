# Configure forwarders in the Google SecOps platform

**Source:** https://docs.cloud.google.com/chronicle/docs/install/forwarder-management-configurations/  
**Scraped:** 2026-03-05T09:47:11.253440Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure forwarders in the Google SecOps platform
Supported in:
Google secops
SIEM
This page describes how to create, manage, and download forwarder configurations
using the Google SecOps user interface (UI).
Forwarder configuration is a two-step process:
Add forwarder configuration: This establishes the framework for your configuration.
Add collector configuration: This defines the source of data that the forwarder will ingest. Without at least one collector, the forwarder does not have any data to work with.
Once you've added one or more collectors, the forwarder configuration is complete. You can then download it and deploy it onto a machine or device that has the forwarder software installed.
For information about how to install and configure the Google SecOps forwarder,
system requirements, and details about configuration settings, see
Install and configure the forwarder
.
Add forwarder configuration
Instead of
adding
a new forwarder, you can
clone
one or more existing
forwarders. For details, see
Clone forwarders
.
To add a new forwarder, follow these steps:
In the navigation bar, click
Settings
.
Under
Settings
, click
Forwarders
.
Click
Add new forwarder
.
In the
Forwarder name
field, type a name.
Optional: Expand the
Configuration values
section and specify the values. For information about the configuration settings, see
Determine the configuration
.
Click
Submit
.
The forwarder is added and
Add collector configuration
window appears.
Add collector configuration
You can add one or more collectors to an existing forwarder. To add a new collector to a forwarder, follow these steps:
In the navigation bar, click
Settings
.
Under Settings, click
Forwarders
.
On the
Forwarders
page, find the forwarder you want. If the list of
forwarders is long, use the
Search
field.
Hold the pointer over the forwarder for which you want to add a collector. The
more_vert
expand menu icon
displays.
Click the
more_vert
expand menu icon
.
Select
Add new collector
.
In the
Collector name
field, type a name.
Click the
Log type
field to view a list of log types, and do one of
the following:
If you don't see the log type you want, start typing its name in the
box to view more suggestions. For a complete list of supported log types,
see
Supported data sets
.
Select a log type from the list.
Optional: Expand the
Configuration values
section and specify the values. For information about the configuration settings, see
Determine the configuration
.
Optional: Expand the
Advanced settings
section and specify any of
the following:
Max seconds per batch:
The number of seconds between batches. The
default is
10
.
Max bytes per batch:
The number of bytes queued before the forwarder
batch upload. The minimum is
204800 bytes
, which is
200 KB
. 
The maximum is
1048576 bytes
, which is
1MB
. The default is
1,048,576 bytes
, which is
1MB
.
Recommended:
Disk buffer:
Click the toggle to the on position to enable disk
buffering for the collector. For details about disk buffering,
see
Disk buffering
.
When enabled, you can specify the following settings:
Directory path:
The directory path for files written.
Maximum Buffered File Size (in bytes):
The maximum disk size used by the collector
before backlogged messages are buffered to disk. The default is
1,073,741,824
.
The maximum is
4,294,967,296
.
Optional:
Override timezone
: Click the toggle to the on position to override 
the default time zone for your logs by selecting a custom one from the
Timezone
list. 
only if your raw logs don't include the correct time zone at the source. Ensure
that the logs have consistent timestamps before enabling it.
The selected time zone is applied on the server side in
Google SecOps. The forwarder ignores this setting, even if the
generated configuration file contains it.
Click the
Collector type
field and select a collector type. Each
collector type has its own settings that you can configure. For details
about the collector types and their settings, see
Determine the configuration
.
Click
Submit
.
Download configuration files
Downloading the forwarder configuration files requires at least one collector. If you try to download a forwarder without a collector, you get an error.
You can download the forwarder configuration (
.conf
) file, authentication (
_auth.conf
) file, or both, for any forwarder listed in your Google SecOps instance as long as it has at least one collector. After downloading the files, deploy them on the Windows or Linux system where the Google SecOps forwarder resides.
To download forwarder configuration files:
In the navigation bar, click
Settings
.
Under Settings, click
Forwarders
. The page displays the list of forwarders.
On the
Forwarders
page, find the forwarder you want. If the list of
forwarders is long, use the
Search
field.
Hold the pointer over the forwarder for which you want to download configuration files. The
more_vert
expand menu icon
displays.
Click the
more_vert
expand menu icon
.
Select
Download
.
In the
Download forwarder configuration
dialog, do one of the following:
To download the forwarder configuration file, click the
download icon
next to the
.conf
file type.
To download the forwarder authentication file, click the
download icon
next to the
_auth.conf
file type.
To download both files, click
Download all
.
Manage forwarders
This section describes how to view and manage forwarders.
List the forwarders in a Google SecOps instance
In the navigation bar, click
Settings
.
Under Settings, click
Forwarders
. The page displays the list of forwarders.
Optional: Sort the list by clicking the
Name
or
Last updated
column.
Optionally, use the search field to narrow the results in your list.
Clone forwarders
Cloning lets you create a copy of one or more forwarder configurations.
To clone a forwarder configuration, follow these steps:
On the Forwarders page, select the checkbox for each forwarder that you want to clone.
Click the
more_vert
expand menu icon
.
Select
Clone
.
Click
Clone
. A copy of each forwarder configuration is added.
Edit a forwarder configuration
In the navigation bar, click
Settings
.
Under Settings, click
Forwarders
. The page displays the list of forwarders.
Hold the pointer over the forwarder for which you want to edit the configuration. The
more_vert
expand menu icon
displays.
Click the
more_vert
expand menu icon
.
Select
Edit forwarder configuration
.
Make your changes to the configuration. For more information, see the configuration steps in the procedure for
adding forwarders
.
Click
Update
Restart the forwarder for your changes to take effect.
Delete forwarders
On the Forwarders page, select the checkbox for each forwarder that you want to delete.
Click the
more_vert
expand menu icon
.
Select
Delete
.
In the Delete Forwarder dialog, click
Delete
.
Manage collectors
This section describes how to view and manage collectors.
List the collectors in a Google SecOps instance
In the navigation bar, click
Settings
.
Under Settings, click
Forwarders
. The page displays the list of forwarders.
Click the expander arrow next to the
Name
column heading. This expands all of the forwarders, displaying up to five collectors for each forwarder.
If a forwarder has more than five collectors, click the
See all collectors
link.
Edit a collector configuration
In the navigation bar, click
Settings
.
Under Settings, click
Forwarders
. The page displays the list of forwarders.
Click the
arrow_right
expander arrow of the forwarder for which you want to edit a collector.
If there are more than five collectors, click the
See all collectors
link.
Hold the pointer over the collector for which you want to edit the configuration. The
Edit
option displays.
Click
Edit
.
Make your changes to the configuration. For more information, see the configuration steps in the procedure for
adding collectors
.
Click
Update
.
Delete a collector
In the navigation bar, click
Settings
.
Under Settings, click
Forwarders
. The page displays the list of forwarders.
Click the
arrow_right
expander arrow
of the forwarder for which you want to delete a collector.
If there are more than five collectors, click the
See all collectors
link.
Hold the pointer over the collector for which you want to edit the configuration. The
Delete
option displays.
Click
Delete
.
To confirm, click
Delete
in the Delete collector dialog.
Need more help?
Get answers from Community members and Google SecOps professionals.
