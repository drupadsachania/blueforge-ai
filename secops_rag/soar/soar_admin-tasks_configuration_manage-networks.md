# Manage networks

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/manage-networks/  
**Scraped:** 2026-03-05T09:46:40.044985Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage networks
Supported in:
Google secops
SOAR
You can add, modify, and delete networks in the platform using the Classless
  Inter-Domain Routing (CIDR) format. The system identifies network subnets
  to help Google Security Operations recognize internal assets and consider
  network sensitivity during playbook execution.
Network management and display
For readability, network names appear in
Cases
and
Reports
.
An entity with a set IP address appears as an
Internal Entity
on the
Cases
page and has the
isInternal:True
field.
Manage multiple networks
To manage multiple networks, you have two options:
Use the
Export
and
Import
functions.
Download a template, add your network information to it, and then import it. This is particularly helpful for new customers who want to quickly add existing data to the platform.
Add a new network
To add a new network, follow these steps:
Go to
Settings
>
Environments
>
Networks
.
Click
add
Add
.
In the
New Network
dialog, add the relevant information. The
Priority
function
    determines the order of the networks. If an entity matches several ranges, the system selects the one with the highest priority.
Click
Add
.
Need more help?
Get answers from Community members and Google SecOps professionals.
