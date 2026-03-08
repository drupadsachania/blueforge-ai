# Emerging Threats feed

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/emerging-threats-feed/  
**Scraped:** 2026-03-05T09:33:15.653923Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Emerging Threats feed
Supported in:
Google secops
SIEM
The
Emerging Threats
feed in Google Security Operations displays real-time
AI-informed threat intelligence from Google Threat Intelligence (GTI). It
helps you identify potential compromises in your environment by exposing active
and emerging threat campaigns most relevant to your organization.
This feed provides a curated view of campaigns and reports and their associated
threat actors and malware families. It lets you explore threat relationships and
investigate threat campaign details.
The reports displayed in the feed are restricted to those produced by GTI and
don't include crowdsourced reports visible in GTI itself.
Apply filters and view campaigns
You can filter the
Emerging Threats
feed to view the list of campaigns and
reports based on specific criteria.
To apply filters:
Click
filter_alt
Filter
in the
Emerging Threats
feed.
In the
Filters
dialog, select the logical operator:
OR
: Matches any of the selected filters.
AND
: Matches all the selected filters.
Select a filter category:
    *
Object types
: View either campaigns or reports depending on your
        investigation focus.
    *
Source regions
: Filter by the geographical region where the
        threat originated from.
    *
Targeted regions
: Filter by the targeted geographical region.
    *
Targeted industries
: Filter by industries targeted by the
        campaign.
    *
Has IoC matches
: View campaigns that contain IoCs matching your
  environment.
The selected filters appear as chips above the table.
Understand threat cards
Each threat in the feed appears as a card that contains the following:
Threat title and summary
: A brief description of the threat activity.
Associated metadata
: An overview of the targeted industries, targeted
regions, related malware, and threat actors.
Badges
: Quick indicators that display IoC matches and associated rules.
For campaigns and reports, the
IOCs
badge shows whether any IoCs in
the report or campaign match data from your environment.
For campaigns, the
Rules
badge shows the number of associated
detection rules that are enabled in your environment. For example, a
badge labeled
1/2 rules
indicates that only one out of the two
available rules for that campaign are enabled in your environment.
Hold the pointer over the badge to display the breakdown of the number of broad and
precise rules and whether they're enabled or disabled.
View associated actors and malware
To view associated actors and malware, click a threat card to reveal detailed
context about the threat, including:
Associated Actors
: Displays the
Actor Details
panel that includes sections for
actor name, summary, known source country, first and last seen dates, and
any related campaigns, malware, and indicators.
Associated Malware
: Displays the
Malware Details
panel that includes sections for
malware family, summary, operating system, reported aliases, and any related
campaigns, actors, or indicators.
In each panel, click
keyboard_arrow_down
next to a section name to expand it and view more details. Alternatively, you can
open these details directly in GTI to get more information.
Need more help?
Get answers from Community members and Google SecOps professionals.
