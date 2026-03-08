# Work with Managed and Managed-Plus user groups

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/working-with-managed-plus-groups/  
**Scraped:** 2026-03-05T10:10:53.599284Z

---

Home
Documentation
Security
Google Security Operations
Stay organized with collections
Save and categorize content based on your preferences.
Work with Managed and Managed-Plus user groups
Supported in:
Google secops
SOAR
This document outlines the Managed and Managed-plus user groups, which are specifically designed for the end customers of a Managed Security Service Provider (MSSP). These user types offer a flexible level of platform access, acting as a hybrid between the collaborator and full user roles.
Explore the managed user types
This section defines the managed user types and how they offer a flexible level of platform access, acting as a hybrid between the collaborator and full user roles.
Managed user
The Managed user role is ideal for MSSPs who want to operate a hybrid SOC in collaboration with their customers. A Managed user has full case management capabilities within their own environment, similar to an MSSP analyst.
Managed-Plus user
A Managed-Plus user has all the same permissions as a Managed user, with the added ability to build and edit playbooks within their own environment.
Managed-Plus users can view playbooks running in their environment, including those configured for
All environments
playbooks. However, they can't edit playbooks if they don't have permissions for all environments associated with that playbook. For example, a user with permissions only for the "North England" environment would be able to view, but not edit, a playbook running across "North England," "South England," and "East England." Furthermore, this user wouldn't even see that the playbook is running on the "South England" and "East England" environments.
The MSSP is responsible for managing the Content Hub,
configuring integrations and agents, and customizing actions in the Integrated
Development Environment (IDE) for the Managed-plus user.
Create a Managed or Managed-Plus user group
The high-level steps to add a new managed or managed-plus user are the same as
that of adding other types of users:
Make sure you've purchased the Enterprise license, which gives you access
  to unlimited users.
Create a new Managed or Managed-Plus permissions group or use the
  predefined Managed or Managed-Plus group.
For more information, see
Work with permission groups
.
Need more help?
Get answers from Community members and Google SecOps professionals.
