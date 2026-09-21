# config firewall ippool

> Source: `config firewal ippool.pdf`
> Repeated FortiOS page headers and footers were omitted.
> CLI spelling and parameter terminology follow the FortiOS 7.4.6 reference.

### config firewall ippool

Configure IPv4 IP pools.

#### Syntax

```text

config firewall ippool
Description: Configure IPv4 IP pools.
edit <name>
set add-nat64-route [disable|enable]
set arp-intf {string}
set arp-reply [disable|enable]
set associated-interface {string}
set block-size {integer}
set cgn-block-size {integer}
set cgn-client-endip {var-string}
set cgn-client-ipv6shift {integer}
set cgn-client-startip {var-string}
set cgn-fixedalloc [disable|enable]
set cgn-overload [disable|enable]
set cgn-port-end {integer}
set cgn-port-start {integer}
set cgn-spa [disable|enable]
set comments {var-string}
set endip {ipv4-address-any}
set endport {integer}
set exclude-ip <ip1>, <ip2>, ...
set nat64 [disable|enable]
set num-blocks-per-user {integer}
set pba-interim-log {integer}
set pba-timeout {integer}
set permit-any-host [disable|enable]
set port-per-user {integer}
set source-endip {ipv4-address-any}
set source-startip {ipv4-address-any}
set startip {ipv4-address-any}
set startport {integer}
set subnet-broadcast-in-ippool [disable|enable]
set type [overload|one-to-one|...]
set utilization-alarm-clear {integer}
set utilization-alarm-raise {integer}
next
end

```

#### Parameters

```text

config firewall ippool
Parameter Description Type Size Default
add-nat64-
route
Enable/disable adding NAT64 route. option - enable
Option Description
disable Disable adding NAT64 route.
enable Enable adding NAT64 route.
Parameter Description Type Size Default
arp-intf Select an interface from available options that will reply
to ARP requests. (If blank, any is selected).
string Maximum
length: 15
arp-reply Enable/disable replying to ARP requests when an IP
Pool is added to a policy.
option - enable
Option Description
disable Disable ARP reply.
enable Enable ARP reply.
associated-
interface
Associated interface name. string Maximum
length: 15
block-size Number of addresses in a block. integer Minimum
value: 64
Maximum
value: 4096
128
cgn-block-
size *
Number of ports in a block. integer Minimum
value: 64
Maximum
value: 4096
128
cgn-client-
endip *
Final client IPv4 address (inclusive) (format
xxx.xxx.xxx.xxx, Default: 0.0.0.0).
var-string Maximum
length: 255
cgn-client-
ipv6shift *
IPv6 shift for fixed-allocation. integer Minimum
value: 0
Maximum
value: 127
0
cgn-client-
startip *
First client IPv4 address (inclusive) (format
xxx.xxx.xxx.xxx, Default: 0.0.0.0).
var-string Maximum
length: 255
cgn-fixedalloc
*
Enable/disable fixed-allocation mode. option - disable
Option Description
disable Disable fixed-allocation mode.
enable Enable fixed-allocation mode.
cgn-overload
*
Enable/disable overload mode. option - disable
Option Description
disable Disable overload mode.
enable Enable overload mode.
Parameter Description Type Size Default
cgn-port-end * Ending public port can be allocated. integer Minimum
value: 1024
Maximum
value:
65535
65530
cgn-port-start
*
Starting public port can be allocated. integer Minimum
value: 1024
Maximum
value:
65535
5117
cgn-spa * Enable/disable single port allocation mode. option - disable
Option Description
disable Disable SPA mode.
enable Enable SPA mode.
comments Comment. var-string Maximum
length: 255
endip Final IPv4 address (inclusive) in the range for the
address pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).
ipv4-
address-
any
Not
Specified
0.0.0.0
endport Final port number (inclusive) in the range for the
address pool (Default: 65533).
integer Minimum
value: 5117
Maximum
value:
65533
65533
exclude-ip
<ip> *
Exclude IPs x.x.x.x.
Exclude IPs (xxx.xxx.xxx.xxx)
string Maximum
length: 79
name IP pool name. string Maximum
length: 79
nat64 Enable/disable NAT64. option - disable
Option Description
disable Disable DNAT64.
enable Enable DNAT64.
num-blocks-
per-user
Number of addresses blocks that can be used by a user. integer Minimum
value: 1
Maximum
value: 128
8
Parameter Description Type Size Default
pba-interim-
log
Port block allocation interim logging interval. integer Minimum
value: 600
Maximum
value:
86400
0
pba-timeout Port block allocation timeout (seconds). integer Minimum
value: 3
Maximum
value:
86400
30
permit-any-
host
Enable/disable full cone NAT. option - disable
Option Description
disable Disable full cone NAT.
enable Enable full cone NAT.
port-per-user Number of port for each user. integer Minimum
value: 32
Maximum
value:
60417
0
source-endip Final IPv4 address (inclusive) in the range of the source
addresses to be translated (format xxx.xxx.xxx.xxx,
Default: 0.0.0.0).
ipv4-
address-
any
Not
Specified
0.0.0.0
source-startip First IPv4 address. ipv4-
address-
any
Not
Specified
0.0.0.0
startip First IPv4 address (inclusive) in the range for the
address pool (format xxx.xxx.xxx.xxx, Default: 0.0.0.0).
ipv4-
address-
any
Not
Specified
0.0.0.0
startport First port number (inclusive) in the range for the address
pool (Default: 5117).
integer Minimum
value: 5117
Maximum
value:
65533
5117
subnet-
broadcast-in-
ippool
Enable/disable inclusion of the subnetwork address and
broadcast IP address in the NAT64 IP pool.
option - enable
Parameter Description Type Size Default
Option Description
disable Do not include the subnetwork address and broadcast IP address in the
NAT64 IP pool.
enable Include the subnetwork address and broadcast IP address in the NAT64 IP
pool.
type IP pool type: overload, one-to-one, fixed-port-range,
port-block-allocation, cgn-resource-allocation
(hyperscale vdom only)
option - overload
Option Description
overload IP addresses in the IP pool can be shared by clients.
one-to-one One to one mapping.
fixed-port-range Fixed port range.
port-block-
allocation
Port block allocation.
utilization-
alarm-clear *
Pool utilization alarm clear threshold. integer Minimum
value: 40
Maximum
value: 100
80
utilization-
alarm-raise *
Pool utilization alarm raise threshold. integer Minimum
value: 50
Maximum
value: 100
100
- This parameter may not exist in some models.

```

### config firewall ippool6

Configure IPv6 IP pools.

#### Syntax

```text

config firewall ippool6
Description: Configure IPv6 IP pools.
edit <name>
set add-nat46-route [disable|enable]
set comments {var-string}
set endip {ipv6-address}
set nat46 [disable|enable]
set startip {ipv6-address}
next
end

```
