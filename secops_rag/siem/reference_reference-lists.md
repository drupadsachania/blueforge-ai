# Reference Lists

**Source:** https://docs.cloud.google.com/chronicle/docs/reference/reference-lists/  
**Scraped:** 2026-03-05T09:32:47.786201Z

---

Home
Documentation
Security
Google Security Operations
Reference
Stay organized with collections
Save and categorize content based on your preferences.
Reference Lists
Supported in:
Google secops
SIEM
A reference list is a generic list of values which can be used to analyze your
data. For more information on reference lists, see the following:
Use reference lists in UDM search
Reference List Syntax in YARA-L 2.0
Reference List API
Configuring list type
The behavior of a list depends on the
list type
, which must be configured
at list creation time. See the sections below for an explanation of the list
types. List type can be changed as long as the following restrictions are met:
The list must not be used by any rules. If rules use this list, you must
update the rules to remove the list usage. When fetching or viewing a list,
you can see a list of rules that currently use the list, to know what rules
you need to update.
The list must pass the size restrictions for the new type.
The list content must pass validations for the new type. For example, if you
are changing a list type to CIDR, the content lines must all be valid
CIDR ranges.
String reference lists
The default type for a reference list is STRING. All values in the reference
list are treated as case sensitive strings, and Google Security Operations will check if
a field exactly matches any line in the reference list.
Comments begin with double forward slashes,
//
, and continue to the end of the
line. Comments can start on their own line, or can be inline with list content.
Anything contained in a comment is ignored during evaluation.
String reference lists support basic escaping: anything after a back slash (\)
will be escaped to itself. (e.g.
\/
->
/
). You can use escaping if you need to
include a double forward slash in a list line, as seen in the example below.
Example list content:
// This is a new line comment.

hostname-1
hostname-2
hostname-3 // This is an inline comment.
hostname-4

// The following line uses escaping and evaluates to:
// double forward // slash and back slash \
double forward \/\/ slash and back slash \\
When a string reference list contains a URL, escape the double forward slashes (//) using a backslash (), as shown in the example:
https:\/\/www.googleapis.com/compute/v1/projects/abcd
Restrictions for string lists:
Maximum list size: 6MB
Maximum length of any single list content line: 5000 characters
Using a STRING list for integers
You can't use an integer list to filter on numeric values, but you can use a STRING reference list for this purpose: Store the integer values in a STRING reference list, and use
strings.concat
in the UDM search or rule to convert the UDM field of type
int
into a string before checking whether it is in the reference list.
Examples
Your
port_list
contents:
8080
443
Use
strings.concat
to check for values in
port_list
:
strings.concat($e.principal.port , "") in %port_list
not strings.concat($e.principal.port , "") in %port_list
Special reference list types
The following list types let you do more complex matching on list content,
beyond exact string equality.
Regex lists
If list type is REGEX, Google SecOps interprets the list lines as regex and checks
if a field matches any regex in the list.
All regexes in a REGEX list follow
re2 library
regex syntax. The one
exception is that there is an escape sequence for forward slash:
\/
escapes to
/
. After handling this, the regex lines are sent as-is to our regex
engine, which handles other escape characters and other standard regex features.
Comments begin with double forward slashes,
//
, and continue to the
end of the line. Comments can start on their own line, or can be inline with
list content. If you want a regex to contain
//
, you can use
/{2}
or
\/\/
.
The following is an example of regex reference list content:
// This is a new line comment in a regex reference list.
.*chronicle.*
http:\/\/google\.com // This is an inline comment.
^[0-9].*\.gov$

// The line below is a potential problem. Everything after double forward slash is
// a comment, and is ignored.
http://website.com
The above reference list content parses into the regex content below:
.*chronicle.*
http://google\.com
^[0-9].*\.gov$
http:
Regex lists have the following size restrictions:
Maximum list size: 0.1MB
Maximum number of lines: 100
Maximum length of each content line: 5000 characters
CIDR lists
If list type is CIDR, Google SecOps interprets the list lines as Classless
Inter-Domain Routing (CIDR) ranges and checks if a field is within any of the
ranges in the list. A single CIDR list can mix and match both IPv4 ranges and
IPv6 ranges (e.g.
192.0.2.0/24
and
2001:db8::/32
), as specified in
RFC 4632
and
RFC 4291
.
Comments begin with double forward slashes,
//
, and continue to the
end of the line. Comments can start on their own line, or can be inline with
list content.
The following is an example CIDR reference list content:
// This is a comment

205.148.5.0/24 // This is an inline comment.
10.130.0.0/16
2002:1234:abcd:ffff:c0a8:101/64
CIDR lists have the following size restrictions:
Maximum list size: 0.1MB
Maximum number of lines: 150
Maximum length of each content line: 5000 characters
For Community blogs on managing rules, see:
Reference Lists
Regex Reference Lists
CIDR Reference Lists
