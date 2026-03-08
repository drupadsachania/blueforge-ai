# Manage environment load balancing

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/environment-load-balancing/  
**Scraped:** 2026-03-05T09:15:48.345713Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage environment load balancing
Supported in:
Google secops
SOAR
This document explains how you can use environment load balancing to help 
maintain platform stability and ensure fair resource distribution, especially in 
multi-tenant environments. It aims to prevent any single, heavy-loaded 
environment from consuming excessive system resources over a short period of 
time.
The system uses a lottery algorithm to randomly select environments for
resource allocation. Each active environment receives a number of tickets, and
the system randomly selects winning tickets to process tasks. By default, all
environments receive an equal number of tickets, but administrators can assign
higher weights to certain environments to prioritize them.
Configure environment load balancing
Once enabled, the system uses a lottery algorithm to allocate resources.
  Each active environment receives tickets. By default, all environments receive 
  an equal number of tickets. The system randomly selects winning tickets, and 
  the corresponding environments are granted access to system resources for task 
  processing.
This randomized approach ensures fair and balanced resource distribution 
  across all environments.
Basic configuration
You can enable or disable environment load balancing using the following legacy API endpoint:
POST /api/external/v1/settings/toggle-environment-load-balancing
Advanced configuration
The following APIs are used to manage the weights assigned to individual environments:
Chronicle API endpoints (recommended)
To reset the weights of all environments to their default:
POST /projects/{project}/locations/{location}/instances/{instance}/environments:resetWeights
To view the weights of all environments:
GET /projects/{project}/locations/{location}/instances/{instance}/environments
To view the weight of a specific environment:
GET /projects/{project}/locations/{location}/instances/{instance}/environments/{environment}
To set the weight of a specific environment, replace
{environment}
with the
environment_ID
, and adjust the
weight
value in the request body:
PATCH /projects/{project}/locations/{location}/instances/{instance}/environments/{environment}
Request Body example:
{
  "weight": 5
}
Legacy API endpoints (deprecated)
To reset the weights of all environments to their default (equal weight), use the following API:
POST /api/external/v1/settings/reset-environment-priorities
To view the weight of all environments, use the following API:
GET /api/external/v1/settings/environment-priorities
To view the weight of a specific environment, replace
{environment}
with the
environment_ID
, and use the following API:
GET /api/external/v1/settings/environment-priorities/{environment}
To set the weight of a specific environment, replace
{environment}
with the
environment_ID
, update the
weight
value in the request body, and use the following API:
PATCH /api/external/v1/settings/environment-priorities/{environment}
Request Body example:
{
  "weight": 3
}
Need more help?
Get answers from Community members and Google SecOps professionals.
