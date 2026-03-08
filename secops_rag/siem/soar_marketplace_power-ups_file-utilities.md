# File utilities

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/file-utilities/  
**Scraped:** 2026-03-05T09:36:58.909050Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
File utilities
Supported in:
Google secops
SOAR
Overview
File Utilities is a set of file actions used to power up playbook
  capabilities.
Actions
Add Attachment
Description
Adds an attachment to the case wall.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Name
String
N/A
Yes
Specify the name of the attachment that will be visible in the case
        wall.
IsFavorite
Checkbox
Unchecked
No
Specify whether you want the attachment to be marked as favorite in the
        case wall.
Base64 Blob
String
N/A
Yes
Specify the attachment's Base64 blob. Use “Get Files as
        Base64 ”action to get the Base64 blob.
This action accepts a single Base64 blob. If you have multiple
        files, you must call this action for each file individually.
Type
String
N/A
Yes
Specify the extension of the file
Description
String
N/A
Yes
Specify description of the file.
Example
In this scenario, a Base64 blob is derived from a previous action and then is
  attached to the case wall. Once added to the wall, it can then be used for
  further analysis. This action is used alongside the “Get File as
  Base64” action, which generates the Base64 string of a file.
Action Configurations
Parameter
Value
Entities
All entities
Name
Malicious_EML
IsFavorite
Checked
Base64 Blob
[FileUtilities_Get Files as Base64_1.JsonResult | "data.base64"]
Type
[FileUtilities_Get Files as Base64_1.JsonResult | "data.extension"
Description
Malicious EML file from end user.
Action Results
Script Result
Script Result Name
Value options
Example
is_success
True/False
is_success:True
JSON Result
{
"evidenceName" : "Malicious_EML", 
"description " : "Malicious EML file from end user.", 
"evidenceThumbnailBase64" : "", 
"evidenceId" : 322, 
"fileType" : ".eml", 
"creatorUserId" : "Siemplify automation", 
"id " : 322, 
"type"  : 4, 
"caseId" : 51187, 
"isFavorite" : true, 
"modificationTimeUnixTimeInMs" : 1664206699128, 
"creationTimeUnixTimeInMs" : 1664206699128, 
"alertIdentifier" : null
}
Add Entity to File
Description
Adds an identifier of a target entity to a local file. It will only add one
occurrence of the entity to the file and will return False if the entity
already exists.
Important:
When you run this action in a SaaS environment, files are saved to
the temporary local storage of the Python execution pod. This storage is not
persistent and files may become inaccessible or deleted over time, especially in
large-scale deployments.
For reliable and persistent file storage, we strongly recommend running the
integration instance on a Remote Agent.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Filename
String
N/A
Yes
Specify the name of the file to write entities to. File will be stored
        in /tmp/ directory.
Example
In this scenario, suspicious hostname entity identifiers are added to a file
  called iocs_list.txt in /mnt/fileshare/ directory.
Action Configurations
Parameter
Value
Entities
Suspicious hostnames
Filename
/mnt/fileshare/ocs_list.txt
Action Results
Script Result
Script Result Name
Value options
Example
AddedAllEntities
True/False
True
Count Files
Description
Counts number of files in a given folder path according to a specific file
  extension.
Important:
When you run this action in a SaaS environment, files are saved to
the temporary local storage of the Python execution pod. This storage is not
persistent and files may become inaccessible or deleted over time, especially in
large-scale deployments.
For reliable and persistent file storage, we strongly recommend running the
integration instance on a Remote Agent.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
File Extension
String
*.txt
No
Specify the file extension to count by.
Folder
String
N/A
Yes
Specify the folder path which you would like to count the files.
Is Recursive
Checkbox
Unchecked
No
If enabled, this will recursively count all files in the directory.
Example
In this scenario, all files with .txt in /mnt/fileshare directory are counted.
Action Configurations
Parameter
Value
Entities
All entities
File Extension
*.txt
Folder
/mnt/fileshare/
Is Recursive
Checked
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Count Value
10
Create Archive
Description
Creates an archive file from a list of provided files or directory. Returns
  the location of the archive file.
Important:
When you run this action in a SaaS environment, files are saved to
the temporary local storage of the Python execution pod. This storage is not
persistent and files may become inaccessible or deleted over time, especially in
large-scale deployments.
For reliable and persistent file storage, we strongly recommend running the
integration instance on a Remote Agent.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Archive Type
String
N/A
Yes
Specify the type of archive to create. Supports: zip, tar, gztar, bztar,
        xtar.
Archive Base Name
String
N/A
Yes
Specify the name of the archive file that will be created without
        extension.
Archive Input
String
Unchecked
Yes
If enabled, this will recursively count all files in the directory.
Example
In this scenario, an archive zip file called archived_ioc_files is created
  containing multiple files in the /mnt/fileshares directory.
Action Configurations
Parameter
Value
Entities
All entities
Archive Type
zip
Archive Base Name
archived_ioc_files
Archive Input
/mnt/fileshares/ioc_list1,/mnt/fileshares/ioc_list2, /mnt/fileshares/ioc_list3
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
true
JSON Result
{
"archive" : 
"/opt/siemplify/siemplify_server/Scripting/FileUtilities/Archives/archived_ioc_files.zip",
"success" : true
}
Decode Base64
Description
Decodes Base64 input string and returns a json object with the content.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Base64 Input
String
N/A
Yes
Specify the Base64 input string you would like to decode.
Encoding
Dropdown
UTF-8
Yes
Specify the encoding format. UTF-8 or ASCII.
Example
In this scenario, a Base64 blob of a file is converted using UTF-8 to its
  original content.
Action Configurations
Parameter
Value
Entities
All entities
Base64 Input
(2FtcGxIIGZpbGUgY29udGFpbmluZyBzYW1qbGUgZGFOYQ==
Encoding
UTF-8
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
true
JSON Result
{
"decoded_content" : "<file content>"
}
Extract Archive
Description
Extracts an archive file to a directory.
Important:
When you run this action in a SaaS environment, files are saved to
the temporary local storage of the Python execution pod. This storage is not
persistent and files may become inaccessible or deleted over time, especially in
large-scale deployments.
For reliable and persistent file storage, we strongly recommend running the
integration instance on a Remote Agent.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Archive
String
N/A
Yes
Specify the path of the archive to be extracted. Supports: zip, tar,
        gztar, bztar, xtar. Destination path is:
        /opt/siemplify/siemplify_server/Scripting/FileUtilities/Extract
Example
In this scenario, files in ioc_lists.zip are extracted and saved in the
  /opt/siemplify/siemplify_server/Scripting/FileUtilities/Extract directory.
Action Configurations
Parameter
Value
Entities
All entities
Archive
/opt/siemplify/siemplify_server/Scripting/FileUtilities/Extract/ioc_lists
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
true
JSON Result
{"archives" :
    {0 :
        "success" : true,
        "archive" : "ioc_lists.tar",
        "folder" : "/opt/siemplify/siemplify_server/Scripting/FileUtilities/Extract/ioc_lists",
        "files_with_path" :{
                0 : "/opt/siemplify/siemplify_server/Scripting/FileUtilities/Extract/testarchive/Archives/ioc_lists.tar",
                1 : "/opt/siemplify/siemplify_server/Scripting/FileUtilities/Extract/ioc_lists/Archives/file1"
                           },
        
        "files_list" : {
                0 : "ioc_lists.tar",
                1 : "file1",
                2 : "file2"
                        },
        "files" :{
            "name" : "ioc_lists",
            "type" : "directory",
            "children" : {
                0 :{
                    "name" : "ioc_lists.tar",
                    "type" : "file"
                   },
                1 : {
                    "name" : "file1",
                    "type" : "file"
                    },
                2 : {
                    "name" : "file2",
                    "type" : "file"
                    }
                         }

    }
}
Extract Zip Files
Description
Extract files from a ZIP archive. It has the ability to extract password
  protected files by either a supplied password or brute force. It uses the
  attachment_id attribute of a file entity to pull the file from the case wall
  and extract it.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Include Data in JSON Result
Checkbox
Unchecked
No
Specify whether you want to include the extracted data as Base64 values
        in the json result.
Create Entities
Checkbox
Checked
No
Specify whether you want to create entities out of the extracted files.
Zip File Password
String
N/A
No
Specify the password of the zip file if it’s password protected.
Bruteforce Password
Checkbox
Unchecked
No
Specify whether you want to brute force the password protected zip file.
Add to Case Wall
Checkbox
Checked
No
Specify whether you want to add the extracted files to the case wall.
Zip Password List Delimiter
String
,
Yes
Specify the delimiter to use if multiple passwords are provided in the
        “Zip File Password” parameter.
Example
In this scenario, a password protected zip file entity is extracted and the
  resulting files are added to the case wall along with file entity creation.
Action Configurations
Parameter
Value
Include Data in JSON Result
Checked
Create Entities
Checked
Zip File Password
Password1
Bruteforce Password
Unchecked
Add to Case Wall
Checked
Zip Password List Delimiter
,
Action Results
Script Result
Script Result Name
Value options
Example
zip_files_extracted
True/False
true
Get Attachment
Description
Retrieves an attachment from the case wall and returns its Base64 value.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Attachment Scope
Dropdown
Alert
Yes
Specify the type of the attachment that needs to be retrieved. Options
        are: Case or Alert
Example
In this scenario, an attachment is pulled from the case wall and is converted
  to a Base64 blob.
Action Configurations
Parameter
Value
Entities
All entities
Attachment Scope
Alert
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Number of Attachments
1
JSON Result
{
"evidenceName": "myfile.txt", 
"description": "sample descriptions", 
"evidenceThumbnailBase64": "", 
"evidenceId": 475, 
"fileType": ".txt", 
"creatorUserId": "Siemplify automation", 
"id": 475, 
"type": 4, 
"caseId": 51209, 
"isFavorite": false, 
"modificationTimeUnixTimeInMs": 1664222678523, 
"creationTimeUnixTimeInMs": 1664222678523, 
"alertIdentifier": "COFENSE TRIAGE: INBOX REPORTCBEdfghB-B9E2-4A04fghAB-136A6fdghF0C6", 
"base64_blob": "dGhpcyBpcyB0ZXN0aW5nIHNhhdfhfpbmRlIHdpbmRvd3Mgc2hhcmdfghdfgUgddfghXNpbmcgc2llbXBsdfghaWZ5IGFndfghdfghdfghZW50"
}
Get Files as Base64
Description
Converts files in a directory to Base64 values.
Important:
When you run this action in a SaaS environment, files are saved to
the temporary local storage of the Python execution pod. This storage is not
persistent and files may become inaccessible or deleted over time, especially in
large-scale deployments.
For reliable and persistent file storage, we strongly recommend running the
integration instance on a Remote Agent.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
File Paths
String
N/A
Yes
Specify the file path(s) where the files are stored. Use comma delimiter
        if multiple paths are specified.
Example
In this scenario, a file called iocs_list.txt in /mnt/sharefiles directory is
  converted to a Base64 blob. This action is often used along with “Add
  Attachment” action, which takes the Base64 blob as an input and adds the
  file to the case wall.
Action Configurations
Parameter
Value
Entities
All entities
File Paths
/mnt/sharefiles/iocs_list.txt
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Number of Attachments
1
JSON Result
{
"Filenames" : {
     0 :  "/opt/siemplify/siemplify_server/Scripting/Phishing_.eml",
     1 :  "/opt/siemplify/siemplify_server/Scripting/Logo.png"
     },
"data" : {
     0 : {
          "path" : "/opt/siemplify/siemplify_server/Scripting",
          "filename" : "Phishing_.eml",
          "extension" : ".eml",
          "base64" : "asdfagdfgergert34523523452345dfg"  
     }
   }
}
Remove Entity from File
Description
Removes the identifier of a target entity from a local file. It will return
  False if it fails to remove all entities or if an entity doesn't exist.
Important:
When you run this action in a SaaS environment, files are saved to
the temporary local storage of the Python execution pod. This storage is not
persistent and files may become inaccessible or deleted over time, especially in
large-scale deployments.
For reliable and persistent file storage, we strongly recommend running the
integration instance on a Remote Agent.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
File Name
String
N/A
Yes
Specify the name of the file to remove entities from.
Example
In this scenario, internal hostname entity identifiers are removed from
  ioc_list.txt that is located in /tmp directory.
Action Configurations
Parameter
Value
Entities
Internal hostnames
Filename
ioc_list
Action Results
Script Result
Script Result Name
Value options
Example
RemovedAllEntities
True/False
True
Save Base64 to File
Description
Converts a Base64 string to a file. It supports comma separated lists for
  Filename and Base64 Input.
Default path:
/opt/siemplify/siemplify_server/Scripting/downloads/
FILE_NAME
Default path using an agent:
/opt/SiemplifyAgent/downloads/
FILE_NAME
Important:
When you run this action in a SaaS environment, files are saved to
the temporary local storage of the Python execution pod. This storage is not
persistent and files may become inaccessible or deleted over time, especially in
large-scale deployments.
For reliable and persistent file storage, we strongly recommend running the
integration instance on a Remote Agent.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
File Extension
String
N/A
No
Specify the file extension to add to the filename.
Base64 Input
String
N/A
Yes
Specify the Base64 string that will be converted to a file. Supports
        comma separation.
Filename
String
N/A
Yes
Specify the name of the file that will be created based on the Base64
        string.
Example
In this scenario, if the action is run on a Remote agent, a Base64 input string is saved to a
ioc_list
text file located in the
/opt/SiemplifyAgent/downloads
directory.
Action Configurations
Parameter
Value
Entities
Internal hostnames
File Extension
txt
Base64 Input
c2FtcGxIIGZpbGUgY29udGFpbsdfgsdfgmluZyBzYW1wbGUgZGF
OYQ==
Filename
ioc_list
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
true
JSON Result
{
"files": [
{"file_name": "ioc_list", 
"file_path": "/opt/SiemplifyAgent/downloads/ioc_list.txt", 
"extension": ".txt"}]
}
Need more help?
Get answers from Community members and Google SecOps professionals.
