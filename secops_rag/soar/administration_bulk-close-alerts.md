# Close alerts in bulk using the API

**Source:** https://docs.cloud.google.com/chronicle/docs/administration/bulk-close-alerts/  
**Scraped:** 2026-03-05T09:46:18.093813Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Close alerts in bulk using the API
Supported in:
Google secops
SIEM
This document describes how to programmatically close a large number of alerts using the Google Security Operations REST API. Google recommends using this method for situations where closing alerts in the platform would be too time-consuming.
Prerequisites
Before you start, make sure you have the following:
Python Environment:
You will need Python installed to run the sample scripts.
API Samples:
Access to the
api-samples-python
GitHub repository
.
Credentials:
A valid credentials file (for example
.chronicle_credentials.json
).
jq:
A command-line JSON processor used to parse the API output.
Search for Detections
First, you must identify the alerts (alerting detections) you want to close. You use the
list_detections.py
script to find detections associated with a specific Rule ID.
Locate your Rule ID and Project details.
Run the script to output the detections to a JSON file. The JSON filename can either be
detections.json
or
temp.json
.
Command:
python -m detect.v1alpha.list_detections \
  --project_id=$PROJECT_ID \
  --project_instance=$PROJECT_INSTANCE \
  --credentials_file=$CREDENTIALS_FILE \
  --rule_id=$RULE_ID \
  > ip_in_abuseipdb_out.json
Extract Detection IDs
The bulk update script requires a plain text file containing one detection ID per line. The previous step created a JSON file, which you must now convert to a text file.
Use
jq
to extract the detection IDs (which start with
de_
) from the JSON array.
Save the output to a text file.
Command:
cat ip_in_abuseipdb_out.json | jq -r '.detections[].id' \
  > ip_in_abuseipdb_out.txt
This creates a file listing IDs, for example
de_ad9d2771-a567...
..
Configure Feedback ("close" Action)
When you close an alert, the "feedback" status is set to
CLOSED
.
Default Behavior:
The
bulk_update_alerts.py
script uses a hard-coded default feedback payload:
Status:
CLOSED
Reason:
REASON_MAINTENANCE
Comment:
automated cleanup
.
Customization:
If you need to change the verdict (for example to
FALSE_POSITIVE
) or the comment, you can:
Directly edit the
DEFAULT_FEEDBACK
dictionary in the Python file.
Pass CLI parameters (e.g.,
--verdict="FALSE_POSITIVE"
) to override specific values.
Execute Bulk Close
Run the bulk update script using the text file you created before (See
Extract Detection IDs
). This script calls the
UpdateAlert
method for each ID in your list.
Command:
python -m detect.v1alpha.bulk_update_alerts \
  --project_id=$PROJECT_ID \
  --project_instance=$PROJECT_INSTANCE \
  --credentials_file=$CREDENTIALS_FILE \
  --alert_ids_file="$(pwd)/ip_in_abuseipdb_out.txt"
Verify Closure (Optional)
To verify the alerts were closed successfully, you can check the details of a single alert using the
get_alert.py
module.
Command:
python -m detect.v1alpha.get_alert \
  --project_id=$PROJECT_ID \
  --project_instance=$PROJECT_INSTANCE \
  --credentials_file=$CREDENTIALS_FILE \
  --alert_id=$ALERT_ID
Expected Result:
The JSON output contains a
feedbackSummary
object showing
"status": "CLOSED"
and your specified comment (for example "automated cleanup").
Need more help?
Get answers from Community members and Google SecOps professionals.
