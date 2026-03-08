# Configure alert overflow

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/define-alert-overflow-admin/  
**Scraped:** 2026-03-05T09:34:35.800807Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure alert overflow
Supported in:
Google secops
SOAR
The alert overflow mechanism is designed to prevent system overflow and
  improve noise reduction when large volumes of alerts from the same
  environment, product, and rule occur in a short period of time. This 
  mechanism helps avoid repetitive attacks, such as brute force or DDoS, from flooding the
  platform and database, while making sure that the SOC continues
  to function as planned.
The alert grouping mechanism intelligently groups alerts into
  cases based on mutual entities and time proximity, letting analysts 
  perform a contextual analysis of multiple alerts in one case.
In these cases, you'll see multiple alerts in one case, and mutual entities
  marked in the entities list and the
Explorer
page.
Overflow configuration
There are two distinct configurations for the overflow mechanism:
Initial overflow configuration
: This configuration is hard-coded in
the database and defines the trigger conditions. The mechanism activates when more than 50 similar alerts are ingested within a 10-minute timeframe. This is determined by the
Is_Overflow
method, which is configured on the
connector side (added to the connector code in the Integrated Development Environment (IDE)). Once triggered, the system adds an overflow case to the case queue. This case contains one alert indicating the environment, product, and rule of the overflowing alert, along with an overflow tag.
Second overflow configuration
: This configuration defines the system's behavior
after
the overflow mechanism is triggered. You can define this
  in
SOAR Settings
>
Advanced
>
Alerts Grouping
in
  the
Overflow
section.
Timeframe for Overflow Case grouping (in hours):
Choose the number of
    hours in which to group the overflow alerts for the case. This is only
    applied to rules grouped solely by entities.
Max. alerts grouped into an Overflow Case:
Define the maximum number
    of overflow alerts to group together into one case.
For example, if 50 phishing alerts are ingested within 8 minutes, the 51st alert
    triggers the overflow mechanism, and an overflow case is created.
    Over the next three hours another 119 phishing alerts are ingested, resulting
    in four overflow cases, each containing 30 alerts. Once the
    three hours expire, the system returns to the default configuration.
Need more help?
Get answers from Community members and Google SecOps professionals.
