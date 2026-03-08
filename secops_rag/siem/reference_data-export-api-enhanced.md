# Data Export API (Enhanced)

**Source:** https://docs.cloud.google.com/chronicle/docs/reference/data-export-api-enhanced/  
**Scraped:** 2026-03-05T09:37:43.632618Z

---

Home
Documentation
Security
Google Security Operations
Reference
Stay organized with collections
Save and categorize content based on your preferences.
Data Export API (Enhanced)
Supported in:
Google secops
SIEM
The Data Export API facilitates the bulk export of your security data from
Google Security Operations to a Google Cloud Storage bucket that you control.
After you fulfill the
prerequisites
,
you can begin using the APIs.
The following sections describe the Chronicle Data Export API endpoints. The
API sample requests in these sections have the
{region}
set to
US
.
FetchServiceAccountForDataExports
Use this API endpoint to identify your Google SecOps instance's
unique Service Account.
For details, see
Method: dataExports.fetchServiceAccountForDataExport
Request
Endpoint
:
GET https://chronicle.{region}.rep.googleapis.com/v1alpha/{parent}/dataExports:fetchServiceAccountForDataExport
Path parameters
Field
Type
Required
Description
parent
string
required
The Google SecOps instance to export data from, specified in the following format:
projects/{project}/locations/{region}/instances/{instance}
where:
{project}
: Identifier of your project.
{region}
: Region where your destination bucket is located. See the list of
regions
.
{instance}
: Identifier of the source Google SecOps instance.
Request body
The request body must be empty.
Sample request
GET
h
tt
ps
:
//chronicle.us.rep.googleapis.com/v1alpha/projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/dataExports:fetchServiceAccountForDataExport
Sample response
The API returns the Service Account email.
{
"serviceAccountEmail"
:
"service-1234@gcp-sa-chronicle.iam.gserviceaccount.com"
}
Response parameters
Parameter
Type
Description
serviceAccountEmail
string
The Service Account email linked to your Google SecOps tenant.
CreateDataExport
Use this endpoint to create a specification for a bulk data export job. The system
stores the job specification on the
parent resource
— the
Google SecOps instance containing the source log data.
The API exports data using the First-In, First-Out (FIFO) principle,
independent of data size.
For details, see
Method: dataExports.create
Request
Endpoint
:
POST https://chronicle.{region}.rep.googleapis.com/v1alpha/{parent}/dataExports
Path parameters
Field
Type
Required
Description
parent
string
required
The Google SecOps instance to export data from, specified in the following format:
projects/{project}/locations/{region}/instances/{instance}
where:
{project}
: Identifier of your project.
{region}
: Region where your destination bucket is located. See the list of
regions
.
{instance}
: Identifier of the source Google SecOps instance.
Request body
Post a request to the endpoint using the following parameters.
Sample request
POST
h
tt
ps
:
//chronicle.us.rep.googleapis.com/v1alpha/
projec
ts
/myprojec
t
/loca
t
io
ns
/us/i
nstan
ces/aaaaaaaa
-
bbbb
-
cccc
-
dddd
-eeeeeeeeeeee
/da
ta
Expor
ts
{
"startTime"
:
"2025-08-01T00:00:00Z"
,
"endTime"
:
"2025-08-02T00:00:00Z"
,
"gcsBucket"
:
"projects/chronicle-test/buckets/dataexport-test-bucket"
,
"includeLogTypes"
:
[
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/logTypes/GCP_DNS"
,
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/logTypes/GCP_FIREWALL"
]
}
Body parameters
Field
Type
Required
Description
startTime
string
optional
The beginning of the event time range of the data to export, based on the event timestamp.
Format: String in
google.protobuf.Timestamp
format.
If you don't specify a time, it defaults to
01/01/1970 UTC
.
endTime
string
optional
The end of the event time range of the data to export.
Format: String in
google.protobuf.Timestamp
format.
If you don't specify a time, it defaults to the current time.
gcsBucket
string
required
The path to your Google Cloud Storage destination bucket, in the following format:
/projects/{project-id}/buckets/{bucket-name}
.
Note:
The destination bucket must be in the same region as the source Google SecOps tenant.
includeLogTypes
array
optional
A comma-separated array of one or more log types you want to
   export. If not specified, the system exports all log types by default.
