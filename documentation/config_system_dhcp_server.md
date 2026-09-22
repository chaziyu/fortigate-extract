# config system dhcp server

> Source: `config system dhcp server.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
start-ip Start of IP range. ipv6-
address
Not Specified ::
config prefix-range
Parameter Description Type Size Default
end-prefix End of prefix range. ipv6-
address
Not Specified ::
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
prefix-length Prefix length. integer Minimum
value: 1
Maximum
value: 128
0
start-prefix Start of prefix range. ipv6-
address
Not Specified ::

### config system dhcp server

Configure DHCP servers.

#### Syntax

config system dhcp server
Description: Configure DHCP servers.
edit <id>
set auto-configuration [disable|enable]
set auto-managed-status [disable|enable]
set conflicted-ip-timeout {integer}
set ddns-auth [disable|tsig]
set ddns-key {password_aes256}
set ddns-keyname {string}
set ddns-server-ip {ipv4-address}
set ddns-ttl {integer}
set ddns-update [disable|enable]
set ddns-update-override [disable|enable]
set ddns-zone {string}
set default-gateway {ipv4-address}
set dhcp-settings-from-fortiipam [disable|enable]
set dns-server1 {ipv4-address}
set dns-server2 {ipv4-address}
set dns-server3 {ipv4-address}
set dns-server4 {ipv4-address}
set dns-service [local|default|...]
set domain {string}
config exclude-range
Description: Exclude one or more ranges of IP addresses from being assigned to
clients.
edit <id>
set end-ip {ipv4-address}
set lease-time {integer}
set start-ip {ipv4-address}
set uci-match [disable|enable]
set uci-string <uci-string1>, <uci-string2>, ...
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
next
end
set filename {string}
set forticlient-on-net-status [disable|enable]
set interface {string}
set ip-mode [range|usrgrp]
config ip-range
Description: DHCP IP range configuration.
edit <id>
set end-ip {ipv4-address}
set lease-time {integer}
set start-ip {ipv4-address}
set uci-match [disable|enable]
set uci-string <uci-string1>, <uci-string2>, ...
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
next
end
set ipsec-lease-hold {integer}
set lease-time {integer}
set mac-acl-default-action [assign|block]
set netmask {ipv4-netmask}
set next-server {ipv4-address}
set ntp-server1 {ipv4-address}
set ntp-server2 {ipv4-address}
set ntp-server3 {ipv4-address}
set ntp-service [local|default|...]
config options
Description: DHCP options.
edit <id>
set code {integer}
set ip {user}
set type [hex|string|...]
set uci-match [disable|enable]
set uci-string <uci-string1>, <uci-string2>, ...
set value {string}
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
next
end
set relay-agent {ipv4-address}
config reserved-address
Description: Options for the DHCP server to assign IP settings to specific MAC
addresses.
edit <id>
set action [assign|block|...]
set circuit-id {string}
set circuit-id-type [hex|string]
set description {var-string}
set ip {ipv4-address}
set mac {mac-address}
set remote-id {string}
set remote-id-type [hex|string]
set type [mac|option82]
next
end
set server-type [regular|ipsec]
set shared-subnet [disable|enable]
set status [disable|enable]
set tftp-server <tftp-server1>, <tftp-server2>, ...
set timezone {string}
set timezone-option [disable|default|...]
set vci-match [disable|enable]
set vci-string <vci-string1>, <vci-string2>, ...
set wifi-ac-service [specify|local]
set wifi-ac1 {ipv4-address}
set wifi-ac2 {ipv4-address}
set wifi-ac3 {ipv4-address}
set wins-server1 {ipv4-address}
set wins-server2 {ipv4-address}
next
end

#### Parameters

config system dhcp server
Parameter Description Type Size Default
auto-
configuration
Enable/disable auto configuration. option - enable
Option Description
disable Disable auto configuration.
enable Enable auto configuration.
auto-managed-
status
Enable/disable use of this DHCP server once this
interface has been assigned an IP address from
FortiIPAM.
option - enable
Parameter Description Type Size Default
Option Description
disable Disable use of this DHCP server once this interface has been assigned an IP
address from FortiIPAM.
enable Enable use of this DHCP server once this interface has been assigned an IP
address from FortiIPAM.
conflicted-ip-
timeout
Time in seconds to wait after a conflicted IP
address is removed from the DHCP range before it
can be reused.
integer Minimum
value: 60
Maximum
value:
8640000
1800
ddns-auth DDNS authentication mode. option - disable
Option Description
disable Disable DDNS authentication.
tsig TSIG based on RFC2845.
ddns-key DDNS update key (base 64 encoding). password_
aes256
Not Specified
ddns-keyname DDNS update key name. string Maximum
length: 64
ddns-server-ip DDNS server IP. ipv4-address Not Specified 0.0.0.0
ddns-ttl TTL. integer Minimum
value: 60
Maximum
value: 86400
300
ddns-update Enable/disable DDNS update for DHCP. option - disable
Option Description
disable Disable DDNS update for DHCP.
enable Enable DDNS update for DHCP.
ddns-update-
override
Enable/disable DDNS update override for DHCP. option - disable
Option Description
disable Disable DDNS update override for DHCP.
enable Enable DDNS update override for DHCP.
Parameter Description Type Size Default
ddns-zone Zone of your domain name (ex. DDNS.com). string Maximum
length: 64
default-
gateway
Default gateway IP address assigned by the DHCP
server.
ipv4-address Not Specified 0.0.0.0
dhcp-settings-
from-fortiipam
Enable/disable populating of DHCP server settings
from FortiIPAM.
option - disable
Option Description
disable Disable populating of DHCP server settings from FortiIPAM.
enable Enable populating of DHCP server settings from FortiIPAM.
dns-server1 DNS server 1. ipv4-address Not Specified 0.0.0.0
dns-server2 DNS server 2. ipv4-address Not Specified 0.0.0.0
dns-server3 DNS server 3. ipv4-address Not Specified 0.0.0.0
dns-server4 DNS server 4. ipv4-address Not Specified 0.0.0.0
dns-service Options for assigning DNS servers to DHCP
clients.
option - specify
Option Description
local IP address of the interface the DHCP server is added to becomes the client's
DNS server IP address.
default Clients are assigned the FortiGate's configured DNS servers.
specify Specify up to 3 DNS servers in the DHCP server configuration.
domain Domain name suffix for the IP addresses that the
DHCP server assigns to clients.
string Maximum
length: 35
filename Name of the boot file on the TFTP server. string Maximum
length: 127
forticlient-on-
net-status
Enable/disable FortiClient-On-Net service for this
DHCP server.
option - enable
Option Description
disable Disable FortiClient On-Net Status.
enable Enable FortiClient On-Net Status.
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
Parameter Description Type Size Default
interface DHCP server can assign IP configurations to
clients connected to this interface.
string Maximum
length: 15
ip-mode Method used to assign client IP. option - range
Option Description
range Use range defined by start-ip/end-ip to assign client IP.
usrgrp Use user-group defined method to assign client IP.
ipsec-lease-
hold
DHCP over IPsec leases expire this many seconds
after tunnel down (0 to disable forced-expiry).
integer Minimum
value: 0
Maximum
value:
8640000
60
lease-time Lease time in seconds, 0 means unlimited. integer Minimum
value: 300
Maximum
value:
8640000
604800
mac-acl-
default-action
MAC access control default action (allow or block
assigning IP settings).
option - assign
Option Description
assign Allow the DHCP server to assign IP settings to clients on the MAC access
control list.
block Block the DHCP server from assigning IP settings to clients on the MAC
access control list.
netmask Netmask assigned by the DHCP server. ipv4-netmask Not Specified 0.0.0.0
next-server IP address of a server (for example, a TFTP sever)
that DHCP clients can download a boot file from.
ipv4-address Not Specified 0.0.0.0
ntp-server1 NTP server 1. ipv4-address Not Specified 0.0.0.0
ntp-server2 NTP server 2. ipv4-address Not Specified 0.0.0.0
ntp-server3 NTP server 3. ipv4-address Not Specified 0.0.0.0
ntp-service Options for assigning Network Time Protocol
(NTP) servers to DHCP clients.
option - specify
Option Description
local IP address of the interface the DHCP server is added to becomes the client's
NTP server IP address.
Parameter Description Type Size Default
Option Description
default Clients are assigned the FortiGate's configured NTP servers.
specify Specify up to 3 NTP servers in the DHCP server configuration.
relay-agent Relay agent IP. ipv4-address Not Specified 0.0.0.0
server-type DHCP server can be a normal DHCP server or an
IPsec DHCP server.
option - regular
Option Description
regular Regular DHCP service.
ipsec DHCP over IPsec service.
shared-subnet Enable/disable shared subnet. option - disable
Option Description
disable Disable shared subnet.
enable Enable shared subnet.
status Enable/disable this DHCP configuration. option - enable
Option Description
disable Do not use this DHCP server configuration.
enable Use this DHCP server configuration.
tftp-server
<tftp-
server>
One or more hostnames or IP addresses of the
TFTP servers in quotes separated by spaces.
TFTP server.
string Maximum
length: 63
timezone Select the time zone to be assigned to DHCP
clients.
string Maximum
length: 63
timezone-
option
Options for the DHCP server to set the client's time
zone.
option - disable
Option Description
disable Do not set the client's time zone.
default Clients are assigned the FortiGate's configured time zone.
specify Specify the time zone to be assigned to DHCP clients.
Parameter Description Type Size Default
vci-match Enable/disable vendor class identifier (VCI)
matching. When enabled only DHCP requests with
a matching VCI are served.
option - disable
Option Description
disable Disable VCI matching.
enable Enable VCI matching.
vci-string
<vci-
string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string Maximum
length: 255
wifi-ac-service Options for assigning WiFi access controllers to
DHCP clients.
option - specify
Option Description
specify Specify up to 3 WiFi Access Controllers in the DHCP server configuration.
local IP address of the interface the DHCP server is added to becomes the client's
WiFi Access Controller IP address.
wifi-ac1 WiFi Access Controller 1 IP address (DHCP option
138, RFC 5417).
ipv4-address Not Specified 0.0.0.0
wifi-ac2 WiFi Access Controller 2 IP address (DHCP option
138, RFC 5417).
ipv4-address Not Specified 0.0.0.0
wifi-ac3 WiFi Access Controller 3 IP address (DHCP option
138, RFC 5417).
ipv4-address Not Specified 0.0.0.0
wins-server1 WINS server 1. ipv4-address Not Specified 0.0.0.0
wins-server2 WINS server 2. ipv4-address Not Specified 0.0.0.0
config exclude-range
Parameter Description Type Size Default
end-ip End of IP range. ipv4-
address
Not Specified 0.0.0.0
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
Parameter Description Type Size Default
lease-time Lease time in seconds, 0 means default lease time. integer Minimum
value: 300
Maximum
value:
8640000
0
start-ip Start of IP range. ipv4-
address
Not Specified 0.0.0.0
uci-match Enable/disable user class identifier (UCI) matching.
When enabled only DHCP requests with a matching
UCI are served with this range.
option - disable
Option Description
disable Disable UCI matching.
enable Enable UCI matching.
uci-string
<uci-
string>
One or more UCI strings in quotes separated by
spaces.
UCI strings.
string Maximum
length: 255
vci-match Enable/disable vendor class identifier (VCI)
matching. When enabled only DHCP requests with a
matching VCI are served with this range.
option - disable
Option Description
disable Disable VCI matching.
enable Enable VCI matching.
vci-string
<vci-
string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string Maximum
length: 255
config ip-range
Parameter Description Type Size Default
end-ip End of IP range. ipv4-
address
Not Specified 0.0.0.0
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
Parameter Description Type Size Default
lease-time Lease time in seconds, 0 means default lease time. integer Minimum
value: 300
Maximum
value:
8640000
0
start-ip Start of IP range. ipv4-
address
Not Specified 0.0.0.0
uci-match Enable/disable user class identifier (UCI) matching.
When enabled only DHCP requests with a matching
UCI are served with this range.
option - disable
Option Description
disable Disable UCI matching.
enable Enable UCI matching.
uci-string
<uci-
string>
One or more UCI strings in quotes separated by
spaces.
UCI strings.
string Maximum
length: 255
vci-match Enable/disable vendor class identifier (VCI)
matching. When enabled only DHCP requests with a
matching VCI are served with this range.
option - disable
Option Description
disable Disable VCI matching.
enable Enable VCI matching.
vci-string
<vci-
string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string Maximum
length: 255
config options
Parameter Description Type Size Default
code DHCP option code. integer Minimum
value: 0
Maximum
value: 255
0
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
Parameter Description Type Size Default
ip DHCP option IPs. user Not Specified
type DHCP option type. option - hex
Option Description
hex DHCP option in hex.
string DHCP option in string.
ip DHCP option in IP.
fqdn DHCP option in domain search option format.
uci-match Enable/disable user class identifier (UCI) matching.
When enabled only DHCP requests with a matching
UCI are served with this option.
option - disable
Option Description
disable Disable UCI matching.
enable Enable UCI matching.
uci-string
<uci-
string>
One or more UCI strings in quotes separated by
spaces.
UCI strings.
string Maximum
length: 255
value DHCP option value. string Maximum
length: 312
vci-match Enable/disable vendor class identifier (VCI)
matching. When enabled only DHCP requests with a
matching VCI are served with this option.
option - disable
Option Description
disable Disable VCI matching.
enable Enable VCI matching.
vci-string
<vci-
string>
One or more VCI strings in quotes separated by
spaces.
VCI strings.
string Maximum
length: 255
config reserved-address
Parameter Description Type Size Default
action Options for the DHCP server to configure
the client with the reserved MAC address.
option - reserved
Parameter Description Type Size Default
Option Description
assign Configure the client with this MAC address like any other client.
block Block the DHCP server from assigning IP settings to the client with this MAC
address.
reserved Assign the reserved IP address to the client with this MAC address.
circuit-id Option 82 circuit-ID of the client that will get
the reserved IP address.
string Maximum
length: 312
circuit-id-type DHCP option type. option - string
Option Description
hex DHCP option in hex.
string DHCP option in string.
description Description. var-string Maximum
length: 255
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
ip IP address to be reserved for the MAC
address.
ipv4-
address
Not Specified 0.0.0.0
mac MAC address of the client that will get the
reserved IP address.
mac-
address
Not Specified 00:00:00:00:00:00
remote-id Option 82 remote-ID of the client that will get
the reserved IP address.
string Maximum
length: 312
remote-id-
type
DHCP option type. option - string
Option Description
hex DHCP option in hex.
string DHCP option in string.
type DHCP reserved-address type. option - mac
Option Description
mac Match with MAC address.
option82 Match with DHCP option 82.
