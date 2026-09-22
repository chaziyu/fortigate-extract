# config firewall vipgrp

> Source: `config firewall vipgrp.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
versions SSL/TLS versions that the cipher suite can be used
with.
option - ssl-3.0 tls-
1.0 tls-1.1
tls-1.2 tls-
1.3
Option Description
ssl-3.0 SSL 3.0.
tls-1.0 TLS 1.0.
tls-1.1 TLS 1.1.
tls-1.2 TLS 1.2.
tls-1.3 TLS 1.3.

### config firewall vipgrp

Configure IPv4 virtual IP groups.

#### Syntax

config firewall vipgrp
Description: Configure IPv4 virtual IP groups.
edit <name>
set color {integer}
set comments {var-string}
set interface {string}
set member <name1>, <name2>, ...
set uuid {uuid}
next
end

#### Parameters

config firewall vipgrp
Parameter Description Type Size Default
color Integer value to determine the color of the icon in
the GUI.
integer Minimum
value: 0
Maximum
value: 32
0
comments Comment. var-string Maximum
length: 255
interface Interface. string Maximum
length: 35
member
<name>
Member VIP objects of the group (Separate
multiple objects with a space).
VIP name.
string Maximum
length: 79
Parameter Description Type Size Default
name VIP group name. string Maximum
length: 79
uuid Universally Unique Identifier (UUID; automatically
assigned but can be manually reset).
uuid Not
Specified
00000000-0000-
0000-0000-
000000000000

### config firewall vipgrp6

Configure IPv6 virtual IP groups.

#### Syntax

config firewall vipgrp6
Description: Configure IPv6 virtual IP groups.
edit <name>
set color {integer}
set comments {var-string}
set member <name1>, <name2>, ...
set uuid {uuid}
next
end

#### Parameters

config firewall vipgrp6
Parameter Description Type Size Default
color Integer value to determine the color of the icon in
the GUI.
integer Minimum
value: 0
Maximum
value: 32
0
comments Comment. var-string Maximum
length: 255
member
<name>
Member VIP objects of the group (Separate
multiple objects with a space).
IPv6 VIP name.
string Maximum
length: 79
name IPv6 VIP group name. string Maximum
length: 79
uuid Universally Unique Identifier (UUID; automatically
assigned but can be manually reset).
uuid Not
Specified
00000000-0000-
0000-0000-
000000000000

### config firewall wildcard-fqdn custom

Config global/VDOM Wildcard FQDN address.
