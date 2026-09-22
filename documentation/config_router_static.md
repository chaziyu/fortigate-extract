# config router static

> Source: `config router static.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
set-weight BGP weight for routing table. integer Minimum
value: 0
Maximum
value:
4294967295

### config router setting

Configure router settings.

#### Syntax

config router setting
Description: Configure router settings.
set hostname {string}
set show-filter {string}
end

#### Parameters

config router setting
Parameter Description Type Size Default
hostname Hostname for this virtual domain router. string Maximum
length: 14
show-filter Prefix-list as filter for showing routes. string Maximum
length: 35

### config router static

Configure IPv4 static routing tables.

#### Syntax

config router static
Description: Configure IPv4 static routing tables.
edit <seq-num>
set bfd [enable|disable]
set blackhole [enable|disable]
set comment {var-string}
set device {string}
set distance {integer}
set dst {ipv4-classnet}
set dstaddr {string}
set dynamic-gateway [enable|disable]
set gateway {ipv4-address}
set internet-service {integer}
set internet-service-custom {string}
set link-monitor-exempt [enable|disable]
set preferred-source {ipv4-address}
set priority {integer}
set sdwan-zone <name1>, <name2>, ...
set src {ipv4-classnet}
set status [enable|disable]
set tag {integer}
set vrf {integer}
set weight {integer}
next
end

#### Parameters

config router static
Parameter Description Type Size Default
bfd Enable/disable Bidirectional Forwarding Detection
(BFD).
option - disable
Option Description
enable Enable Bidirectional Forwarding Detection (BFD).
disable Disable Bidirectional Forwarding Detection (BFD).
blackhole Enable/disable black hole. option - disable
Option Description
enable Enable black hole.
disable Disable black hole.
comment Optional comments. var-string Maximum
length: 255
device Gateway out interface or tunnel. string Maximum
length: 35
distance Administrative distance. integer Minimum
value: 1
Maximum
value: 255
10
dst Destination IP and mask for this route. ipv4-
classnet
Not Specified 0.0.0.0
0.0.0.0
dstaddr Name of firewall address or address group. string Maximum
length: 79
dynamic-
gateway
Enable use of dynamic gateway retrieved from a
DHCP or PPP server.
option - disable
Option Description
enable Enable dynamic gateway.
disable Disable dynamic gateway.
Parameter Description Type Size Default
gateway Gateway IP for this route. ipv4-
address
Not Specified 0.0.0.0
internet-
service
Application ID in the Internet service database. integer Minimum
value: 0
Maximum
value:
4294967295
0
internet-
service-
custom
Application name in the Internet service custom
database.
string Maximum
length: 64
link-monitor-
exempt
Enable/disable withdrawal of this static route when
link monitor or health check is down.
option - disable
Option Description
enable Keep this static route when link monitor or health check is down.
disable Withdraw this static route when link monitor or health check is down. (default)
preferred-
source
Preferred source IP for this route. ipv4-
address
Not Specified 0.0.0.0
priority Administrative priority. integer Minimum
value: 1
Maximum
value: 65535
1
sdwan-zone
<name>
Choose SD-WAN Zone.
SD-WAN zone name.
string Maximum
length: 79
seq-num Sequence number. integer Minimum
value: 0
Maximum
value:
4294967295
0
src Source prefix for this route. ipv4-
classnet
Not Specified 0.0.0.0
0.0.0.0
status Enable/disable this static route. option - enable
Option Description
enable Enable static route.
disable Disable static route.
Parameter Description Type Size Default
tag Route tag. integer Minimum
value: 0
Maximum
value:
4294967295
0
vrf Virtual Routing Forwarding ID. integer Minimum
value: 0
Maximum
value: 251
unspecified
weight Administrative weight. integer Minimum
value: 0
Maximum
value: 255
0

### config router static6

Configure IPv6 static routing tables.

#### Syntax

config router static6
Description: Configure IPv6 static routing tables.
edit <seq-num>
set bfd [enable|disable]
set blackhole [enable|disable]
set comment {var-string}
set device {string}
set devindex {integer}
set distance {integer}
set dst {ipv6-network}
set dstaddr {string}
set dynamic-gateway [enable|disable]
set gateway {ipv6-address}
set link-monitor-exempt [enable|disable]
set priority {integer}
set sdwan-zone <name1>, <name2>, ...
set status [enable|disable]
set vrf {integer}
set weight {integer}
next
end

#### Parameters

config router static6
Parameter Description Type Size Default
bfd Enable/disable Bidirectional Forwarding Detection
(BFD).
option - disable