Sample response
Upon successful creation of the data export job, the API returns a unique
name
for the data export job and the job's initial status, which is
IN_QUEUE
. The
response also includes an
estimatedVolume
of the data that the system expects to
export.
{
"name"
:
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/dataExports/b4a3c2d1-e8f7-6a5b-4c3d-2e1f0a9b8c7d"
,
"startTime"
:
"2025-08-01T00:00:00Z"
,
"endTime"
:
"2025-08-02T00:00:00Z"
,
"gcsBucket"
:
"projects/chronicle-test/buckets/dataexport-test-bucket"
,
"includeLogTypes"
:
[
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/logTypes/GCP_DNS"
,
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/logTypes/GCP_FIREWALL"
],
"dataExportStatus"
:
{
"stage"
:
"IN_QUEUE"
},
"estimatedVolume"
:
"10737418240"
,
"createTime"
:
"2025-08-13T11:00:00Z"
,
"updateTime"
:
"2025-08-13T11:00:00Z"
}
Response parameters
Parameter
Type
Description
name
string
Unique data export job ID.
The system extracts the
dataExportId
from the last section of the
name
parameter. Use this UUID in other calls to represent the data export request.
startTime
string
Starting time range.
Format: String in
google.protobuf.Timestamp
format.
endTime
string
Ending time range.
Format: String in
google.protobuf.Timestamp
format.
gcsBucket
string
The path to your Google Cloud Storage destination bucket, in the following format:
projects/{project-id}/buckets/{bucket-name}
.
includeLogTypes
list
A comma-separated list of log types included.
dataExportStatus.stage
string
The status of the export job at the time of creation (always
IN_QUEUE
).
estimatedVolume
string
The estimated export volume in bytes.
createTime
string
Job creation time.
Format: String in
google.protobuf.Timestamp
format.
updateTime
string
Job update time.
Format: String in
google.protobuf.Timestamp
format.
GetDataExport
Retrieve a specific data export job's current status and details, using its
dataExportId
.
Request
Endpoint:
GET https://chronicle.{region}.rep.googleapis.com/v1alpha/{name}
Path parameters
Field
Type
Required
Description
name
string
required
The name of the data export job to retrieve, in the following format:
projects/{project}/locations/{region}/instances/{instance}/dataexports/{dataExportId}
where:
{project}
: Identifier of your project.
{region}
: Region where your destination bucket is located. See the list of
regions
.
{instance}
: Identifier of the source Google SecOps instance.
{dataExportId}
: UUID of the data export job.
Request body
The request body must be empty.
Sample request
GET
h
tt
ps
:
//chronicle.us.rep.googleapis.com/v1alpha/
projec
ts
/myprojec
t
/loca
t
io
ns
/us/i
nstan
ces/aaaaaaaa
-
bbbb
-
cccc
-
dddd
-eeeeeeeeeeee
/da
ta
Expor
ts
/b
4
a
3
c
2
d
1-e8
f
7-6
a
5
b
-4
c
3
d
-2e1
f
0
a
9
b
8
c
7
d
Sample response
The response contains the full job details, including its current status. For completed jobs, the response also returns the actual volume of data successfully exported.
{
"name"
:
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/dataExports/b4a3c2d1-e8f7-6a5b-4c3d-2e1f0a9b8c7d"
,
"startTime"
:
"2025-08-01T00:00:00Z"
,
"endTime"
:
"2025-08-02T00:00:00Z"
,
"gcsBucket"
:
"projects/chronicle-test/buckets/dataexport-test-bucket"
,
"includeLogTypes"
:
[
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/logTypes/GCP_DNS"
,
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/logTypes/GCP_FIREWALL"
],
"dataExportStatus"
:
{
"stage"
:
"FINISHED_SUCCESS"
,
"exportedGlobPatterns"
:
[
"/bigstore/<bucket>/<dataexportid>/exported_paths.txt"
]
},
"estimatedVolume"
:
"10737418240"
,
"exportedVolume"
:
"10938428241"
,
"createTime"
:
"2025-08-13T11:00:00Z"
,
"updateTime"
:
"2025-08-13T11:05:00Z"
}
Response parameters
Parameter
Type
Description
name
string
Unique name for a data export job.
startTime
string
Starting time range.
endTime
string
Ending time range.
gcsBucket
string
The path to your Google Cloud Storage destination bucket, in the following format:
/projects/{project-id}/buckets/{bucket-name}
.
includeLogTypes
list
A comma-separated list of included log types.
dataExportStatus.stage
string
Current status of the data export job, which can have one of the following values:
IN_QUEUE
: The system has accepted the job and it's waiting for resources to become available.
PROCESSING
: The job is actively executing.
FINISHED_SUCCESS
: The job completed successfully. The response will include the final exportedVolume.
FINISHED_FAILURE
: The job failed after all retry attempts. The response will include detailed error information.
CANCELLED
: A user cancelled the job before it started processing.
(For more details, see the
DataExportStatus
reference.)
dataExportStatus.exportedGlobPatterns
list
File path of the exported text file, containing a list of all the exported file shards (exported glob patterns) created in the destination bucket.
estimatedVolume
string
The estimated export volume in bytes.
exportedVolume
string
For completed jobs, the actual volume of data exported.
createTime
string
Job creation time.
updateTime
string
Job update time.
ListDataExport
List data export jobs associated with a Google SecOps instance.
You can optionally filter the list to narrow results by the current job
status (
dataExportStatus.stage
), the data export job's
createTime
, and
the job
name
.
Request
Endpoint:
GET https://chronicle.{region}.rep.googleapis.com/v1alpha/{parent}/dataExports{?queryParameters}
Path parameters
Field
Type
Required
Description
parent
string
required
The Google SecOps instance for which to list data export requests, specified in the following format:
projects/{project}/locations/{region}/instances/{instance}
where:
{project}
: Identifier of your project.
{region}
: Region where your destination bucket is located. See the list of
regions
.
{instance}
: Identifier of the source Google SecOps instance.
Query parameters
Append optional query parameters to the request to add filters to narrow the results.
You must encode query parameters in a UTF-8 format.
Field
Type
Required
Description
pageSize
integer
optional
The maximum number of export jobs to return. The response may return fewer results. If you don't specify it, the API returns a list of 10 jobs by default. The API can return a maximum of 100 jobs in a single request.
pageToken
string
optional
A string value that the API returns in a paginated response, which you can use to retrieve the subsequent page.
filter
string
optional
You can apply the following filters to the list of jobs:
dataExportStatus.stage:{list of job stages}
:
A list of job status values, separated by the
OR
operator, to include in the request.
createTime >= {timestamp}
:
The start of the time range to include, based on
creationTime
.
createTime <= {timestamp}
:
The end of the time range to include, based on
creationTime
.
name = {list of names}
:
A list of job names, separated by the
OR
operator, to include in the request.
Example of query parameters in a UTF-8 encoded format
f
il
ter
=(da
ta
Expor
t
S
tatus
.s
ta
ge%
3
D%
22
FINISHED_SUCCESS%
22
%
20
OR%
20
da
ta
Expor
t
S
tatus
.s
ta
ge%
3
D%
22
CANCELLED%
22
)
%
20
AND%
20
crea
te
Time%
3E
%
3
D%
222025-08-29
T
00
%
3
A
00
%
3
A
00
Z%
22
%
20
AND%
20
crea
te
Time%
3
C%
3
D%
222025-09-09
T
00
%
3
A
00
%
3
A
00
Z%
22
%
20
AND%
20
na
me%
3
D%
22
projec
ts
%
2
F
140410331797
%
2
Floca
t
io
ns
%
2
Fus
%
2
Fi
nstan
ces%
2
Febdc
4
bb
9-878
b
-11e7-8455-10604
b
7
cb
5
c
1
%
2
Fda
ta
Expor
ts
%
2
Fed
3
f
735
d
-3347-439
a
-9161-1
d
474407e
ae
2
%
22
&
pageSize=
2
The example uses the following parameters:
Parameters
Description
filter=
This introduces filters.
(data_export_status.stage%3D%22FINISHED_SUCCESS%22%20OR%20data_export_status.stage%3D%22CANCELLED%22)
This creates a filter to only include jobs with the "dataExportStatus.stage" values as "FINISHED_SUCCESS" OR "CANCELLED".
%20AND%20
This acts as a separator to introduce another filter using the
AND
operator.
createTime%3E%3D%222025-08-29T00%3A00%3A00Z%22
This creates a filter for
createTime
to be greater than or equal to "2025-08-29T00:00:00Z".
createTime%3C%3D%222025-09-09T00%3A00%3A00Z%22
This creates a filter for
createTime
to be less than or equal to "2025-08-29T00:00:00Z".
name%3D%22projects%2F140410331797%2Flocations%2Fus%2Finstances%2Febdc4bb9-878b-11e7-8455-10604b7cb5c1%2FdataExports%2Fed3f735d-3347-439a-9161-1d474407eae2%22
This creates a filter to restrict results to the job name: "projects/140410331797/locations/us/instances/ebdc4bb9-878b-11e7-8455-10604b7cb5c1/dataExports/ed3f735d-3347-439a-9161-1d474407eae2".
&pageSize=2
This specifies the required page size.
Request body
The request body must be empty.
Sample request
Send a request using optional query parameters to add filters to narrow the results, for example, the current job status
dataExportStatus.stage
, the
createTime
of the data export job, and the job
name
.
GET
h
tt
ps
:
//chronicle.googleapis.com/v1alpha/
projec
ts
/myprojec
t
/loca
t
io
ns
/us/i
nstan
ces/aaaaaaaa
-
bbbb
-
cccc
-
dddd
-eeeeeeeeeeee
/da
ta
Expor
ts
?
f
il
ter
=(da
ta
Expor
t
S
tatus
.s
ta
ge%
3
D%
22
FINISHED_SUCCESS%
22
%
20
OR%
20
da
ta
Expor
t
S
tatus
.s
ta
ge%
3
D%
22
CANCELLED%
22
)%
20
AND%
20
crea
te
Time%
3E
%
3
D%
222025-08-29
T
00
%
3
A
00
%
3
A
00
Z%
22
%
20
AND%
20
crea
te
Time%
3
C%
3
D%
222025-09-09
T
00
%
3
A
00
%
3
A
00
Z%
22
%
20
AND%
20
na
me%
3
D%
22
projec
ts
%
2
F
140410331797
%
2
Floca
t
io
ns
%
2
Fus%
2
Fi
nstan
ces%
2
Febdc
4
bb
9-878
b
-11e7-8455-10604
b
7
cb
5
c
1
%
2
Fda
ta
Expor
ts
%
2
Fed
3
f
735
d
-3347-439
a
-9161-1
d
474407e
ae
2
%
22
&
pageSize=
2
Sample response
The response returns a paginated array of data export job objects that match the
filter criteria. Each object contains full job details and the current job
status. Completed jobs include the actual volume of data successfully exported.
{
"dataExports"
:
[
{
"name"
:
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/dataExports/b4a3c2d1-e8f7-6a5b-4c3d-2e1f0a9b8c7d"
,
"startTime"
:
"2025-08-01T00:00:00Z"
,
"endTime"
:
"2025-08-03T00:00:00Z"
,
"gcsBucket"
:
"projects/chronicle-test/buckets/dataexport-test-bucket"
,
"includeLogTypes"
:
[
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/logTypes/GCP_DNS"
,
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/logTypes/GCP_FIREWALL"
],
"dataExportStatus"
:
{
"stage"
:
"CANCELLED"
},
"estimatedVolume"
:
"10737418240"
,
"createTime"
:
"2025-08-01T11:00:00Z"
,
"updateTime"
:
"2025-08-13T11:10:00Z"
},
{
"name"
:
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/dataExports/f1e2d3c4-b5a6-7890-1234-567890abcdef"
,
"startTime"
:
"2025-08-03T00:00:00Z"
,
"endTime"
:
"2025-08-04T00:00:00Z"
,
"gcsBucket"
:
"projects/chronicle-test/buckets/dataexport-test-bucket"
,
"dataExportStatus"
:
{
"stage"
:
"FINISHED_SUCCESS"
,
"exportedGlobPatterns"
:
[
"/bigstore/<bucket>/<dataexportid>/exported_paths.txt"
]
},
"estimatedVolume"
:
"53687091200"
,
"exportedVolume"
:
"54687091205"
,
"createTime"
:
"2025-08-01T09:00:00Z"
,
"updateTime"
:
"2025-08-13T10:30:00Z"
}
],
"nextPageToken"
:
"aecg2S1w"
}
Response parameters
Parameter
Type
Description
dataExports
array
Array of data export job objects that match the specified filters:
name
: Unique data export job ID.
startTime
: Starting time range.
endTime
: Ending time range.
gcsBucket
:
The path to your Google Cloud Storage destination bucket, specified in the following format:
/projects/{project-id}/buckets/{bucket-name}
.
includeLogTypes
: A comma-separated list of included log types.
dataExportStatus.stage
: Current status of the data export job.
dataExportStatus.exportedGlobPatterns
:
File path of the exported text file, containing a list of all the exported file shards created in the destination bucket.
estimatedVolume
: The estimated export volume in bytes.
exportedVolume
: For completed jobs, the actual volume of data exported.
createTime
: Job creation time.
updateTime
: Job update time.
nextPageToken
string
A token (string) used to retrieve the subsequent page in a different request.
UpdateDataExport
You can only modify an existing job's parameters when it's in the
IN_QUEUE
status.
Request
Endpoint
:
PATCH https://chronicle.{region}.rep.googleapis.com/v1alpha/{parent}/dataExports/{dataExportId}
Path parameters
Field
Type
Required
Description
parent
string
required
The parent resource containing this data export specification, in the following format:
projects/{project}/locations/{region}/instances/{instance}
where:
{project}
: Identifier of your project.
{region}
: Region where your destination bucket is located. See the list of
regions
.
{instance}
: Identifier of the source Google SecOps instance.
dataExportId
string
required
The job UUID to update.
Request body
Send a
PATCH
request specifying the job's
name
.
Sample request
PATCH
h
tt
ps
:
//chronicle.us.rep.googleapis.com/v1alpha/
projec
ts
/myprojec
t
/loca
t
io
ns
/us/i
nstan
ces/aaaaaaaa
-
bbbb
-
cccc
-
dddd
-eeeeeeeeeeee
/da
ta
Expor
ts
/b
4
a
3
c
2
d
1-e8
f
7-6
a
5
b
-4
c
3
d
-2e1
f
0
a
9
b
8
c
7
d
{
"name"
:
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/dataExports/b4a3c2d1-e8f7-6a5b-4c3d-2e1f0a9b8c7d"
,
"endTime"
:
"2025-08-03T00:00:00Z"
,
"gcsBucket"
:
"projects/chronicle-test/buckets/dataexport-test-bucket2"
}
Body parameters
Field
Type
Required
Description
name
string
required
Unique name of the data export job to update, in the following format:
projects/{project}/locations/{region}/instances/{instance}/dataexports/{dataExportId}
where:
{project}
: Identifier of your project.
{region}
: Region where your destination bucket is located. See the list of
regions
.
{instance}
: Identifier of the source Google SecOps instance.
{dataExportId}
: UUID identifier of the data export job.
startTime
google.protobuf.
Timestamp
optional
The updated starting value of the time range for the export.
endTime
google.protobuf.
Timestamp
optional
The updated ending value of the time range for the export.
gcsBucket
string
optional
The updated path to your Google Cloud Storage destination bucket, in the following format:
/projects/{project-id}/buckets/{bucket-name}
.
Note:
You must create the bucket in the same region as your Google SecOps tenant.
includeLogTypes
array
optional
The updated, comma-separated list of one or more log types you want to
   export. If this field is included but the value is left blank, the system exports all log types by default.
