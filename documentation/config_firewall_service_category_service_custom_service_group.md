# config firewall service category service custom service group

> Source: `config firewall service category, service category, service group.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
status Enable or disable this policy. option - enable
Option Description
enable Enable setting.
disable Disable setting.
url-category URL categories or groups. user Not Specified
users <name> Names of individual users that can authenticate
with this policy.
User name.
string Maximum
length: 79
uuid Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid Not Specified 00000000-0000-
0000-0000-
000000000000
videofilter-
profile
Name of an existing VideoFilter profile. string Maximum
length: 35
virtual-patch-
profile
Name of an existing virtual-patch profile. string Maximum
length: 35
voip-profile Name of an existing VoIP (voipd) profile. string Maximum
length: 35
webfilter-
profile
Name of an existing Web filter profile. string Maximum
length: 35

### config firewall service category

Configure service categories.

#### Syntax

config firewall service category
Description: Configure service categories.
edit <name>
set comment {var-string}
set fabric-object [enable|disable]
next
end

#### Parameters

config firewall service category
Parameter Description Type Size Default
comment Comment. var-string Maximum
length: 255
fabric-object Security Fabric global object setting. option - disable
Parameter Description Type Size Default
Option Description
enable Object is set as a security fabric-wide global object.
disable Object is local to this security fabric member.
name Service category name. string Maximum
length: 63

### config firewall service custom

Configure custom services.

#### Syntax

config firewall service custom
Description: Configure custom services.
edit <name>
set app-category <id1>, <id2>, ...
set app-service-type [disable|app-id|...]
set application <id1>, <id2>, ...
set category {string}
set check-reset-range [disable|strict|...]
set color {integer}
set comment {var-string}
set fabric-object [enable|disable]
set fqdn {string}
set helper [auto|disable|...]
set icmpcode {integer}
set icmptype {integer}
set iprange {user}
set protocol [TCP/UDP/SCTP|ICMP|...]
set protocol-number {integer}
set proxy [enable|disable]
set sctp-portrange {user}
set session-ttl {user}
set tcp-halfclose-timer {integer}
set tcp-halfopen-timer {integer}
set tcp-portrange {user}
set tcp-rst-timer {integer}
set tcp-timewait-timer {integer}
set udp-idle-timer {integer}
set udp-portrange {user}
set uuid {uuid}
next
end

#### Parameters

config firewall service custom
Parameter Description Type Size Default
app-category
<id>
Application category ID.
Application category id.
integer Minimum
value: 0
Maximum
value:
4294967295
app-service-
type
Application service type. option - disable
Option Description
disable Disable application type.
app-id Application ID.
app-category Applicatin category.
application
<id>
Application ID.
Application id.
integer Minimum
value: 0
Maximum
value:
4294967295
category Service category. string Maximum
length: 63
check-reset-
range
Configure the type of ICMP error message
verification.
option - default
Option Description
disable Disable RST range check.
strict Check RST range strictly.
default Using system default setting.
color Color of icon on the GUI. integer Minimum
value: 0
Maximum
value: 32
0
comment Comment. var-string Maximum
length: 255
fabric-object Security Fabric global object setting. option - disable
Option Description
enable Object is set as a security fabric-wide global object.
disable Object is local to this security fabric member.
Parameter Description Type Size Default
fqdn Fully qualified domain name. string Maximum
length: 255
helper Helper name. option - auto
Option Description
auto Automatically select helper based on protocol and port.
disable Disable helper.
ftp FTP.
tftp TFTP.
ras RAS.
h323 H323.
tns TNS.
mms MMS.
sip SIP.
pptp PPTP.
rtsp RTSP.
dns-udp DNS UDP.
dns-tcp DNS TCP.
pmap PMAP.
rsh RSH.
dcerpc DCERPC.
mgcp MGCP.
icmpcode ICMP code. integer Minimum
value: 0
Maximum
value: 255
icmptype ICMP type. integer Minimum
value: 0
Maximum
value:
4294967295
iprange Start and end of the IP range associated with
service.
user Not Specified
Parameter Description Type Size Default
name Custom service name. string Maximum
length: 79
protocol Protocol type based on IANA numbers. option - TCP/UDP/SCTP
Option Description
TCP/UDP/SCTP TCP, UDP and SCTP.
ICMP ICMP.
ICMP6 ICMP6.
IP IP.
HTTP HTTP - for web proxy.
FTP FTP - for web proxy.
CONNECT Connect - for web proxy.
SOCKS-TCP Socks TCP - for web proxy.
SOCKS-UDP Socks UDP - for web proxy.
ALL All - for web proxy.
protocol-
number
IP protocol number. integer Minimum
value: 0
Maximum
value: 254
0
proxy Enable/disable web proxy service. option - disable
Option Description
enable Enable setting.
disable Disable setting.
sctp-
portrange
Multiple SCTP port ranges. user Not Specified
session-ttl Session TTL. user Not Specified
tcp-halfclose-
timer
Wait time to close a TCP session waiting for an
unanswered FIN packet.
integer Minimum
value: 0
Maximum
value: 86400
0
tcp-halfopen-
timer
Wait time to close a TCP session waiting for an
unanswered open session packet.
integer Minimum
value: 0
Maximum
value: 86400
0
Parameter Description Type Size Default
tcp-portrange Multiple TCP port ranges. user Not Specified
tcp-rst-timer Set the length of the TCP CLOSE state in
seconds.
integer Minimum
value: 5
Maximum
value: 300
0
tcp-timewait-
timer
Set the length of the TCP TIME-WAIT state in
seconds.
integer Minimum
value: 0
Maximum
value: 300
0
udp-idle-timer Number of seconds before an idle UDP
connection times out.
integer Minimum
value: 0
Maximum
value: 86400
0
udp-portrange Multiple UDP port ranges. user Not Specified
uuid Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid Not Specified 00000000-0000-
0000-0000-
000000000000

### config firewall service group

Configure service groups.

#### Syntax

config firewall service group
Description: Configure service groups.
edit <name>
set color {integer}
set comment {var-string}
set fabric-object [enable|disable]
set member <name1>, <name2>, ...
set proxy [enable|disable]
set uuid {uuid}
next
end

#### Parameters

config firewall service group
Parameter Description Type Size Default
color Color of icon on the GUI. integer Minimum
value: 0
Maximum
value: 32
0
Parameter Description Type Size Default
comment Comment. var-string Maximum
length: 255
fabric-object Security Fabric global object setting. option - disable
Option Description
enable Object is set as a security fabric-wide global object.
disable Object is local to this security fabric member.
member
<name>
Service objects contained within the group.
Service or service group name.
string Maximum
length: 79
name Service group name. string Maximum
length: 79
proxy Enable/disable web proxy service group. option - disable
Option Description
enable Enable setting.
disable Disable setting.
uuid Universally Unique Identifier (UUID; automatically
assigned but can be manually reset).
uuid Not
Specified
00000000-0000-
0000-0000-
000000000000

### config firewall shaper per-ip-shaper
