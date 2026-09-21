# config firewall schedule

> Source: `config firewall schedule.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
ztna-ems-tag
<name>
ZTNA EMS Tag names.
EMS Tag name.
string Maximum
length: 79
ztna-tags-
match-logic
ZTNA tag matching logic. option - or
Option Description
or Match ZTNA tags using a logical OR operator.
and Match ZTNA tags using a logical AND operator.
- This parameter may not exist in some models.

### config firewall region

Define region table. Read-only.

#### Syntax

config firewall region
Description: Define region table. Read-only.
edit <id>
set city <id1>, <id2>, ...
set name {string}
next
end

#### Parameters

config firewall region
Parameter Description Type Size Default
city <id> City ID list.
City ID.
integer Minimum
value: 0
Maximum
value:
65535
id Region ID. integer Minimum
value: 0
Maximum
value:
65535
0
name Region name. string Maximum
length: 63

### config firewall schedule group

Schedule group configuration.

#### Syntax

config firewall schedule group
Description: Schedule group configuration.
edit <name>
set color {integer}
set fabric-object [enable|disable]
set member <name1>, <name2>, ...
next
end

#### Parameters

config firewall schedule group
Parameter Description Type Size Default
color Color of icon on the GUI. integer Minimum
value: 0
Maximum
value: 32
0
fabric-object Security Fabric global object setting. option - disable
Option Description
enable Object is set as a security fabric-wide global object.
disable Object is local to this security fabric member.
member
<name>
Schedules added to the schedule group.
Schedule name.
string Maximum
length: 79
name Schedule group name. string Maximum
length: 31

### config firewall schedule onetime

Onetime schedule configuration.

#### Syntax

config firewall schedule onetime
Description: Onetime schedule configuration.
edit <name>
set color {integer}
set end {user}
set end-utc {user}
set expiration-days {integer}
set fabric-object [enable|disable]
set start {user}
set start-utc {user}
next
end

#### Parameters

config firewall schedule onetime
Parameter Description Type Size Default
color Color of icon on the GUI. integer Minimum
value: 0
Maximum
value: 32
0
end Schedule end date and time, format hh:mm
yyyy/mm/dd.
user Not
Specified
end-utc Schedule end date and time, in epoch format. user Not
Specified
expiration-
days
Write an event log message this many days before the
schedule expires.
integer Minimum
value: 0
Maximum
value: 100
3
fabric-object Security Fabric global object setting. option - disable
Option Description
enable Object is set as a security fabric-wide global object.
disable Object is local to this security fabric member.
name Onetime schedule name. string Maximum
length: 31
start Schedule start date and time, format hh:mm
yyyy/mm/dd.
user Not
Specified
start-utc Schedule start date and time, in epoch format. user Not
Specified

### config firewall schedule recurring

Recurring schedule configuration.

#### Syntax

config firewall schedule recurring
Description: Recurring schedule configuration.
edit <name>
set color {integer}
set day {option1}, {option2}, ...
set end {user}
set fabric-object [enable|disable]
set start {user}
next
end

#### Parameters

config firewall schedule recurring
Parameter Description Type Size Default
color Color of icon on the GUI. integer Minimum
value: 0
Maximum
value: 32
0
day One or more days of the week on which the schedule is
valid. Separate the names of the days with a space.
option - none
Option Description
sunday Sunday.
monday Monday.
tuesday Tuesday.
wednesday Wednesday.
thursday Thursday.
friday Friday.
saturday Saturday.
none None.
end Time of day to end the schedule, format hh:mm. user Not
Specified
fabric-object Security Fabric global object setting. option - disable
Option Description
enable Object is set as a security fabric-wide global object.
disable Object is local to this security fabric member.
name Recurring schedule name. string Maximum
length: 31
start Time of day to start the schedule, format hh:mm. user Not
Specified

### config firewall security-policy

Configure NGFW IPv4/IPv6 application policies.

#### Syntax

config firewall security-policy
Description: Configure NGFW IPv4/IPv6 application policies.
edit <policyid>
set action [accept|deny]
set app-category <id1>, <id2>, ...
