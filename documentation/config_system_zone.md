# config system zone

> Source: `config system zone.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
power-level Power level. integer Minimum
value: 0
Maximum
value: 17
17
rogue-scan Enable/disable rogue scan. option - disable
Option Description
enable Enable rogue scan.
disable Disable rogue scan.
rogue-scan-
mac-
adjacency
MAC adjacency. integer Minimum
value: 0
Maximum
value: 31
7
short-guard-
interval
Enable/disable short guard interval. option - disable
Option Description
enable 400 ns long guard interval.
disable 800 ns short guard interval.

### config system zone

Configure zones to group two or more interfaces. When a zone is created you can configure policies for the zone instead
of individual interfaces in the zone.

#### Syntax

config system zone
Description: Configure zones to group two or more interfaces. When a zone is created you
can configure policies for the zone instead of individual interfaces in the zone.
edit <name>
set description {string}
set interface <interface-name1>, <interface-name2>, ...
set intrazone [allow|deny]
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
next
end

#### Parameters

config system zone
Parameter Description Type Size Default
description Description. string Maximum
length: 127
interface
<interface-
name>
Add interfaces to this zone. Interfaces must not be
assigned to another zone or have firewall policies
defined.
Select interfaces to add to the zone.
string Maximum
length: 79
intrazone Allow or deny traffic routing between different
interfaces in the same zone.
option - deny
Option Description
allow Allow traffic between interfaces in the zone.
deny Deny traffic between interfaces in the zone.
name Zone name. string Maximum
length: 35
config tagging
Parameter Description Type Size Default
category Tag category. string Maximum
length: 63
name Tagging entry name. string Maximum
length: 63
tags <name> Tags.
Tag name.
string Maximum
length: 79