Sample response
If the request is successful, the API returns a confirmation of the update.
The response contains the updated field values for the specified job name,
along with an updated estimate of the data volume for the export.
{
"name"
:
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/dataExports/b4a3c2d1-e8f7-6a5b-4c3d-2e1f0a9b8c7d"
,
"startTime"
:
"2025-08-01T00:00:00Z"
,
"endTime"
:
"2025-08-03T00:00:00Z"
,
"gcsBucket"
:
"projects/chronicle-test/buckets/dataexport-test-bucket2"
,
"includeLogTypes"
:
[
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/logTypes/GCP_DNS"
],
"dataExportStatus"
:
{
"stage"
:
"IN_QUEUE"
},
"estimatedVolume"
:
"15737418240"
,
"createTime"
:
"2025-08-13T12:00:00Z"
,
"updateTime"
:
"2025-08-13T12:05:00Z"
}
Response Parameters
Parameter
Type
Description
name
string
The unique name of the updated data export job.
startTime
string
The updated starting time range
endTime
string
The updated ending time range
gcsBucket
string
The updated path to your Google Cloud Storage destination bucket, in the following format:
/projects/{project-id}/buckets/{bucket-name}
.
includeLogTypes
list
The updated comma-separated list of included log types.
dataExportStatus.stage
string
The status of the export job at the time of update (always
IN_QUEUE
).
estimatedVolume
string
The updated estimated export volume in bytes.
createTime
string
The original job creation time.
updateTime
string
The job update time.
CancelDataExport
You can only cancel an existing job when it is in the
IN_QUEUE
status.
Reference Documentation:
Method: dataExports.cancel
Request
Endpoint
:
POST https://chronicle.{region}.rep.googleapis.com/v1alpha/{name}:cancel
Path parameters
Field
Type
Required
Description
name
string
required
The name of the data export job to cancel, in the following format:
projects/{project}/locations/{region}/instances/{instance}/dataexports/{id}
where:
{project}
: Identifier of your project.
{region}
: Region where your destination bucket is located. See the list of
regions
.
{instance}
: Identifier of the source Google SecOps instance.
{id}
: UUID identifier of the data export request.
Request body
The request body must be empty.
Sample request
POST
h
tt
ps
:
//chronicle.us.rep.googleapis.com/v1alpha/
projec
ts
/myprojec
t
/loca
t
io
ns
/us/i
nstan
ces/aaaaaaaa
-
bbbb
-
cccc
-
dddd
-eeeeeeeeeeee
/da
ta
Expor
ts
/b
4
a
3
c
2
d
1-e8
f
7-6
a
5
b
-4
c
3
d
-2e1
f
0
a
9
b
8
c
7
d
:
ca
n
cel
Sample response
A successful response shows the job's status as
CANCELLED
.
{
"name"
:
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/dataExports/b4a3c2d1-e8f7-6a5b-4c3d-2e1f0a9b8c7d"
,
"startTime"
:
"2025-08-01T00:00:00Z"
,
"endTime"
:
"2025-08-02T00:00:00Z"
,
"gcsBucket"
:
"projects/chronicle-test/buckets/dataexport-test-bucket"
,
"includeLogTypes"
:
[
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/logTypes/GCP_DNS"
,
"projects/myproject/locations/us/instances/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/logTypes/GCP_FIREWALL"
],
"dataExportStatus"
:
{
"stage"
:
"CANCELLED"
},
"estimatedVolume"
:
"10737418240"
,
"createTime"
:
"2025-08-13T11:00:00Z"
,
"updateTime"
:
"2025-08-13T11:10:00Z"
}
Need more help?
Get answers from Community members and Google SecOps professionals.
