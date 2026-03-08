# Remote Agent scaling strategy

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/remote-agent-scaling-strategy/  
**Scraped:** 2026-03-05T10:09:02.996665Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Remote Agent scaling strategy
Supported in:
Google secops
SOAR
This document provides a detailed overview of the scalability of the
  Google Security Operations platform. It outlines the performance metrics for different
  agent configurations, demonstrating the Remote Agent framework's ability to handle high volumes
  of traffic with minimal infrastructure. The data presented reflects average
  results from a 10-minute end-to-end flow test.
Prerequisites
Connector or Action Execution Time (avg)
: 7-10 seconds
Connector or Action Result Size (avg)
: 500 KB-1 MB
Request
: An end-to-end flow of sending a request to the agent and
    getting the response back into Google SecOps.
A single request equals a single action execution or a single connector run.
Basic agent
The basic agent consists of 4 cores, 8 GB RAM, and 100 GB storage.
Actions Rate
: 96 actions per minute
Connectors Rate
: 96 runs per minute
For example, 16 connectors, each connector runs every 10 seconds and returns a result.
Combined Rate
: 96 requests per minute
For example, 60 actions + 6 connectors, each connector runs every 10 seconds and returns a result.
Scaled up agent
The scaled up agent consists of 8 cores, 16 GB RAM, and 100 GB storage.
Actions Rate
: 144 actions per minute (completed full run)
Connectors Rate
: 144 runs per minute
For example, 24 connectors, each connector runs every 10 seconds and returns a result.
Combined Rate
: 144 requests per minute
For example, 90 actions + 9 connectors, each connector runs every 10 seconds and returns a result.
Need more help?
Get answers from Community members and Google SecOps professionals.
