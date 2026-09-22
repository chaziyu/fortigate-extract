# config firewall addrgrp

> Source: `config firewall addrgrp.pdf`
> Repeated FortiOS page headers and footers were omitted.
> CLI spelling and parameter terminology follow the FortiOS 7.4.6 reference.

### config firewall addrgrp

Configure IPv4 address groups.

#### Syntax

```text

config firewall addrgrp
Description: Configure IPv4 address groups.
edit <name>
set allow-routing [enable|disable]
set category [default|ztna-ems-tag|...]
set color {integer}
set comment {var-string}
set exclude [enable|disable]
set exclude-member <name1>, <name2>, ...
set fabric-object [enable|disable]
set member <name1>, <name2>, ...
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set type [default|folder]
set uuid {uuid}
next
end

```

#### Parameters

```text

config firewall addrgrp
Parameter Description Type Size Default
allow-routing Enable/disable use of this group in the static route
configuration.
option - disable
Option Description
enable Enable use of this group in the static route configuration.
disable Disable use of this group in the static route configuration.
category Address group category. option - default
Option Description
default Default address group category (cannot be used as ztna-ems-tag/ztna-geo-
tag in policy).
ztna-ems-tag Members must be ztna-ems-tag group or ems-tag address, can be used as
ztna-ems-tag in policy.
ztna-geo-tag Members must be ztna-geo-tag group or geographic address, can be used as
ztna-geo-tag in policy.
Parameter Description Type Size Default
color Color of icon on the GUI. integer Minimum
value: 0
Maximum
value: 32
0
comment Comment. var-string Maximum
length: 255
exclude Enable/disable address exclusion. option - disable
Option Description
enable Enable address exclusion.
disable Disable address exclusion.
exclude-
member
<name>
Address exclusion member.
Address name.
string Maximum
length: 79
fabric-object Security Fabric global object setting. option - disable
Option Description
enable Object is set as a security fabric-wide global object.
disable Object is local to this security fabric member.
member
<name>
Address objects contained within the group.
Address name.
string Maximum
length: 79
name Address group name. string Maximum
length: 79
type Address group type. option - default
Option Description
default Default address group type (address may belong to multiple groups).
folder Address folder group (members may not belong to any other group).
uuid Universally Unique Identifier (UUID; automatically
assigned but can be manually reset).
uuid Not
Specified
00000000-0000-
0000-0000-
000000000000
config tagging
Parameter Description Type Size Default
category Tag category. string Maximum
length: 63
Parameter Description Type Size Default
name Tagging entry name. string Maximum
length: 63
tags <name> Tags.
Tag name.
string Maximum
length: 79

```

### config firewall addrgrp6

Configure IPv6 address groups.

#### Syntax

```text

config firewall addrgrp6
Description: Configure IPv6 address groups.
edit <name>
set color {integer}
set comment {var-string}
set exclude [enable|disable]
set exclude-member <name1>, <name2>, ...
set fabric-object [enable|disable]
set member <name1>, <name2>, ...
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set uuid {uuid}
next
end

```

#### Parameters

```text

config firewall addrgrp6
Parameter Description Type Size Default
color Integer value to determine the color of the icon in
the GUI.
integer Minimum
value: 0
Maximum
value: 32
0
comment Comment. var-string Maximum
length: 255
exclude Enable/disable address6 exclusion. option - disable
Option Description
enable Enable address6 exclusion.
disable Disable address6 exclusion.
```
