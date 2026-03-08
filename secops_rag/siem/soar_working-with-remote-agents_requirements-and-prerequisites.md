# Remote Agent deployment requirements

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/requirements-and-prerequisites/  
**Scraped:** 2026-03-05T09:35:51.029601Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Remote Agent deployment requirements
Supported in:
Google secops
SOAR
This document outlines the technical and environmental requirements necessary
to deploy a Google Security Operations Remote Agent. The Remote Agent acts as a bridge,
letting your Google Security Operations platform communicate with security tools and
devices within your local environment.
Before you begin
Before proceeding with the installation, confirm that you meet the following prerequisites:
Email configuration (optional)
: Configure the email (SMTP/IMAP)
  integration in the Content Hub only if you require
  the installation package to be sent by email. If configured, use
Shared Instances
on the
Configure
page.
Server accessibility
: The Agent server must be accessible to both the Google SecOps Publisher and the target security tools within the corresponding environment.
Technical requirements
Review the following hardware and operating system requirements for the server hosting the Remote Agent:
Requirement
Basic deployment
Scaled-up deployment
CPU
4 cores
8 cores
RAM
8 GB
16 GB
Storage
100 GB
100 GB
Supported operating systems
Following are the prerequisites for the end customer server (for Remote Agent manual
  installation only):
Clean Centos 7.9
RHEL 8.7
Debian 12
Supported container engines
The Remote Agent supports the following container engines:
Podman
(recommended for all new installations)
Docker
Need more help?
Get answers from Community members and Google SecOps professionals.
