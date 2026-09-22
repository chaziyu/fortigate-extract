# config firewall address references

> Source: `config firewall address references.pdf`
> Repeated FortiOS page headers and footers were omitted.
> CLI spelling and parameter terminology follow the FortiOS 7.4.6 reference.

### config firewall address

Configure IPv4 addresses.

#### Syntax

```text

config firewall address
Description: Configure IPv4 addresses.
edit <name>
set allow-routing [enable|disable]
set associated-interface {string}
set cache-ttl {integer}
set clearpass-spt [unknown|healthy|...]
set color {integer}
set comment {var-string}
set country {string}
set end-ip {ipv4-address-any}
set epg-name {string}
set fabric-object [enable|disable]
set filter {var-string}
set fqdn {string}
set fsso-group <name1>, <name2>, ...
set hw-model {string}
set hw-vendor {string}
set interface {string}
config list
Description: IP address list.
edit <ip>
next
end
set macaddr <macaddr1>, <macaddr2>, ...
set node-ip-only [enable|disable]
set obj-id {var-string}
set obj-tag {string}
set obj-type [ip|mac]
set organization {string}
set os {string}
set policy-group {string}
set route-tag {integer}
set sdn {string}
set sdn-addr-type [private|public|...]
set sdn-tag {string}
set start-ip {ipv4-address-any}
set sub-type [sdn|clearpass-spt|...]
set subnet {ipv4-classnet-any}
set subnet-name {string}
set sw-version {string}
set tag-detection-level {string}
set tag-type {string}
config tagging
Description: Config object tagging.
edit <name>
set category {string}
set tags <name1>, <name2>, ...
next
end
set tenant {string}
set type [ipmask|iprange|...]
set uuid {uuid}
set wildcard {ipv4-classnet-any}
set wildcard-fqdn {string}
next
end

```

#### Parameters

```text

config firewall address
Parameter Description Type Size Default
allow-routing Enable/disable use of this address in the static
route configuration.
option - disable
Option Description
enable Enable use of this address in the static route configuration.
disable Disable use of this address in the static route configuration.
Parameter Description Type Size Default
associated-
interface
Network interface associated with address. string Maximum
length: 35
cache-ttl Defines the minimal TTL of individual IP
addresses in FQDN cache measured in
seconds.
integer Minimum
value: 0
Maximum
value: 86400
0
clearpass-spt SPT (System Posture Token) value. option - unknown
Option Description
unknown UNKNOWN.
healthy HEALTHY.
quarantine QUARANTINE.
checkup CHECKUP.
transient TRANSIENT.
infected INFECTED.
color Color of icon on the GUI. integer Minimum
value: 0
Maximum
value: 32
0
comment Comment. var-string Maximum
length: 255
country IP addresses associated to a specific country. string Maximum
length: 2
end-ip Final IP address (inclusive) in the range for the
address.
ipv4-
address-
any
Not Specified 0.0.0.0
epg-name Endpoint group name. string Maximum
length: 255
fabric-object Security Fabric global object setting. option - disable
Option Description
enable Object is set as a security fabric-wide global object.
disable Object is local to this security fabric member.
filter Match criteria filter. var-string Maximum
length: 2047
Parameter Description Type Size Default
fqdn Fully Qualified Domain Name address. string Maximum
length: 255
fsso-group
<name>
FSSO group(s).
FSSO group name.
string Maximum
length: 511
hw-model Dynamic address matching hardware model. string Maximum
length: 35
hw-vendor Dynamic address matching hardware vendor. string Maximum
length: 35
interface Name of interface whose IP address is to be
used.
string Maximum
length: 35
macaddr
<macaddr>
Multiple MAC address ranges.
MAC address ranges <start>[-<end>]
separated by space.
string Maximum
length: 127
name Address name. string Maximum
length: 79
node-ip-only Enable/disable collection of node addresses
only in Kubernetes.
option - disable
Option Description
enable Enable collection of node addresses only in Kubernetes.
disable Disable collection of node addresses only in Kubernetes.
obj-id Object ID for NSX. var-string Maximum
length: 255
obj-tag Tag of dynamic address object. string Maximum
length: 255
obj-type Object type. option - ip
Option Description
ip IP address.
mac MAC address
organization Organization domain name (Syntax:
organization/domain).
string Maximum
length: 35
os Dynamic address matching operating system. string Maximum
length: 35
policy-group Policy group name. string Maximum
length: 15
Parameter Description Type Size Default
route-tag route-tag address. integer Minimum
value: 1
Maximum
value:
4294967295
0
sdn SDN. string Maximum
length: 35
sdn-addr-type Type of addresses to collect. option - private
Option Description
private Collect private addresses only.
public Collect public addresses only.
all Collect both public and private addresses.
sdn-tag SDN Tag. string Maximum
length: 15
start-ip First IP address (inclusive) in the range for the
address.
ipv4-
address-
any
Not Specified 0.0.0.0
sub-type Sub-type of address. option - sdn
Option Description
sdn SDN address.
clearpass-spt ClearPass SPT (System Posture Token) address.
fsso FSSO address.
ems-tag FortiClient EMS tag.
fortivoice-tag FortiVoice tag.
fortinac-tag FortiNAC tag.
fortipolicy-tag FortiPolicy tag.
swc-tag Switch Controller NAC policy tag.
device-
identification
Device address.
subnet IP address and subnet mask of address. ipv4-
classnet-
any
Not Specified 0.0.0.0 0.0.0.0
subnet-name Subnet name. string Maximum
length: 255
Parameter Description Type Size Default
sw-version Dynamic address matching software version. string Maximum
length: 35
tag-detection-
level
Tag detection level of dynamic address object. string Maximum
length: 15
tag-type Tag type of dynamic address object. string Maximum
length: 63
tenant Tenant. string Maximum
length: 35
type Type of address. option - ipmask
Option Description
ipmask Standard IPv4 address with subnet mask.
iprange Range of IPv4 addresses between two specified addresses (inclusive).
fqdn Fully Qualified Domain Name address.
geography IP addresses from a specified country.
wildcard Standard IPv4 using a wildcard subnet mask.
dynamic Dynamic address object.
interface-subnet IP and subnet of interface.
mac Range of MAC addresses.
route-tag route-tag addresses.
uuid Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid Not Specified 00000000-0000-
0000-0000-
000000000000
wildcard IP address and wildcard netmask. ipv4-
classnet-
any
Not Specified 0.0.0.0 0.0.0.0
wildcard-fqdn Fully Qualified Domain Name with wildcard
characters.
string Maximum
length: 255
config list
Parameter Description Type Size Default
ip IP. string Maximum
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

```

### config firewall address6-template

Configure IPv6 address templates.

#### Syntax

```text

config firewall address6-template
Description: Configure IPv6 address templates.
edit <name>
set fabric-object [enable|disable]
set ip6 {ipv6-network}
config subnet-segment
Description: IPv6 subnet segments.
edit <id>
set bits {integer}
set exclusive [enable|disable]
set name {string}
config values
Description: Subnet segment values.
edit <name>
set value {string}
next
end
next
end
set subnet-segment-count {integer}
next
end

```

#### Parameters

```text

config firewall address6-template
Parameter Description Type Size Default
fabric-object Security Fabric global object setting. option - disable
Option Description
enable Object is set as a security fabric-wide global object.
disable Object is local to this security fabric member.
```
