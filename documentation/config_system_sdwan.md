# config system sdwan

> Source: `config system sdwan.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

### config system sdn-proxy

Configure SDN proxy.

#### Syntax

config system sdn-proxy
Description: Configure SDN proxy.
edit <name>
set password {password_aes256}
set server {string}
set server-port {integer}
set type [general|fortimanager]
set username {string}
next
end

#### Parameters

config system sdn-proxy
Parameter Description Type Size Default
name SDN proxy name. string Maximum
length: 35
password SDN proxy password. password_
aes256
Not
Specified
server Server address of the SDN proxy. string Maximum
length: 127
server-port Port number of the SDN proxy. integer Minimum
value: 0
Maximum
value:
65535
0
type Type of SDN proxy. option - general
Option Description
general General HTTP proxy.
fortimanager FortiManager SDN proxy.
username SDN proxy username. string Maximum
length: 64

### config system sdwan

Configure redundant Internet connections with multiple outbound links and health-check profiles.

#### Syntax

config system sdwan
Description: Configure redundant Internet connections with multiple outbound links and
health-check profiles.
set app-perf-log-period {integer}
config duplication
Description: Create SD-WAN duplication rule.
edit <id>
set dstaddr <name1>, <name2>, ...
set dstaddr6 <name1>, <name2>, ...
set dstintf <name1>, <name2>, ...
set packet-de-duplication [enable|disable]
set packet-duplication [disable|force|...]
set service <name1>, <name2>, ...
set service-id <id1>, <id2>, ...
set sla-match-service [enable|disable]
set srcaddr <name1>, <name2>, ...
set srcaddr6 <name1>, <name2>, ...
set srcintf <name1>, <name2>, ...
next
end
set duplication-max-num {integer}
set fail-alert-interfaces <name1>, <name2>, ...
set fail-detect [enable|disable]
config health-check
Description: SD-WAN status checking or health checking. Identify a server on the
Internet and determine how SD-WAN verifies that the FortiGate can communicate with it.
edit <name>
set addr-mode [ipv4|ipv6]
set class-id {integer}
set detect-mode [active|passive|...]
set diffservcode {user}
set dns-match-ip {ipv4-address}
set dns-request-domain {string}
set embed-measured-health [enable|disable]
set failtime {integer}
set ftp-file {string}
set ftp-mode [passive|port]
set ha-priority {integer}
set http-agent {string}
set http-get {string}
set http-match {string}
set interval {integer}
set members <seq-num1>, <seq-num2>, ...
set mos-codec [g711|g722|...]
set packet-size {integer}
set password {password}
set port {integer}
set probe-count {integer}
set probe-packets [disable|enable]
set probe-timeout {integer}
set protocol [ping|tcp-echo|...]
set quality-measured-method [half-open|half-close]
set recoverytime {integer}
set security-mode [none|authentication]
set server {string}
config sla
Description: Service level agreement (SLA).
edit <id>
set jitter-threshold {integer}
set latency-threshold {integer}
set link-cost-factor {option1}, {option2}, ...
set mos-threshold {string}
set packetloss-threshold {integer}
set priority-in-sla {integer}
set priority-out-sla {integer}
next
end
set sla-fail-log-period {integer}
set sla-id-redistribute {integer}
set sla-pass-log-period {integer}
set source {ipv4-address}
set source6 {ipv6-address}
set system-dns [disable|enable]
set threshold-alert-jitter {integer}
set threshold-alert-latency {integer}
set threshold-alert-packetloss {integer}
set threshold-warning-jitter {integer}
set threshold-warning-latency {integer}
set threshold-warning-packetloss {integer}
set update-cascade-interface [enable|disable]
set update-static-route [enable|disable]
set user {string}
set vrf {integer}
next
end
set load-balance-mode [source-ip-based|weight-based|...]
config members
Description: FortiGate interfaces added to the SD-WAN.
edit <seq-num>
set comment {var-string}
set cost {integer}
set gateway {ipv4-address}
set gateway6 {ipv6-address}
set ingress-spillover-threshold {integer}
set interface {string}
set preferred-source {ipv4-address}
set priority {integer}
set priority6 {integer}
set source {ipv4-address}
set source6 {ipv6-address}
set spillover-threshold {integer}
set status [disable|enable]
set transport-group {integer}
set volume-ratio {integer}
set weight {integer}
set zone {string}
next
end
config neighbor
Description: Create SD-WAN neighbor from BGP neighbor table to control route
advertisements according to SLA status.
edit <ip>
set health-check {string}
set member <seq-num1>, <seq-num2>, ...
set minimum-sla-meet-members {integer}
set mode [sla|speedtest]
set role [standalone|primary|...]
set service-id {integer}
set sla-id {integer}
next
end
set neighbor-hold-boot-time {integer}
set neighbor-hold-down [enable|disable]
set neighbor-hold-down-time {integer}
config service
Description: Create SD-WAN rules (also called services) to control how sessions are
distributed to interfaces in the SD-WAN.
edit <id>
set addr-mode [ipv4|ipv6]
set agent-exclusive [enable|disable]
set bandwidth-weight {integer}
set default [enable|disable]
set dscp-forward [enable|disable]
set dscp-forward-tag {user}
set dscp-reverse [enable|disable]
set dscp-reverse-tag {user}
set dst <name1>, <name2>, ...
set dst-negate [enable|disable]
set dst6 <name1>, <name2>, ...
set end-port {integer}
set end-src-port {integer}
set gateway [enable|disable]
set groups <name1>, <name2>, ...
set hash-mode [round-robin|source-ip-based|...]
set health-check <name1>, <name2>, ...
set hold-down-time {integer}
set input-device <name1>, <name2>, ...
set input-device-negate [enable|disable]
set input-zone <name1>, <name2>, ...
set internet-service [enable|disable]
set internet-service-app-ctrl <id1>, <id2>, ...
set internet-service-app-ctrl-category <id1>, <id2>, ...
set internet-service-app-ctrl-group <name1>, <name2>, ...
set internet-service-custom <name1>, <name2>, ...
set internet-service-custom-group <name1>, <name2>, ...
set internet-service-group <name1>, <name2>, ...
set internet-service-name <name1>, <name2>, ...
set jitter-weight {integer}
set latency-weight {integer}
set link-cost-factor [latency|jitter|...]
set link-cost-threshold {integer}
set load-balance [enable|disable]
set minimum-sla-meet-members {integer}
set mode [auto|manual|...]
set name {string}
set packet-loss-weight {integer}
set passive-measurement [enable|disable]
set priority-members <seq-num1>, <seq-num2>, ...
set priority-zone <name1>, <name2>, ...
set protocol {integer}
set quality-link {integer}
set role [standalone|primary|...]
set shortcut [enable|disable]
set shortcut-priority [enable|disable|...]
config sla
Description: Service level agreement (SLA).
edit <health-check>
set id {integer}
next
end
set sla-compare-method [order|number]
set sla-stickiness [enable|disable]
set src <name1>, <name2>, ...
set src-negate [enable|disable]
set src6 <name1>, <name2>, ...
set standalone-action [enable|disable]
set start-port {integer}
set start-src-port {integer}
set status [enable|disable]
set tie-break [zone|cfg-order|...]
set tos {user}
set tos-mask {user}
set use-shortcut-sla [enable|disable]
set users <name1>, <name2>, ...
set zone-mode [enable|disable]
next
end
set speedtest-bypass-routing [disable|enable]
set status [disable|enable]
config zone
Description: Configure SD-WAN zones.
edit <name>
set advpn-health-check {string}
set advpn-select [enable|disable]
set minimum-sla-meet-members {integer}
set service-sla-tie-break [cfg-order|fib-best-match|...]
next
end
end

#### Parameters

config system sdwan
Parameter Description Type Size Default
app-perf-log-
period
Time interval in seconds that application performance
logs are generated.
integer Minimum
value: 0
Maximum
value: 3600
0
duplication-
max-num
Maximum number of interface members a packet is
duplicated in the SD-WAN zone.
integer Minimum
value: 2
Maximum
value: 4
2
fail-alert-
interfaces
<name>
Physical interfaces that will be alerted.
Physical interface name.
string Maximum
length: 79
fail-detect Enable/disable SD-WAN Internet connection status
checking (failure detection).
option - disable
Parameter Description Type Size Default
Option Description
enable Enable status checking.
disable Disable status checking.
load-balance-
mode
Algorithm or mode to use for load balancing Internet
traffic to SD-WAN members.
option - source-ip-
based
Option Description
source-ip-based Source IP load balancing. All traffic from a source IP is sent to the same
interface.
weight-based Weight-based load balancing. Interfaces with higher weights have higher
priority and get more traffic.
usage-based Usage-based load balancing. All traffic is sent to the first interface on the list.
When the bandwidth on that interface exceeds the spill-over limit new traffic is
sent to the next interface.
source-dest-ip-
based
Source and destination IP load balancing. All traffic from a source IP to a
destination IP is sent to the same interface.
measured-
volume-based
Volume-based load balancing. Traffic is load balanced based on traffic volume
(in bytes). More traffic is sent to interfaces with higher volume ratios.
neighbor-
hold-boot-
time
Waiting period in seconds when switching from the
primary neighbor to the secondary neighbor from the
neighbor start.
integer Minimum
value: 0
Maximum
value:
10000000
0
neighbor-
hold-down
Enable/disable hold switching from the secondary
neighbor to the primary neighbor.
option - disable
Option Description
enable Enable hold switching from the secondary neighbor to the primary neighbor.
disable Disable hold switching from the secondary neighbor to the primary neighbor.
neighbor-
hold-down-
time
Waiting period in seconds when switching from the
secondary neighbor to the primary neighbor when hold-
down is disabled.
integer Minimum
value: 0
Maximum
value:
10000000
0
speedtest-
bypass-
routing
Enable/disable bypass routing when speedtest on a
SD-WAN member.
option - disable
Parameter Description Type Size Default
Option Description
disable Disable SD-WAN.
enable Enable SD-WAN.
status Enable/disable SD-WAN. option - disable
Option Description
disable Disable SD-WAN.
enable Enable SD-WAN.
config duplication
Parameter Description Type Size Default
dstaddr
<name>
Destination address or address group names.
Address or address group name.
string Maximum
length: 79
dstaddr6
<name>
Destination address6 or address6 group names.
Address6 or address6 group name.
string Maximum
length: 79
dstintf
<name>
Outgoing (egress) interfaces or zones.
Interface, zone or SDWAN zone name.
string Maximum
length: 79
id Duplication rule ID. integer Minimum
value: 1
Maximum
value: 255
0
packet-de-
duplication
Enable/disable discarding of packets that have been
duplicated.
option - disable
Option Description
enable Enable discarding of packets that have been duplicated.
disable Disable discarding of packets that have been duplicated.
packet-
duplication
Configure packet duplication method. option - disable
Option Description
disable Disable packet duplication.
force Duplicate packets across all interface members of the SD-WAN zone.
on-demand Duplicate packets across all interface members of the SD-WAN zone based
on the link quality.
Parameter Description Type Size Default
service
<name>
Service and service group name.
Service and service group name.
string Maximum
length: 79
service-id
<id>
SD-WAN service rule ID list.
SD-WAN service rule ID.
integer Minimum
value: 0
Maximum
value:
4294967295
sla-match-
service
Enable/disable packet duplication matching health-
check SLAs in service rule.
option - disable
Option Description
enable Enable packet duplication matching health-check SLAs in service rule
(matching all SLAs of current defined service).
disable Disable packet duplication matching health-check SLAs in service rule
(matching all SLAs of all defined health-check).
srcaddr
<name>
Source address or address group names.
Address or address group name.
string Maximum
length: 79
srcaddr6
<name>
Source address6 or address6 group names.
Address6 or address6 group name.
string Maximum
length: 79
srcintf
<name>
Incoming (ingress) interfaces or zones.
Interface, zone or SDWAN zone name.
string Maximum
length: 79
config health-check
Parameter Description Type Size Default
addr-mode Address mode (IPv4 or IPv6). option - ipv4
Option Description
ipv4 IPv4 mode.
ipv6 IPv6 mode.
class-id Traffic class ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
detect-mode The mode determining how to detect the
server.
option - active
Parameter Description Type Size Default
Option Description
active The probes are sent actively.
passive The traffic measures health without probes.
prefer-passive The probes are sent in case of no new traffic.
remote Link health obtained from remote peers.
agent-based Traffic health is measured from the fabric connectors.
diffservcode Differentiated services code point (DSCP)
in the IP header of the probe packet.
user Not Specified
dns-match-ip Response IP expected from DNS server if
the protocol is DNS.
ipv4-
address
Not Specified 0.0.0.0
dns-request-
domain
Fully qualified domain name to resolve for
the DNS probe.
string Maximum
length: 255
www.example.com
embed-
measured-
health
Enable/disable embedding measured
health information.
option - disable
Option Description
enable Enable embed measured health.
disable Disable embed measured health.
failtime Number of failures before server is
considered lost.
integer Minimum
value: 1
Maximum
value: 3600
5
ftp-file Full path and file name on the FTP server
to download for FTP health-check to
probe.
string Maximum
length: 254
ftp-mode FTP mode. option - passive
Option Description
passive The FTP health-check initiates and establishes the data connection.
port The FTP server initiates and establishes the data connection.
ha-priority HA election priority. integer Minimum
value: 1
Maximum
value: 50
1
Parameter Description Type Size Default
http-agent String in the http-agent field in the HTTP
header.
string Maximum
length: 1024
Chrome/ Safari/
http-get URL used to communicate with the server
if the protocol if the protocol is HTTP.
string Maximum
length: 1024
/
http-match Response string expected from the server
if the protocol is HTTP.
string Maximum
length: 1024
interval Status check interval in milliseconds, or
the time between attempting to connect to
the server.
integer Minimum
value: 20
Maximum
value:
3600000
500
members
<seq-num>
Member sequence number list.
Member sequence number.
integer Minimum
value: 0
Maximum
value:
4294967295
mos-codec Codec to use for MOS calculation. option - g711
Option Description
g711 Calculate MOS based on the G.711 codec.
g722 Calculate MOS based on the G.722 codec.
g729 Calculate MOS based on the G.729 codec.
name Status check or health check name. string Maximum
length: 35
packet-size Packet size of a TWAMP test session. integer Minimum
value: 0
Maximum
value: 65535
124
password TWAMP controller password in
authentication mode.
password Not Specified
port Port number used to communicate with
the server over the selected protocol.
integer Minimum
value: 0
Maximum
value: 65535
0
probe-count Number of most recent probes that should
be used to calculate latency and jitter.
integer Minimum
value: 5
Maximum
value: 30
30
Parameter Description Type Size Default
probe-packets Enable/disable transmission of probe
packets.
option - enable
Option Description
disable Disable transmission of probe packets.
enable Enable transmission of probe packets.
probe-timeout Time to wait before a probe packet is
considered lost.
integer Minimum
value: 20
Maximum
value:
3600000
500
protocol Protocol used to determine if the
FortiGate can communicate with the
server.
option - ping
Option Description
ping Use PING to test the link with the server.
tcp-echo Use TCP echo to test the link with the server.
udp-echo Use UDP echo to test the link with the server.
http Use HTTP-GET to test the link with the server.
https Use HTTPS-GET to test the link with the server.
twamp Use TWAMP to test the link with the server.
dns Use DNS query to test the link with the server.
tcp-connect Use a full TCP connection to test the link with the server.
ftp Use FTP to test the link with the server.
quality-
measured-
method
Method to measure the quality of tcp-
connect.
option - half-open
Option Description
half-open Measure the round trip between syn and ack.
half-close Measure the round trip between fin and ack.
recoverytime Number of successful responses received
before server is considered recovered.
integer Minimum
value: 1
Maximum
value: 3600
5
security-mode Twamp controller security mode. option - none
Parameter Description Type Size Default
Option Description
none Unauthenticated mode.
authentication Authenticated mode.
server IP address or FQDN name of the server. string Maximum
length: 79
sla-fail-log-
period
Time interval in seconds that SLA fail log
messages will be generated.
integer Minimum
value: 0
Maximum
value: 3600
0
sla-id-
redistribute
Select the ID from the SLA sub-table. The
selected SLA's priority value will be
distributed into the routing table.
integer Minimum
value: 0
Maximum
value: 32
0
sla-pass-log-
period
Time interval in seconds that SLA pass
log messages will be generated.
integer Minimum
value: 0
Maximum
value: 3600
0
source Source IP address used in the health-
check packet to the server.
ipv4-
address
Not Specified 0.0.0.0
source6 Source IPv6 address used in the health-
check packet to server.
ipv6-
address
Not Specified ::
system-dns Enable/disable system DNS as the probe
server.
option - disable
Option Description
disable Disable system DNS as the probe server.
enable Enable system DNS as the probe server.
threshold-alert-
jitter
Alert threshold for jitter. integer Minimum
value: 0
Maximum
value:
4294967295
0
threshold-alert-
latency
Alert threshold for latency. integer Minimum
value: 0
Maximum
value:
4294967295
0
Parameter Description Type Size Default
threshold-alert-
packetloss
Alert threshold for packet loss. integer Minimum
value: 0
Maximum
value: 100
0
threshold-
warning-jitter
Warning threshold for jitter. integer Minimum
value: 0
Maximum
value:
4294967295
0
threshold-
warning-
latency
Warning threshold for latency. integer Minimum
value: 0
Maximum
value:
4294967295
0
threshold-
warning-
packetloss
Warning threshold for packet loss. integer Minimum
value: 0
Maximum
value: 100
0
update-
cascade-
interface
Enable/disable update cascade interface. option - enable
Option Description
enable Enable update cascade interface.
disable Disable update cascade interface.
update-static-
route
Enable/disable updating the static route. option - enable
Option Description
enable Enable updating the static route.
disable Disable updating the static route.
user The user name to access probe server. string Maximum
length: 64
vrf Virtual Routing Forwarding ID. integer Minimum
value: 0
Maximum
value: 251
0
config sla
Parameter Description Type Size Default
health-check SD-WAN health-check. string Maximum
length: 35
id SLA ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
config members
Parameter Description Type Size Default
comment Comments. var-string Maximum
length: 255
cost Cost of this interface for services in SLA mode. integer Minimum
value: 0
Maximum
value:
4294967295
0
gateway The default gateway for this interface. Usually the
default gateway of the Internet service provider that
this interface is connected to.
ipv4-
address
Not Specified 0.0.0.0
gateway6 IPv6 gateway. ipv6-
address
Not Specified ::
ingress-
spillover-
threshold
Ingress spillover threshold for this interface. When
this traffic volume threshold is reached, new sessions
spill over to other interfaces in the SD-WAN.
integer Minimum
value: 0
Maximum
value:
16776000
0
interface Interface name. string Maximum
length: 15
preferred-
source
Preferred source of route for this member. ipv4-
address
Not Specified 0.0.0.0
priority Priority of the interface for IPv4. Used for SD-WAN
rules or priority rules.
integer Minimum
value: 1
Maximum
value: 65535
1
Parameter Description Type Size Default
priority6 Priority of the interface for IPv6. Used for SD-WAN
rules or priority rules.
integer Minimum
value: 1
Maximum
value: 65535
1024
seq-num Sequence number. integer Minimum
value: 0
Maximum
value: 512
0
source Source IP address used in the health-check packet to
the server.
ipv4-
address
Not Specified 0.0.0.0
source6 Source IPv6 address used in the health-check packet
to the server.
ipv6-
address
Not Specified ::
spillover-
threshold
Egress spillover threshold for this interface. When
this traffic volume threshold is reached, new sessions
spill over to other interfaces in the SD-WAN.
integer Minimum
value: 0
Maximum
value:
16776000
0
status Enable/disable this interface in the SD-WAN. option - enable
Option Description
disable Disable this interface in the SD-WAN.
enable Enable this interface in the SD-WAN.
transport-
group
Measured transport group. integer Minimum
value: 0
Maximum
value: 255
0
volume-ratio Measured volume ratio. integer Minimum
value: 1
Maximum
value: 255
1
weight Weight of this interface for weighted load balancing.
More traffic is directed to interfaces with higher
weights.
integer Minimum
value: 1
Maximum
value: 255
1
zone Zone name. string Maximum
length: 35
virtual-wan-
link
config neighbor
Parameter Description Type Size Default
health-check SD-WAN health-check name. string Maximum
length: 35
ip IP/IPv6 address of neighbor or neighbor-group
name.
string Maximum
length: 45
member
<seq-num>
Member sequence number list.
Member sequence number.
integer Minimum
value: 0
Maximum
value:
4294967295
minimum-sla-
meet-
members
Minimum number of members which meet SLA
when the neighbor is preferred.
integer Minimum
value: 1
Maximum
value: 255
1
mode What metric to select the neighbor. option - sla
Option Description
sla Select neighbor based on SLA link quality.
speedtest Select neighbor based on the speedtest status.
role Role of neighbor. option - standalone
Option Description
standalone Standalone neighbor.
primary Primary neighbor.
secondary Secondary neighbor.
service-id SD-WAN service ID to work with the neighbor. integer Minimum
value: 0
Maximum
value:
4294967295
0
sla-id SLA ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
config service
Parameter Description Type Size Default
addr-mode Address mode (IPv4 or IPv6). option - ipv4
Option Description
ipv4 IPv4 mode.
ipv6 IPv6 mode.
agent-exclusive Set/unset the service as agent use exclusively. option - disable
Option Description
enable Set the service as agent use exclusively.
disable Unset the service as agent use exclusively.
bandwidth-
weight
Coefficient of reciprocal of available bidirectional
bandwidth in the formula of custom-profile-1.
integer Minimum
value: 0
Maximum
value:
10000000
0
default Enable/disable use of SD-WAN as default service. option - disable
Option Description
enable Enable use of SD-WAN as default service.
disable Disable use of SD-WAN as default service.
dscp-forward Enable/disable forward traffic DSCP tag. option - disable
Option Description
enable Enable use of forward DSCP tag.
disable Disable use of forward DSCP tag.
dscp-forward-
tag
Forward traffic DSCP tag. user Not Specified
dscp-reverse Enable/disable reverse traffic DSCP tag. option - disable
Option Description
enable Enable use of reverse DSCP tag.
disable Disable use of reverse DSCP tag.
dscp-reverse-
tag
Reverse traffic DSCP tag. user Not Specified
Parameter Description Type Size Default
dst <name> Destination address name.
Address or address group name.
string Maximum
length: 79
dst-negate Enable/disable negation of destination address
match.
option - disable
Option Description
enable Enable destination address negation.
disable Disable destination address negation.
dst6 <name> Destination address6 name.
Address6 or address6 group name.
string Maximum
length: 79
end-port End destination port number. integer Minimum
value: 0
Maximum
value: 65535
65535
end-src-port End source port number. integer Minimum
value: 0
Maximum
value: 65535
65535
gateway Enable/disable SD-WAN service gateway. option - disable
Option Description
enable Enable SD-WAN service gateway.
disable Disable SD-WAN service gateway.
groups <name> User groups.
Group name.
string Maximum
length: 79
hash-mode Hash algorithm for selected priority members for
load balance mode.
option - round-robin
Option Description
round-robin All traffic are distributed to selected interfaces in equal portions and circular
order.
source-ip-based All traffic from a source IP is sent to the same interface.
source-dest-ip-
based
All traffic from a source IP to a destination IP is sent to the same interface.
inbandwidth All traffic are distributed to a selected interface with most available
bandwidth for incoming traffic.
Parameter Description Type Size Default
Option Description
outbandwidth All traffic are distributed to a selected interface with most available
bandwidth for outgoing traffic.
bibandwidth All traffic are distributed to a selected interface with most available
bandwidth for both incoming and outgoing traffic.
health-check
<name>
Health check list.
Health check name.
string Maximum
length: 79
hold-down-time Waiting period in seconds when switching from
the back-up member to the primary member.
integer Minimum
value: 0
Maximum
value:
10000000
0
id SD-WAN rule ID. integer Minimum
value: 1
Maximum
value: 4000
0
input-device
<name>
Source interface name.
Interface name.
string Maximum
length: 79
input-device-
negate
Enable/disable negation of input device match. option - disable
Option Description
enable Enable negation of input device match.
disable Disable negation of input device match.
input-zone
<name>
Source input-zone name.
Zone.
string Maximum
length: 79
internet-service Enable/disable use of Internet service for
application-based load balancing.
option - disable
Option Description
enable Enable cloud service to support application-based load balancing.
disable Disable cloud service to support application-based load balancing.
internet-service-
app-ctrl <id>
Application control based Internet Service ID list.
Application control based Internet Service ID.
integer Minimum
value: 0
Maximum
value:
4294967295
Parameter Description Type Size Default
internet-service-
app-ctrl-
category <id>
IDs of one or more application control categories.
Application control category ID.
integer Minimum
value: 0
Maximum
value:
4294967295
internet-service-
app-ctrl-group
<name>
Application control based Internet Service group
list.
Application control based Internet Service group
name.
string Maximum
length: 79
internet-service-
custom <name>
Custom Internet service name list.
Custom Internet service name.
string Maximum
length: 79
internet-service-
custom-group
<name>
Custom Internet Service group list.
Custom Internet Service group name.
string Maximum
length: 79
internet-service-
group <name>
Internet Service group list.
Internet Service group name.
string Maximum
length: 79
internet-service-
name <name>
Internet service name list.
Internet service name.
string Maximum
length: 79
jitter-weight Coefficient of jitter in the formula of custom-profile-
1.
integer Minimum
value: 0
Maximum
value:
10000000
0
latency-weight Coefficient of latency in the formula of custom-
profile-1.
integer Minimum
value: 0
Maximum
value:
10000000
0
link-cost-factor Link cost factor. option - latency
Option Description
latency Select link based on latency.
jitter Select link based on jitter.
packet-loss Select link based on packet loss.
inbandwidth Select link based on available bandwidth of incoming traffic.
outbandwidth Select link based on available bandwidth of outgoing traffic.
bibandwidth Select link based on available bandwidth of bidirectional traffic.
custom-profile-1 Select link based on customized profile.
Parameter Description Type Size Default
link-cost-
threshold
Percentage threshold change of link cost values
that will result in policy route regeneration.
integer Minimum
value: 0
Maximum
value:
10000000
10
load-balance Enable/disable load-balance. option - disable
Option Description
enable Enable load-balance.
disable Disable load-balance.
minimum-sla-
meet-members
Minimum number of members which meet SLA. integer Minimum
value: 0
Maximum
value: 255
0
mode Control how the SD-WAN rule sets the priority of
interfaces in the SD-WAN.
option - manual
Option Description
auto Assign interfaces a priority based on quality.
manual Assign interfaces a priority manually.
priority Assign interfaces a priority based on the link-cost-factor quality of the
interface.
sla Assign interfaces a priority based on selected SLA settings.
name SD-WAN rule name. string Maximum
length: 35
packet-loss-
weight
Coefficient of packet-loss in the formula of
custom-profile-1.
integer Minimum
value: 0
Maximum
value:
10000000
0
passive-
measurement
Enable/disable passive measurement based on
the service criteria.
option - disable
Option Description
enable Enable passive measurement of user traffic.
disable Disable passive measurement of user traffic.
Parameter Description Type Size Default
priority-
members
<seq-num>
Member sequence number list.
Member sequence number.
integer Minimum
value: 0
Maximum
value:
4294967295
priority-zone
<name>
Priority zone name list.
Priority zone name.
string Maximum
length: 79
protocol Protocol number. integer Minimum
value: 0
Maximum
value: 255
0
quality-link Quality grade. integer Minimum
value: 0
Maximum
value: 255
0
role Service role to work with neighbor. option - standalone
Option Description
standalone Standalone service.
primary Primary service for primary neighbor.
secondary Secondary service for secondary neighbor.
shortcut Enable/disable shortcut for this service. option - enable
Option Description
enable Enable use of ADVPN shortcut for this service.
disable Disable use of ADVPN shortcut for this service.
shortcut-priority High priority of ADVPN shortcut for this service. option - auto
Option Description
enable Enable a high priority of ADVPN shortcut for this service.
disable Disable a high priority of ADVPN shortcut for this service.
auto Auto enable a high priority of ADVPN shortcut for this service if ADVPN2.0
enabled.
sla-compare-
method
Method to compare SLA value for SLA mode. option - order
Parameter Description Type Size Default
Option Description
order Compare SLA value based on the order of health-check.
number Compare SLA value based on the number of satisfied health-check. Limits
health-checks to only configured member interfaces.
sla-stickiness Enable/disable SLA stickiness. option - disable
Option Description
enable Traffic remains in the original session path if the path is within the SLA.
disable Traffic switches to the best path regardless of the SLA.
src <name> Source address name.
Address or address group name.
string Maximum
length: 79
src-negate Enable/disable negation of source address match. option - disable
Option Description
enable Enable source address negation.
disable Disable source address negation.
src6 <name> Source address6 name.
Address6 or address6 group name.
string Maximum
length: 79
standalone-
action
Enable/disable service when selected neighbor
role is standalone while service role is not
standalone.
option - disable
Option Description
enable Enable service when selected neighbor role is standalone.
disable Disable service when selected neighbor role is standalone.
start-port Start destination port number. integer Minimum
value: 0
Maximum
value: 65535
1
start-src-port Start source port number. integer Minimum
value: 0
Maximum
value: 65535
1
status Enable/disable SD-WAN service. option - enable
Parameter Description Type Size Default
Option Description
enable Enable SD-WAN service.
disable Disable SD-WAN service.
tie-break Method of selecting member if more than one
meets the SLA.
option - zone
Option Description
zone Use the setting that is configured for the members' zone.
cfg-order Members that meet the SLA are selected in the order they are configured.
fib-best-match Members that meet the SLA are selected that match the longest prefix in the
routing table.
input-device Members that meet the SLA are selected by matching the input device.
tos Type of service bit pattern. user Not Specified
tos-mask Type of service evaluated bits. user Not Specified
use-shortcut-sla Enable/disable use of ADVPN shortcut for quality
comparison.
option - enable
Option Description
enable Enable use of ADVPN shortcut for quality comparison.
disable Disable use of ADVPN shortcut for quality comparison.
users <name> User name.
User name.
string Maximum
length: 79
zone-mode Enable/disable zone mode. option - disable
Option Description
enable Traffic steered based on zone.
disable Traffic steered based on member.
config sla
Parameter Description Type Size Default
health-check SD-WAN health-check. string Maximum
length: 35
Parameter Description Type Size Default
id SLA ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
config zone
Parameter Description Type Size Default
advpn-health-
check
Health check for ADVPN local overlay link quality. string Maximum
length: 35
advpn-select Enable/disable selection of ADVPN based on SDWAN
information.
option - disable
Option Description
enable Enable selection of ADVPN based on SDWAN information.
disable Disable selection of ADVPN based on SDWAN information.
minimum-sla-
meet-
members
Minimum number of members which meet SLA when
the neighbor is preferred.
integer Minimum
value: 1
Maximum
value: 255
1
name Zone name. string Maximum
length: 35
service-sla-
tie-break
Method of selecting member if more than one meets the
SLA.
option - cfg-order
Option Description
cfg-order Members that meet the SLA are selected in the order they are configured.
fib-best-match Members that meet the SLA are selected that match the longest prefix in the
routing table.
input-device Members that meet the SLA are selected by matching the input device.

### config system serial-port

This command is available for model(s): FortiGateRugged 70F.
It is not available for: FortiGate 1000D, FortiGate 1000F, FortiGate 1001F, FortiGate 100F,
FortiGate 101F, FortiGate 1100E, FortiGate 1101E, FortiGate 120G, FortiGate 121G,
FortiGate 140E-POE, FortiGate 140E, FortiGate 1800F, FortiGate 1801F, FortiGate 2000E,
FortiGate 200E, FortiGate 200F, FortiGate 201E, FortiGate 201F, FortiGate 2200E, FortiGate
2201E, FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate 3000D, FortiGate
3000F, FortiGate 3001F, FortiGate 300E, FortiGate 301E, FortiGate 3100D, FortiGate 3200D,
FortiGate 3200F, FortiGate 3201F, FortiGate 3300E, FortiGate 3301E, FortiGate 3400E,
FortiGate 3401E, FortiGate 3500F, FortiGate 3501F, FortiGate 3600E, FortiGate 3601E,
FortiGate 3700D, FortiGate 3700F, FortiGate 3701F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 401E, FortiGate 401F,
FortiGate 4200F, FortiGate 4201F, FortiGate 4400F, FortiGate 4401F, FortiGate 5001E1,
FortiGate 5001E, FortiGate 500E, FortiGate 501E, FortiGate 600E, FortiGate 600F, FortiGate
601E, FortiGate 601F, FortiGate 60E DSLJ, FortiGate 60E DSL, FortiGate 60E-POE,
FortiGate 60E, FortiGate 61E, FortiGate 800D, FortiGate 80E-POE, FortiGate 80E, FortiGate
80F DSL, FortiGate 81E-POE, FortiGate 81E, FortiGate 900D, FortiGate 900G, FortiGate
901G, FortiGate 90E, FortiGate 90G, FortiGate 91E, FortiGate 91G, FortiGate-VM for Aliyun,
FortiGate-VM for AWS, FortiGate-VM for Azure, FortiGate-VM for GCP, FortiGate-VM for
OPC, FortiGate-VM64, FortiWiFi 60E DSLJ, FortiWiFi 60E DSL, FortiWiFi 60E, FortiWiFi 61E,
FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 81F 2R 3G4G DSL.
Serial port list. Read-only.

#### Syntax

config system serial-port
Description: Serial port list. Read-only.
edit <name>
next
end

#### Parameters

config system serial-port
Parameter Description Type Size Default
name Serial port name. string Maximum
length: 35

### config system session-helper

Configure session helper.

#### Syntax

config system session-helper
Description: Configure session helper.
edit <id>
set name [ftp|tftp|...]
set port {integer}
set protocol {integer}
