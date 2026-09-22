# config vpn phase 1 and 2

> Source: `config vpn phase 1 and 2.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
npu-offload * Enable/disable NPU offloading. option - enable
Option Description
enable Enable NPU offloading.
disable Disable NPU offloading.
remote-gw Peer gateway. ipv4-
address
Not
Specified
0.0.0.0
remotespi Remote SPI, a hexadecimal 8-digit (4-byte) tag.
Discerns between two traffic streams with different
encryption rules.
user Not
Specified
- This parameter may not exist in some models.

### config vpn ipsec phase1-interface

Configure VPN remote gateway.

#### Syntax

config vpn ipsec phase1-interface
Description: Configure VPN remote gateway.
edit <name>
set acct-verify [enable|disable]
set add-gw-route [enable|disable]
set add-route [disable|enable]
set aggregate-member [enable|disable]
set aggregate-weight {integer}
set assign-ip [disable|enable]
set assign-ip-from [range|usrgrp|...]
set authmethod [psk|signature]
set authmethod-remote [psk|signature]
set authpasswd {password}
set authusr {string}
set authusrgrp {string}
set auto-discovery-crossover [allow|block]
set auto-discovery-forwarder [enable|disable]
set auto-discovery-offer-interval {integer}
set auto-discovery-psk [enable|disable]
set auto-discovery-receiver [enable|disable]
set auto-discovery-sender [enable|disable]
set auto-discovery-shortcuts [independent|dependent]
set auto-negotiate [enable|disable]
set azure-ad-autoconnect [enable|disable]
set backup-gateway <address1>, <address2>, ...
set banner {var-string}
set cert-id-validation [enable|disable]
set cert-peer-username-strip [disable|enable]
set cert-peer-username-validation [none|othername|...]
set cert-trust-store [local|ems]
set certificate <name1>, <name2>, ...
set childless-ike [enable|disable]
set client-auto-negotiate [disable|enable]
set client-keep-alive [disable|enable]
set client-resume [enable|disable]
set client-resume-interval {integer}
set comments {var-string}
set default-gw {ipv4-address}
set default-gw-priority {integer}
set dev-id {string}
set dev-id-notification [disable|enable]
set dhcp-ra-giaddr {ipv4-address}
set dhcp6-ra-linkaddr {ipv6-address}
set dhgrp {option1}, {option2}, ...
set digital-signature-auth [enable|disable]
set distance {integer}
set dns-mode [manual|auto]
set domain {string}
set dpd [disable|on-idle|...]
set dpd-retrycount {integer}
set dpd-retryinterval {user}
set eap [enable|disable]
set eap-cert-auth [enable|disable]
set eap-exclude-peergrp {string}
set eap-identity [use-id-payload|send-request]
set ems-sn-check [enable|disable]
set encap-local-gw4 {ipv4-address}
set encap-local-gw6 {ipv6-address}
set encap-remote-gw4 {ipv4-address}
set encap-remote-gw6 {ipv6-address}
set encapsulation [none|gre|...]
set encapsulation-address [ike|ipv4|...]
set enforce-unique-id [disable|keep-new|...]
set esn [require|allow|...]
set exchange-fgt-device-id [enable|disable]
set exchange-interface-ip [enable|disable]
set exchange-ip-addr4 {ipv4-address}
set exchange-ip-addr6 {ipv6-address}
set fallback-tcp-threshold {integer}
set fec-base {integer}
set fec-codec [rs|xor]
set fec-egress [enable|disable]
set fec-health-check {string}
set fec-ingress [enable|disable]
set fec-mapping-profile {string}
set fec-receive-timeout {integer}
set fec-redundant {integer}
set fec-send-timeout {integer}
set fgsp-sync [enable|disable]
set fortinet-esp [enable|disable]
set fragmentation [enable|disable]
set fragmentation-mtu {integer}
set group-authentication [enable|disable]
set group-authentication-secret {password-3}
set ha-sync-esp-seqno [enable|disable]
set idle-timeout [enable|disable]
set idle-timeoutinterval {integer}
set ike-version [1|2]
set inbound-dscp-copy [enable|disable]
set include-local-lan [disable|enable]
set interface {string}
set internal-domain-list <domain-name1>, <domain-name2>, ...
set ip-delay-interval {integer}
set ip-fragmentation [pre-encapsulation|post-encapsulation]
set ip-version [4|6]
set ipv4-dns-server1 {ipv4-address}
set ipv4-dns-server2 {ipv4-address}
set ipv4-dns-server3 {ipv4-address}
set ipv4-end-ip {ipv4-address}
config ipv4-exclude-range
Description: Configuration Method IPv4 exclude ranges.
edit <id>
set end-ip {ipv4-address}
set start-ip {ipv4-address}
next
end
set ipv4-name {string}
set ipv4-netmask {ipv4-netmask}
set ipv4-split-exclude {string}
set ipv4-split-include {string}
set ipv4-start-ip {ipv4-address}
set ipv4-wins-server1 {ipv4-address}
set ipv4-wins-server2 {ipv4-address}
set ipv6-dns-server1 {ipv6-address}
set ipv6-dns-server2 {ipv6-address}
set ipv6-dns-server3 {ipv6-address}
set ipv6-end-ip {ipv6-address}
config ipv6-exclude-range
Description: Configuration method IPv6 exclude ranges.
edit <id>
set end-ip {ipv6-address}
set start-ip {ipv6-address}
next
end
set ipv6-name {string}
set ipv6-prefix {integer}
set ipv6-split-exclude {string}
set ipv6-split-include {string}
set ipv6-start-ip {ipv6-address}
set keepalive {integer}
set keylife {integer}
set kms {string}
set link-cost {integer}
set local-gw {ipv4-address}
set local-gw6 {ipv6-address}
set localid {string}
set localid-type [auto|fqdn|...]
set loopback-asymroute [enable|disable]
set mesh-selector-type [disable|subnet|...]
set mode [aggressive|main]
set mode-cfg [disable|enable]
set mode-cfg-allow-client-selector [disable|enable]
set monitor <name1>, <name2>, ...
set monitor-hold-down-delay {integer}
set monitor-hold-down-time {user}
set monitor-hold-down-type [immediate|delay|...]
set monitor-hold-down-weekday [everyday|sunday|...]
set monitor-min {integer}
set nattraversal [enable|disable|...]
set negotiate-timeout {integer}
set net-device [enable|disable]
set network-id {integer}
set network-overlay [disable|enable]
set npu-offload [enable|disable]
set packet-redistribution [enable|disable]
set passive-mode [enable|disable]
set peer {string}
set peergrp {string}
set peerid {string}
set peertype [any|one|...]
set ppk [disable|allow|...]
set ppk-identity {string}
set ppk-secret {password-3}
set priority {integer}
set proposal {option1}, {option2}, ...
set psksecret {password-3}
set psksecret-remote {password-3}
set qkd [disable|allow|...]
set qkd-profile {string}
set reauth [disable|enable]
set rekey [enable|disable]
set remote-gw {ipv4-address}
set remote-gw-country {string}
set remote-gw-end-ip {ipv4-address-any}
set remote-gw-match [any|ipmask|...]
set remote-gw-start-ip {ipv4-address-any}
set remote-gw-subnet {ipv4-classnet-any}
set remote-gw6 {ipv6-address}
set remote-gw6-country {string}
set remote-gw6-end-ip {ipv6-address}
set remote-gw6-match [any|ipprefix|...]
set remote-gw6-start-ip {ipv6-address}
set remote-gw6-subnet {ipv6-network}
set remotegw-ddns {string}
set rsa-signature-format [pkcs1|pss]
set rsa-signature-hash-override [enable|disable]
set save-password [disable|enable]
set send-cert-chain [enable|disable]
set signature-hash-alg {option1}, {option2}, ...
set split-include-service {string}
set suite-b [disable|suite-b-gcm-128|...]
set transport [udp|udp-fallback-tcp|...]
set type [static|dynamic|...]
set unity-support [disable|enable]
set usrgrp {string}
set vni {integer}
set wizard-type [custom|dialup-forticlient|...]
set xauthtype [disable|client|...]
next
end

#### Parameters

config vpn ipsec phase1-interface
Parameter Description Type Size Default
acct-verify Enable/disable verification of RADIUS
accounting record.
option - disable
Option Description
enable Enable verification of RADIUS accounting record.
disable Disable verification of RADIUS accounting record.
add-gw-route Enable/disable automatically add a route
to the remote gateway.
option - disable
Option Description
enable Automatically add a route to the remote gateway.
disable Do not automatically add a route to the remote gateway.
add-route Enable/disable control addition of a route
to peer destination selector.
option - enable
Option Description
disable Do not add a route to destination of peer selector.
enable Add route to destination of peer selector.
aggregate-
member
Enable/disable use as an aggregate
member.
option - disable
Option Description
enable Enable use as an aggregate member.
disable Disable use as an aggregate member.
aggregate-
weight
Link weight for aggregate. integer Minimum
value: 1
Maximum
value: 100
1
assign-ip Enable/disable assignment of IP to IPsec
interface via configuration method.
option - enable
Option Description
disable Do not assign an IP address to the IPsec interface.
enable Assign an IP address to the IPsec interface.
assign-ip-from Method by which the IP address will be
assigned.
option - range
Parameter Description Type Size Default
Option Description
range Assign IP address from locally defined range.
usrgrp Assign IP address via user group.
dhcp Assign IP address via DHCP.
name Assign IP address from firewall address or group.
authmethod Authentication method. option - psk
Option Description
psk PSK authentication method.
signature Signature authentication method.
authmethod-
remote
Authentication method (remote side). option -
Option Description
psk PSK authentication method.
signature Signature authentication method.
authpasswd XAuth password (max 35 characters). password Not Specified
authusr XAuth user name. string Maximum
length: 64
authusrgrp Authentication user group. string Maximum
length: 35
auto-discovery-
crossover
Allow/block set-up of short-cut tunnels
between different network IDs.
option - allow
Option Description
allow Allow set-up of short-cut tunnels between different network IDs.
block Block set-up of short-cut tunnels between different network IDs.
auto-discovery-
forwarder
Enable/disable forwarding auto-discovery
short-cut messages.
option - disable
Option Description
enable Enable forwarding auto-discovery short-cut messages.
disable Disable forwarding auto-discovery short-cut messages.
Parameter Description Type Size Default
auto-discovery-
offer-interval
Interval between shortcut offer messages
in seconds.
integer Minimum
value: 1
Maximum
value: 300
5
auto-discovery-
psk
Enable/disable use of pre-shared secrets
for authentication of auto-discovery
tunnels.
option - disable
Option Description
enable Enable use of pre-shared-secret authentication for auto-discovery tunnels.
disable Disable use of authentication defined by 'authmethod' for auto-discovery
tunnels.
auto-discovery-
receiver
Enable/disable accepting auto-discovery
short-cut messages.
option - disable
Option Description
enable Enable receiving auto-discovery short-cut messages.
disable Disable receiving auto-discovery short-cut messages.
auto-discovery-
sender
Enable/disable sending auto-discovery
short-cut messages.
option - disable
Option Description
enable Enable sending auto-discovery short-cut messages.
disable Disable sending auto-discovery short-cut messages.
auto-discovery-
shortcuts
Control deletion of child short-cut tunnels
when the parent tunnel goes down.
option - independent
Option Description
independent Short-cut tunnels remain up if the parent tunnel goes down.
dependent Short-cut tunnels are brought down if the parent tunnel goes down.
auto-negotiate Enable/disable automatic initiation of IKE
SA negotiation.
option - enable
Option Description
enable Enable automatic initiation of IKE SA negotiation.
disable Disable automatic initiation of IKE SA negotiation.
Parameter Description Type Size Default
azure-ad-
autoconnect
Enable/disable Azure AD Auto-Connect
for FortiClient.
option - disable
Option Description
enable Enable Azure AD Auto-Connect for FortiClient.
disable Disable Azure AD Auto-Connect for FortiClient.
backup-gateway
<address>
Instruct unity clients about the backup
gateway address(es).
Address of backup gateway.
string Maximum
length: 79
banner Message that unity client should display
after connecting.
var-string Maximum
length: 1024
cert-id-validation Enable/disable cross validation of peer ID
and the identity in the peer's certificate as
specified in RFC 4945.
option - enable
Option Description
enable Enable cross validation of peer ID and the identity in the peer's certificate as
specified in RFC 4945.
disable Disable cross validation of peer ID and the identity in the peer's certificate
as specified in RFC 4945.
cert-peer-
username-strip
Enable/disable domain stripping on
certificate identity.
option - disable
Option Description
disable Disable domain stripping on certificate identity.
enable Enable domain stripping on certificate identity.
cert-peer-
username-
validation
Enable/disable cross validation of peer
username and the identity in the peer's
certificate.
option - none
Option Description
none Disable cross validation of peer username and the identity in the peer's
certificate.
othername Validate principal name in SAN othername.
rfc822name Validate RFC822 email address in SAN.
cn Validate CN in subject.
cert-trust-store CA certificate trust store. option - local
Parameter Description Type Size Default
Option Description
local Use local CA certificate.
ems Use EMS CA certificate.
certificate
<name>
The names of up to 4 signed personal
certificates.
Certificate name.
string Maximum
length: 79
childless-ike Enable/disable childless IKEv2 initiation
(RFC 6023).
option - disable
Option Description
enable Enable childless IKEv2 initiation (RFC 6023).
disable Disable childless IKEv2 initiation (RFC 6023).
client-auto-
negotiate
Enable/disable allowing the VPN client to
bring up the tunnel when there is no
traffic.
option - disable
Option Description
disable Disable allowing the VPN client to bring up the tunnel when there is no
traffic.
enable Enable allowing the VPN client to bring up the tunnel when there is no
traffic.
client-keep-alive Enable/disable allowing the VPN client to
keep the tunnel up when there is no
traffic.
option - disable
Option Description
disable Disable allowing the VPN client to keep the tunnel up when there is no
traffic.
enable Enable allowing the VPN client to keep the tunnel up when there is no
traffic.
client-resume Enable/disable resumption of offline
FortiClient sessions. When a FortiClient
enabled laptop is closed or enters
sleep/hibernate mode, enabling this
feature allows FortiClient to keep the
tunnel during this period, and allows
users to immediately resume using the
IPsec tunnel when the device wakes up.
option - disable
Parameter Description Type Size Default
Option Description
enable Enable client session resumption.
disable Disable client session resumption.
client-resume-
interval
Maximum time in seconds during which a
VPN client may resume using a tunnel
after a client PC has entered sleep mode
or temporarily lost its network connection.
integer Minimum
value: 120
Maximum
value: 172800
7200
comments Comment. var-string Maximum
length: 255
default-gw IPv4 address of default route gateway to
use for traffic exiting the interface.
ipv4-address Not Specified 0.0.0.0
default-gw-
priority
Priority for default gateway route. A
higher priority number signifies a less
preferred route.
integer Minimum
value: 0
Maximum
value:
4294967295
0
dev-id Device ID carried by the device ID
notification.
string Maximum
length: 63
dev-id-
notification
Enable/disable device ID notification. option - disable
Option Description
disable Disable device ID notification.
enable Enable device ID notification.
dhcp-ra-giaddr Relay agent gateway IP address to use in
the giaddr field of DHCP requests.
ipv4-address Not Specified 0.0.0.0
dhcp6-ra-
linkaddr
Relay agent IPv6 link address to use in
DHCP6 requests.
ipv6-address Not Specified ::
dhgrp DH group. option - 14
Option Description
1 DH Group 1.
2 DH Group 2.
5 DH Group 5.
14 DH Group 14.
15 DH Group 15.
Parameter Description Type Size Default
Option Description
16 DH Group 16.
17 DH Group 17.
18 DH Group 18.
19 DH Group 19.
20 DH Group 20.
21 DH Group 21.
27 DH Group 27.
28 DH Group 28.
29 DH Group 29.
30 DH Group 30.
31 DH Group 31.
32 DH Group 32.
digital-signature-
auth
Enable/disable IKEv2 Digital Signature
Authentication (RFC 7427).
option - disable
Option Description
enable Enable IKEv2 Digital Signature Authentication (RFC 7427).
disable Disable IKEv2 Digital Signature Authentication (RFC 7427).
distance Distance for routes added by IKE. integer Minimum
value: 1
Maximum
value: 255
15
dns-mode DNS server mode. option - manual
Option Description
manual Manually configure DNS servers.
auto Use default DNS servers.
domain Instruct unity clients about the single
default DNS domain.
string Maximum
length: 63
dpd Dead Peer Detection mode. option - on-demand
Parameter Description Type Size Default
Option Description
disable Disable Dead Peer Detection.
on-idle Trigger Dead Peer Detection when IPsec is idle.
on-demand Trigger Dead Peer Detection when IPsec traffic is sent but no reply is
received from the peer.
dpd-retrycount Number of DPD retry attempts. integer Minimum
value: 0
Maximum
value: 10
3
dpd-retryinterval DPD retry interval. user Not Specified
eap Enable/disable IKEv2 EAP
authentication.
option - disable
Option Description
enable Enable IKEv2 EAP authentication.
disable Disable IKEv2 EAP authentication.
eap-cert-auth Enable/disable peer certificate
authentication in addition to EAP if peer is
a FortiClient endpoint.
option - disable
Option Description
enable Enable peer certificate authentication in addition to EAP if peer is a
FortiClient endpoint.
disable Disable peer certificate authentication in addition to EAP if peer is a
FortiClient endpoint.
eap-exclude-
peergrp
Peer group excluded from EAP
authentication.
string Maximum
length: 35
eap-identity IKEv2 EAP peer identity type. option - use-id-payload
Option Description
use-id-payload Use IKEv2 IDi payload to resolve peer identity.
send-request Use EAP identity request to resolve peer identity.
ems-sn-check Enable/disable verification of EMS serial
number.
option - disable
Parameter Description Type Size Default
Option Description
enable Enable EMS serial number verification.
disable Disable EMS serial number verification.
encap-local-gw4 Local IPv4 address of GRE/VXLAN
tunnel.
ipv4-address Not Specified 0.0.0.0
encap-local-gw6 Local IPv6 address of GRE/VXLAN
tunnel.
ipv6-address Not Specified ::
encap-remote-
gw4
Remote IPv4 address of GRE/VXLAN
tunnel.
ipv4-address Not Specified 0.0.0.0
encap-remote-
gw6
Remote IPv6 address of GRE/VXLAN
tunnel.
ipv6-address Not Specified ::
encapsulation Enable/disable GRE/VXLAN/VPNID
encapsulation.
option - none
Option Description
none No additional encapsulation.
gre GRE encapsulation.
vxlan VXLAN encapsulation.
vpn-id-ipip VPN ID with IPIP encapsulation.
encapsulation-
address
Source for GRE/VXLAN tunnel address. option - ike
Option Description
ike Use IKE/IPsec gateway addresses.
ipv4 Specify separate GRE/VXLAN tunnel address.
ipv6 Specify separate GRE/VXLAN tunnel address.
enforce-unique-
id
Enable/disable peer ID uniqueness
check.
option - disable
Option Description
disable Disable peer ID uniqueness enforcement.
keep-new Enforce peer ID uniqueness, keep new connection if collision found.
keep-old Enforce peer ID uniqueness, keep old connection if collision found.
Parameter Description Type Size Default
esn * Extended sequence number (ESN)
negotiation.
option - disable
Option Description
require Require extended sequence number.
allow Allow extended sequence number.
disable Disable extended sequence number.
exchange-fgt-
device-id
Enable/disable device identifier exchange
with peer FortiGate units for use of VPN
monitor data by FortiManager.
option - disable
Option Description
enable Enable exchange of FortiGate device identifier.
disable Disable exchange of FortiGate device identifier.
exchange-
interface-ip
Enable/disable exchange of IPsec
interface IP address.
option - disable
Option Description
enable Enable exchange of IPsec interface IP address.
disable Disable exchange of IPsec interface IP address.
exchange-ip-
addr4
IPv4 address to exchange with peers. ipv4-address Not Specified 0.0.0.0
exchange-ip-
addr6
IPv6 address to exchange with peers. ipv6-address Not Specified ::
fallback-tcp-
threshold
Timeout in seconds before falling back
IKE/IPsec traffic to tcp.
integer Minimum
value: 1
Maximum
value: 300
15
fec-base Number of base Forward Error Correction
packets.
integer Minimum
value: 1
Maximum
value: 20
10
fec-codec Forward Error Correction
encoding/decoding algorithm.
option - rs
Option Description
rs Reed-Solomon FEC algorithm.
Parameter Description Type Size Default
Option Description
xor XOR FEC algorithm.
fec-egress Enable/disable Forward Error Correction
for egress IPsec traffic.
option - disable
Option Description
enable Enable Forward Error Correction for egress IPsec traffic.
disable Disable Forward Error Correction for egress IPsec traffic.
fec-health-check SD-WAN health check. string Maximum
length: 35
fec-ingress Enable/disable Forward Error Correction
for ingress IPsec traffic.
option - disable
Option Description
enable Enable Forward Error Correction for ingress IPsec traffic.
disable Disable Forward Error Correction for ingress IPsec traffic.
fec-mapping-
profile
Forward Error Correction (FEC) mapping
profile.
string Maximum
length: 35
fec-receive-
timeout
Timeout in milliseconds before dropping
Forward Error Correction packets.
integer Minimum
value: 1
Maximum
value: 1000
50
fec-redundant Number of redundant Forward Error
Correction packets.
integer Minimum
value: 1
Maximum
value: 5
1
fec-send-timeout Timeout in milliseconds before sending
Forward Error Correction packets.
integer Minimum
value: 1
Maximum
value: 1000
5
fgsp-sync Enable/disable IPsec syncing of tunnels
for FGSP IPsec.
option - disable
Option Description
enable Enable IPsec syncing of tunnels to other cluster members.
disable Disable IPsec syncing of tunnels to other cluster members.
Parameter Description Type Size Default
fortinet-esp Enable/disable Fortinet ESP
encapsulaton.
option - disable
Option Description
enable Enable Fortinet ESP encapsulation.
disable Disable Fortinet ESP encapsulaton.
fragmentation Enable/disable fragment IKE message on
re-transmission.
option - enable
Option Description
enable Enable intra-IKE fragmentation support on re-transmission.
disable Disable intra-IKE fragmentation support.
fragmentation-
mtu
IKE fragmentation MTU. integer Minimum
value: 500
Maximum
value: 16000
1200
group-
authentication
Enable/disable IKEv2 IDi group
authentication.
option - disable
Option Description
enable Enable IKEv2 IDi group authentication.
disable Disable IKEv2 IDi group authentication.
group-
authentication-
secret
Password for IKEv2 ID group
authentication. ASCII string or
hexadecimal indicated by a leading 0x.
password-3 Not Specified
ha-sync-esp-
seqno
Enable/disable sequence number jump
ahead for IPsec HA.
option - enable
Option Description
enable Enable HA syncing of ESP sequence numbers.
disable Disable HA syncing of ESP sequence numbers.
idle-timeout Enable/disable IPsec tunnel idle timeout. option - disable
Option Description
enable Enable IPsec tunnel idle timeout.
disable Disable IPsec tunnel idle timeout.
Parameter Description Type Size Default
idle-
timeoutinterval
IPsec tunnel idle timeout in minutes. integer Minimum
value: 5
Maximum
value: 43200
15
ike-version IKE protocol version. option - 1
Option Description
1 Use IKEv1 protocol.
2 Use IKEv2 protocol.
inbound-dscp-
copy
Enable/disable copy the dscp in the ESP
header to the inner IP Header.
option - disable
Option Description
enable Enable copy the dscp in the ESP header to the inner IP Header.
disable Disable copy the dscp in the ESP header to the inner IP Header.
include-local-lan Enable/disable allow local LAN access on
unity clients.
option - disable
Option Description
disable Disable local LAN access on Unity clients.
enable Enable local LAN access on Unity clients.
interface Local physical, aggregate, or VLAN
outgoing interface.
string Maximum
length: 35
internal-domain-
list <domain-
name>
One or more internal domain names in
quotes separated by spaces.
Domain name.
string Maximum
length: 79
ip-delay-interval IP address reuse delay interval in
seconds.
integer Minimum
value: 0
Maximum
value: 28800
0
ip-fragmentation Determine whether IP packets are
fragmented before or after IPsec
encapsulation.
option - post-encapsulation
Option Description
pre-
encapsulation
Fragment before IPsec encapsulation.
Parameter Description Type Size Default
Option Description
post-
encapsulation
Fragment after IPsec encapsulation (RFC compliant).
ip-version IP version to use for VPN interface. option - 4
Option Description
4 Use IPv4 addressing for gateways.
6 Use IPv6 addressing for gateways.
ipv4-dns-server1 IPv4 DNS server 1. ipv4-address Not Specified 0.0.0.0
ipv4-dns-server2 IPv4 DNS server 2. ipv4-address Not Specified 0.0.0.0
ipv4-dns-server3 IPv4 DNS server 3. ipv4-address Not Specified 0.0.0.0
ipv4-end-ip End of IPv4 range. ipv4-address Not Specified 0.0.0.0
ipv4-name IPv4 address name. string Maximum
length: 79
ipv4-netmask IPv4 Netmask. ipv4-
netmask
Not Specified 255.255.255.255
ipv4-split-
exclude
IPv4 subnets that should not be sent over
the IPsec tunnel.
string Maximum
length: 79
ipv4-split-include IPv4 split-include subnets. string Maximum
length: 79
ipv4-start-ip Start of IPv4 range. ipv4-address Not Specified 0.0.0.0
ipv4-wins-
server1
WINS server 1. ipv4-address Not Specified 0.0.0.0
ipv4-wins-
server2
WINS server 2. ipv4-address Not Specified 0.0.0.0
ipv6-dns-server1 IPv6 DNS server 1. ipv6-address Not Specified ::
ipv6-dns-server2 IPv6 DNS server 2. ipv6-address Not Specified ::
ipv6-dns-server3 IPv6 DNS server 3. ipv6-address Not Specified ::
ipv6-end-ip End of IPv6 range. ipv6-address Not Specified ::
ipv6-name IPv6 address name. string Maximum
length: 79
Parameter Description Type Size Default
ipv6-prefix IPv6 prefix. integer Minimum
value: 1
Maximum
value: 128
128
ipv6-split-
exclude
IPv6 subnets that should not be sent over
the IPsec tunnel.
string Maximum
length: 79
ipv6-split-include IPv6 split-include subnets. string Maximum
length: 79
ipv6-start-ip Start of IPv6 range. ipv6-address Not Specified ::
keepalive NAT-T keep alive interval. integer Minimum
value: 5
Maximum
value: 900
10
keylife Time to wait in seconds before phase 1
encryption key expires.
integer Minimum
value: 120
Maximum
value: 172800
86400
kms Key Management Services server. string Maximum
length: 35
link-cost VPN tunnel underlay link cost. integer Minimum
value: 0
Maximum
value: 255
0
local-gw IPv4 address of the local gateway's
external interface.
ipv4-address Not Specified 0.0.0.0
local-gw6 IPv6 address of the local gateway's
external interface.
ipv6-address Not Specified ::
localid Local ID. string Maximum
length: 63
localid-type Local ID type. option - auto
Option Description
auto Select ID type automatically.
fqdn Use fully qualified domain name.
user-fqdn Use user fully qualified domain name.
keyid Use key-id string.
address Use local IP address.
asn1dn Use ASN.1 distinguished name.
Parameter Description Type Size Default
loopback-
asymroute
Enable/disable asymmetric routing for
IKE traffic on loopback interface.
option - enable
Option Description
enable Allow ingress/egress IKE traffic to be routed over different interfaces.
disable Ingress/egress IKE traffic must be routed over the same interface.
mesh-selector-
type
Add selectors containing subsets of the
configuration depending on traffic.
option - disable
Option Description
disable Disable.
subnet Enable addition of matching subnet selector.
host Enable addition of host to host selector.
mode The ID protection mode used to establish
a secure channel.
option - main
Option Description
aggressive Aggressive mode.
main Main mode.
mode-cfg Enable/disable configuration method. option - disable
Option Description
disable Disable Configuration Method.
enable Enable Configuration Method.
mode-cfg-allow-
client-selector
Enable/disable mode-cfg client to use
custom phase2 selectors.
option - disable
Option Description
disable Mode-cfg client to use wildcard selectors.
enable Mode-cfg client to use custom selectors.
monitor <name> IPsec interface as backup for primary
interface.
IPsec interface as backup for primary
interface.
string Maximum
length: 79
Parameter Description Type Size Default
monitor-hold-
down-delay
Time to wait in seconds before recovery
once primary re-establishes.
integer Minimum
value: 0
Maximum
value:
31536000
0
monitor-hold-
down-time
Time of day at which to fail back to
primary after it re-establishes.
user Not Specified
monitor-hold-
down-type
Recovery time method when primary
interface re-establishes.
option - immediate
Option Description
immediate Fail back immediately after primary recovers.
delay Number of seconds to delay fail back after primary recovers.
time Specify a time at which to fail back after primary recovers.
monitor-hold-
down-weekday
Day of the week to recover once primary
re-establishes.
option - sunday
Option Description
everyday Every Day.
sunday Sunday.
monday Monday.
tuesday Tuesday.
wednesday Wednesday.
thursday Thursday.
friday Friday.
saturday Saturday.
monitor-min Minimum number of links to become
degraded before activating this interface.
Zero (0) means all links must be down
before activating this interface.
integer Minimum
value: 0
Maximum
value:
4294967295
0
name IPsec remote gateway name. string Maximum
length: 15
nattraversal Enable/disable NAT traversal. option - enable
Parameter Description Type Size Default
Option Description
enable Enable IPsec NAT traversal.
disable Disable IPsec NAT traversal.
forced Force IPsec NAT traversal on.
negotiate-
timeout
IKE SA negotiation timeout in seconds. integer Minimum
value: 1
Maximum
value: 300
30
net-device Enable/disable kernel device creation. option - disable
Option Description
enable Create a kernel device for every tunnel.
disable Do not create a kernel device for tunnels.
network-id VPN gateway network ID. integer Minimum
value: 0
Maximum
value: 255
0
network-overlay Enable/disable network overlays. option - disable
Option Description
disable Disable network overlays.
enable Enable network overlays.
npu-offload * Enable/disable offloading NPU. option - enable
Option Description
enable Enable NPU offloading.
disable Disable NPU offloading.
packet-
redistribution *
Enable/disable packet distribution (RPS)
on the IPsec interface.
option - disable
Option Description
enable Enable packet redistribution.
disable Disable packet redistribution.
passive-mode Enable/disable IPsec passive mode for
static tunnels.
option - disable
Parameter Description Type Size Default
Option Description
enable Enable IPsec passive mode.
disable Disable IPsec passive mode.
peer Accept this peer certificate. string Maximum
length: 35
peergrp Accept this peer certificate group. string Maximum
length: 35
peerid Accept this peer identity. string Maximum
length: 255
peertype Accept this peer type. option - peer
Option Description
any Accept any peer ID.
one Accept this peer ID.
dialup Accept peer ID in dialup group.
peer Accept this peer certificate.
peergrp Accept this peer certificate group.
ppk Enable/disable IKEv2 Postquantum
Preshared Key (PPK).
option - disable
Option Description
disable Disable use of IKEv2 Postquantum Preshared Key (PPK).
allow Allow, but do not require, use of IKEv2 Postquantum Preshared Key (PPK).
require Require use of IKEv2 Postquantum Preshared Key (PPK).
ppk-identity IKEv2 Postquantum Preshared Key
Identity.
string Maximum
length: 35
ppk-secret IKEv2 Postquantum Preshared Key
(ASCII string or hexadecimal encoded
with a leading 0x).
password-3 Not Specified
priority Priority for routes added by IKE. integer Minimum
value: 1
Maximum
value: 65535
1
proposal Phase1 proposal. option -
Parameter Description Type Size Default
Option Description
des-md5 des-md5
des-sha1 des-sha1
des-sha256 des-sha256
des-sha384 des-sha384
des-sha512 des-sha512
3des-md5 3des-md5
3des-sha1 3des-sha1
3des-sha256 3des-sha256
3des-sha384 3des-sha384
3des-sha512 3des-sha512
aes128-md5 aes128-md5
aes128-sha1 aes128-sha1
aes128-sha256 aes128-sha256
aes128-sha384 aes128-sha384
aes128-sha512 aes128-sha512
aes128gcm-prfsha1 aes128gcm-prfsha1
aes128gcm-prfsha256 aes128gcm-prfsha256
aes128gcm-prfsha384 aes128gcm-prfsha384
aes128gcm-prfsha512 aes128gcm-prfsha512
aes192-md5 aes192-md5
aes192-sha1 aes192-sha1
aes192-sha256 aes192-sha256
aes192-sha384 aes192-sha384
aes192-sha512 aes192-sha512
aes256-md5 aes256-md5
aes256-sha1 aes256-sha1
aes256-sha256 aes256-sha256
aes256-sha384 aes256-sha384
aes256-sha512 aes256-sha512
Parameter Description Type Size Default
Option Description
aes256gcm-prfsha1 aes256gcm-prfsha1
aes256gcm-prfsha256 aes256gcm-prfsha256
aes256gcm-prfsha384 aes256gcm-prfsha384
aes256gcm-prfsha512 aes256gcm-prfsha512
chacha20poly1305-prfsha1 chacha20poly1305-prfsha1
chacha20poly1305-prfsha256 chacha20poly1305-prfsha256
chacha20poly1305-prfsha384 chacha20poly1305-prfsha384
chacha20poly1305-prfsha512 chacha20poly1305-prfsha512
aria128-md5 aria128-md5
aria128-sha1 aria128-sha1
aria128-sha256 aria128-sha256
aria128-sha384 aria128-sha384
aria128-sha512 aria128-sha512
aria192-md5 aria192-md5
aria192-sha1 aria192-sha1
aria192-sha256 aria192-sha256
aria192-sha384 aria192-sha384
aria192-sha512 aria192-sha512
aria256-md5 aria256-md5
aria256-sha1 aria256-sha1
aria256-sha256 aria256-sha256
aria256-sha384 aria256-sha384
aria256-sha512 aria256-sha512
seed-md5 seed-md5
seed-sha1 seed-sha1
seed-sha256 seed-sha256
seed-sha384 seed-sha384
seed-sha512 seed-sha512
Parameter Description Type Size Default
psksecret Pre-shared secret for PSK authentication
(ASCII string or hexadecimal encoded
with a leading 0x).
password-3 Not Specified
psksecret-
remote
Pre-shared secret for remote side PSK
authentication (ASCII string or
hexadecimal encoded with a leading 0x).
password-3 Not Specified
qkd Enable/disable use of Quantum Key
Distribution (QKD) server.
option - disable
Option Description
disable Disable use of a Quantum Key Distribution (QKD) server.
allow Allow, but do not require, use of a Quantum Key Distribution (QKD) server.
require Require use of a Quantum Key Distribution (QKD) server.
qkd-profile Quantum Key Distribution (QKD) server
profile.
string Maximum
length: 35
reauth Enable/disable re-authentication upon
IKE SA lifetime expiration.
option - disable
Option Description
disable Disable IKE SA re-authentication.
enable Enable IKE SA re-authentication.
rekey Enable/disable phase1 rekey. option - enable
Option Description
enable Enable phase1 rekey.
disable Disable phase1 rekey.
remote-gw IPv4 address of the remote gateway's
external interface.
ipv4-address Not Specified 0.0.0.0
remote-gw-
country
IPv4 addresses associated to a specific
country.
string Maximum
length: 2
remote-gw-end-
ip
Last IPv4 address in the range. ipv4-
address-any
Not Specified 0.0.0.0
remote-gw-
match
Set type of IPv4 remote gateway address
matching.
option - any
Parameter Description Type Size Default
Option Description
any Match any IPv4 gateway address.
ipmask Match IPv4 gateway address and mask.
iprange Match IPv4 gateway address range.
geography Match IPv4 gateway address from a specified country.
remote-gw-start-
ip
First IPv4 address in the range. ipv4-
address-any
Not Specified 0.0.0.0
remote-gw-
subnet
IPv4 address and subnet mask. ipv4-
classnet-any
Not Specified 0.0.0.0 0.0.0.0
remote-gw6 IPv6 address of the remote gateway's
external interface.
ipv6-address Not Specified ::
remote-gw6-
country
IPv6 addresses associated to a specific
country.
string Maximum
length: 2
remote-gw6-end-
ip
Last IPv6 address in the range. ipv6-address Not Specified ::
remote-gw6-
match
Set type of IPv6 remote gateway address
matching.
option - any
Option Description
any Match any IPv6 gateway address.
ipprefix Match IPv6 gateway address and prefix.
iprange Match IPv6 gateway address range.
geography Match IPv6 gateway address from a specified country.
remote-gw6-
start-ip
First IPv6 address in the range. ipv6-address Not Specified ::
remote-gw6-
subnet
IPv6 address and prefix. ipv6-network Not Specified ::/0
remotegw-ddns Domain name of remote gateway. For
example, name.ddns.com.
string Maximum
length: 63
rsa-signature-
format
Digital Signature Authentication RSA
signature format.
option - pkcs1
Option Description
pkcs1 RSASSA PKCS#1 v1.5.
pss RSASSA Probabilistic Signature Scheme (PSS).
Parameter Description Type Size Default
rsa-signature-
hash-override
Enable/disable IKEv2 RSA signature
hash algorithm override.
option - disable
Option Description
enable Enable IKEv2 RSA signature hash algorithm override.
disable Disable IKEv2 RSA signature hash algorithm override.
save-password Enable/disable saving XAuth username
and password on VPN clients.
option - disable
Option Description
disable Disable saving XAuth username and password on VPN clients.
enable Enable saving XAuth username and password on VPN clients.
send-cert-chain Enable/disable sending certificate chain. option - enable
Option Description
enable Enable sending certificate chain.
disable Disable sending certificate chain.
signature-hash-
alg
Digital Signature Authentication hash
algorithms.
option - sha2-512
Option Description
sha1 SHA1.
sha2-256 SHA2-256.
sha2-384 SHA2-384.
sha2-512 SHA2-512.
split-include-
service
Split-include services. string Maximum
length: 79
suite-b Use Suite-B. option - disable
Option Description
disable Do not use UI suite.
suite-b-gcm-128 Use Suite-B-GCM-128.
suite-b-gcm-256 Use Suite-B-GCM-256.
transport Set IKE transport protocol. option - udp
Parameter Description Type Size Default
Option Description
udp Use UDP transport for IKE.
udp-fallback-tcp Use UDP transport for IKE, with fallback to TCP transport.
tcp Use TCP transport for IKE.
type Remote gateway type. option - static
Option Description
static Remote VPN gateway has fixed IP address.
dynamic Remote VPN gateway has dynamic IP address.
ddns Remote VPN gateway has dynamic IP address and is a dynamic DNS
client.
unity-support Enable/disable support for Cisco UNITY
Configuration Method extensions.
option - enable
Option Description
disable Disable Cisco Unity Configuration Method Extensions.
enable Enable Cisco Unity Configuration Method Extensions.
usrgrp User group name for dialup peers. string Maximum
length: 35
vni VNI of VXLAN tunnel. integer Minimum
value: 1
Maximum
value:
16777215
0
wizard-type GUI VPN Wizard Type. option - custom
Option Description
custom Custom VPN configuration.
dialup-forticlient Dial Up - FortiClient Windows, Mac and Android.
dialup-ios Dial Up - iPhone / iPad Native IPsec Client.
dialup-android Dial Up - Android Native IPsec Client.
dialup-windows Dial Up - Windows Native IPsec Client.
dialup-cisco Dial Up - Cisco IPsec Client.
static-fortigate Site to Site - FortiGate.
Parameter Description Type Size Default
Option Description
dialup-fortigate Dial Up - FortiGate.
static-cisco Site to Site - Cisco.
dialup-cisco-fw Dialup Up - Cisco Firewall.
simplified-static-
fortigate
Site to Site - FortiGate (SD-WAN).
hub-fortigate-
auto-discovery
Hub role in a Hub-and-Spoke auto-discovery VPN.
spoke-fortigate-
auto-discovery
Spoke role in a Hub-and-Spoke auto-discovery VPN.
xauthtype XAuth type. option - disable
Option Description
disable Disable.
client Enable as client.
pap Enable as server PAP.
chap Enable as server CHAP.
auto Enable as server auto.
- This parameter may not exist in some models.
config ipv4-exclude-range
Parameter Description Type Size Default
end-ip End of IPv4 exclusive range. ipv4-
address
Not Specified 0.0.0.0
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
start-ip Start of IPv4 exclusive range. ipv4-
address
Not Specified 0.0.0.0
config ipv6-exclude-range
Parameter Description Type Size Default
end-ip End of IPv6 exclusive range. ipv6-
address
Not Specified ::
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
start-ip Start of IPv6 exclusive range. ipv6-
address
Not Specified ::

### config vpn ipsec phase1

Configure VPN remote gateway.

#### Syntax

config vpn ipsec phase1
Description: Configure VPN remote gateway.
edit <name>
set acct-verify [enable|disable]
set add-gw-route [enable|disable]
set add-route [disable|enable]
set assign-ip [disable|enable]
set assign-ip-from [range|usrgrp|...]
set authmethod [psk|signature]
set authmethod-remote [psk|signature]
set authpasswd {password}
set authusr {string}
set authusrgrp {string}
set auto-negotiate [enable|disable]
set azure-ad-autoconnect [enable|disable]
set backup-gateway <address1>, <address2>, ...
set banner {var-string}
set cert-id-validation [enable|disable]
set cert-peer-username-strip [disable|enable]
set cert-peer-username-validation [none|othername|...]
set cert-trust-store [local|ems]
set certificate <name1>, <name2>, ...
set childless-ike [enable|disable]
set client-auto-negotiate [disable|enable]
set client-keep-alive [disable|enable]
set client-resume [enable|disable]
set client-resume-interval {integer}
set comments {var-string}
set dev-id {string}
set dev-id-notification [disable|enable]
set dhcp-ra-giaddr {ipv4-address}
set dhcp6-ra-linkaddr {ipv6-address}
set dhgrp {option1}, {option2}, ...
set digital-signature-auth [enable|disable]
set distance {integer}
set dns-mode [manual|auto]
set domain {string}
set dpd [disable|on-idle|...]
set dpd-retrycount {integer}
set dpd-retryinterval {user}
set eap [enable|disable]
set eap-cert-auth [enable|disable]
set eap-exclude-peergrp {string}
set eap-identity [use-id-payload|send-request]
set ems-sn-check [enable|disable]
set enforce-unique-id [disable|keep-new|...]
set esn [require|allow|...]
set exchange-fgt-device-id [enable|disable]
set fallback-tcp-threshold {integer}
set fec-base {integer}
set fec-codec [rs|xor]
set fec-egress [enable|disable]
set fec-health-check {string}
set fec-ingress [enable|disable]
set fec-mapping-profile {string}
set fec-receive-timeout {integer}
set fec-redundant {integer}
set fec-send-timeout {integer}
set fgsp-sync [enable|disable]
set fortinet-esp [enable|disable]
set fragmentation [enable|disable]
set fragmentation-mtu {integer}
set group-authentication [enable|disable]
set group-authentication-secret {password-3}
set ha-sync-esp-seqno [enable|disable]
set idle-timeout [enable|disable]
set idle-timeoutinterval {integer}
set ike-version [1|2]
set inbound-dscp-copy [enable|disable]
set include-local-lan [disable|enable]
set interface {string}
set internal-domain-list <domain-name1>, <domain-name2>, ...
set ip-delay-interval {integer}
set ipv4-dns-server1 {ipv4-address}
set ipv4-dns-server2 {ipv4-address}
set ipv4-dns-server3 {ipv4-address}
set ipv4-end-ip {ipv4-address}
config ipv4-exclude-range
Description: Configuration Method IPv4 exclude ranges.
edit <id>
set end-ip {ipv4-address}
set start-ip {ipv4-address}
next
end
set ipv4-name {string}
set ipv4-netmask {ipv4-netmask}
set ipv4-split-exclude {string}
set ipv4-split-include {string}
set ipv4-start-ip {ipv4-address}
set ipv4-wins-server1 {ipv4-address}
set ipv4-wins-server2 {ipv4-address}
set ipv6-dns-server1 {ipv6-address}
set ipv6-dns-server2 {ipv6-address}
set ipv6-dns-server3 {ipv6-address}
set ipv6-end-ip {ipv6-address}
config ipv6-exclude-range
Description: Configuration method IPv6 exclude ranges.
edit <id>
set end-ip {ipv6-address}
set start-ip {ipv6-address}
next
end
set ipv6-name {string}
set ipv6-prefix {integer}
set ipv6-split-exclude {string}
set ipv6-split-include {string}
set ipv6-start-ip {ipv6-address}
set keepalive {integer}
set keylife {integer}
set kms {string}
set link-cost {integer}
set local-gw {ipv4-address}
set localid {string}
set localid-type [auto|fqdn|...]
set loopback-asymroute [enable|disable]
set mesh-selector-type [disable|subnet|...]
set mode [aggressive|main]
set mode-cfg [disable|enable]
set mode-cfg-allow-client-selector [disable|enable]
set nattraversal [enable|disable|...]
set negotiate-timeout {integer}
set network-id {integer}
set network-overlay [disable|enable]
set npu-offload [enable|disable]
set peer {string}
set peergrp {string}
set peerid {string}
set peertype [any|one|...]
set ppk [disable|allow|...]
set ppk-identity {string}
set ppk-secret {password-3}
set priority {integer}
set proposal {option1}, {option2}, ...
set psksecret {password-3}
set psksecret-remote {password-3}
set qkd [disable|allow|...]
set qkd-profile {string}
set reauth [disable|enable]
set rekey [enable|disable]
set remote-gw {ipv4-address}
set remote-gw-country {string}
set remote-gw-end-ip {ipv4-address-any}
set remote-gw-match [any|ipmask|...]
set remote-gw-start-ip {ipv4-address-any}
set remote-gw-subnet {ipv4-classnet-any}
set remote-gw6-country {string}
set remote-gw6-end-ip {ipv6-address}
set remote-gw6-match [any|ipprefix|...]
set remote-gw6-start-ip {ipv6-address}
set remote-gw6-subnet {ipv6-network}
set remotegw-ddns {string}
set rsa-signature-format [pkcs1|pss]
set rsa-signature-hash-override [enable|disable]
set save-password [disable|enable]
set send-cert-chain [enable|disable]
set signature-hash-alg {option1}, {option2}, ...
set split-include-service {string}
set suite-b [disable|suite-b-gcm-128|...]
set transport [udp|udp-fallback-tcp|...]
set type [static|dynamic|...]
set unity-support [disable|enable]
set usrgrp {string}
set wizard-type [custom|dialup-forticlient|...]
set xauthtype [disable|client|...]
next
end

#### Parameters

config vpn ipsec phase1
Parameter Description Type Size Default
acct-verify Enable/disable verification of RADIUS
accounting record.
option - disable
Option Description
enable Enable verification of RADIUS accounting record.
disable Disable verification of RADIUS accounting record.
add-gw-route Enable/disable automatically add a route to
the remote gateway.
option - disable
Option Description
enable Automatically add a route to the remote gateway.
disable Do not automatically add a route to the remote gateway.
add-route Enable/disable control addition of a route to
peer destination selector.
option - disable
Option Description
disable Do not add a route to destination of peer selector.
enable Add route to destination of peer selector.
assign-ip Enable/disable assignment of IP to IPsec
interface via configuration method.
option - enable
Parameter Description Type Size Default
Option Description
disable Do not assign an IP address to the IPsec interface.
enable Assign an IP address to the IPsec interface.
assign-ip-from Method by which the IP address will be
assigned.
option - range
Option Description
range Assign IP address from locally defined range.
usrgrp Assign IP address via user group.
dhcp Assign IP address via DHCP.
name Assign IP address from firewall address or group.
authmethod Authentication method. option - psk
Option Description
psk PSK authentication method.
signature Signature authentication method.
authmethod-
remote
Authentication method (remote side). option -
Option Description
psk PSK authentication method.
signature Signature authentication method.
authpasswd XAuth password (max 35 characters). password Not
Specified
authusr XAuth user name. string Maximum
length: 64
authusrgrp Authentication user group. string Maximum
length: 35
auto-negotiate Enable/disable automatic initiation of IKE
SA negotiation.
option - enable
Option Description
enable Enable automatic initiation of IKE SA negotiation.
disable Disable automatic initiation of IKE SA negotiation.
Parameter Description Type Size Default
azure-ad-
autoconnect
Enable/disable Azure AD Auto-Connect for
FortiClient.
option - disable
Option Description
enable Enable Azure AD Auto-Connect for FortiClient.
disable Disable Azure AD Auto-Connect for FortiClient.
backup-gateway
<address>
Instruct unity clients about the backup
gateway address(es).
Address of backup gateway.
string Maximum
length: 79
banner Message that unity client should display
after connecting.
var-string Maximum
length: 1024
cert-id-validation Enable/disable cross validation of peer ID
and the identity in the peer's certificate as
specified in RFC 4945.
option - enable
Option Description
enable Enable cross validation of peer ID and the identity in the peer's certificate as
specified in RFC 4945.
disable Disable cross validation of peer ID and the identity in the peer's certificate
as specified in RFC 4945.
cert-peer-
username-strip
Enable/disable domain stripping on
certificate identity.
option - disable
Option Description
disable Disable domain stripping on certificate identity.
enable Enable domain stripping on certificate identity.
cert-peer-
username-
validation
Enable/disable cross validation of peer
username and the identity in the peer's
certificate.
option - none
Option Description
none Disable cross validation of peer username and the identity in the peer's
certificate.
othername Validate principal name in SAN othername.
rfc822name Validate RFC822 email address in SAN.
cn Validate CN in subject.
cert-trust-store CA certificate trust store. option - local
Parameter Description Type Size Default
Option Description
local Use local CA certificate.
ems Use EMS CA certificate.
certificate
<name>
Names of up to 4 signed personal
certificates.
Certificate name.
string Maximum
length: 79
childless-ike Enable/disable childless IKEv2 initiation
(RFC 6023).
option - disable
Option Description
enable Enable childless IKEv2 initiation (RFC 6023).
disable Disable childless IKEv2 initiation (RFC 6023).
client-auto-
negotiate
Enable/disable allowing the VPN client to
bring up the tunnel when there is no traffic.
option - disable
Option Description
disable Disable allowing the VPN client to bring up the tunnel when there is no
traffic.
enable Enable allowing the VPN client to bring up the tunnel when there is no
traffic.
client-keep-alive Enable/disable allowing the VPN client to
keep the tunnel up when there is no traffic.
option - disable
Option Description
disable Disable allowing the VPN client to keep the tunnel up when there is no
traffic.
enable Enable allowing the VPN client to keep the tunnel up when there is no
traffic.
client-resume Enable/disable resumption of offline
FortiClient sessions. When a FortiClient
enabled laptop is closed or enters
sleep/hibernate mode, enabling this feature
allows FortiClient to keep the tunnel during
this period, and allows users to immediately
resume using the IPsec tunnel when the
device wakes up.
option - disable
Parameter Description Type Size Default
Option Description
enable Enable client session resumption.
disable Disable client session resumption.
client-resume-
interval
Maximum time in seconds during which a
VPN client may resume using a tunnel after
a client PC has entered sleep mode or
temporarily lost its network connection.
integer Minimum
value: 120
Maximum
value:
172800
7200
comments Comment. var-string Maximum
length: 255
dev-id Device ID carried by the device ID
notification.
string Maximum
length: 63
dev-id-
notification
Enable/disable device ID notification. option - disable
Option Description
disable Disable device ID notification.
enable Enable device ID notification.
dhcp-ra-giaddr Relay agent gateway IP address to use in
the giaddr field of DHCP requests.
ipv4-address Not
Specified
0.0.0.0
dhcp6-ra-
linkaddr
Relay agent IPv6 link address to use in
DHCP6 requests.
ipv6-address Not
Specified
::
dhgrp DH group. option - 14
Option Description
1 DH Group 1.
2 DH Group 2.
5 DH Group 5.
14 DH Group 14.
15 DH Group 15.
16 DH Group 16.
17 DH Group 17.
18 DH Group 18.
19 DH Group 19.
Parameter Description Type Size Default
Option Description
20 DH Group 20.
21 DH Group 21.
27 DH Group 27.
28 DH Group 28.
29 DH Group 29.
30 DH Group 30.
31 DH Group 31.
32 DH Group 32.
digital-signature-
auth
Enable/disable IKEv2 Digital Signature
Authentication (RFC 7427).
option - disable
Option Description
enable Enable IKEv2 Digital Signature Authentication (RFC 7427).
disable Disable IKEv2 Digital Signature Authentication (RFC 7427).
distance Distance for routes added by IKE. integer Minimum
value: 1
Maximum
value: 255
15
dns-mode DNS server mode. option - manual
Option Description
manual Manually configure DNS servers.
auto Use default DNS servers.
domain Instruct unity clients about the single default
DNS domain.
string Maximum
length: 63
dpd Dead Peer Detection mode. option - on-demand
Option Description
disable Disable Dead Peer Detection.
on-idle Trigger Dead Peer Detection when IPsec is idle.
on-demand Trigger Dead Peer Detection when IPsec traffic is sent but no reply is
received from the peer.
Parameter Description Type Size Default
dpd-retrycount Number of DPD retry attempts. integer Minimum
value: 0
Maximum
value: 10
3
dpd-retryinterval DPD retry interval. user Not
Specified
eap Enable/disable IKEv2 EAP authentication. option - disable
Option Description
enable Enable IKEv2 EAP authentication.
disable Disable IKEv2 EAP authentication.
eap-cert-auth Enable/disable peer certificate
authentication in addition to EAP if peer is a
FortiClient endpoint.
option - disable
Option Description
enable Enable peer certificate authentication in addition to EAP if peer is a
FortiClient endpoint.
disable Disable peer certificate authentication in addition to EAP if peer is a
FortiClient endpoint.
eap-exclude-
peergrp
Peer group excluded from EAP
authentication.
string Maximum
length: 35
eap-identity IKEv2 EAP peer identity type. option - use-id-payload
Option Description
use-id-payload Use IKEv2 IDi payload to resolve peer identity.
send-request Use EAP identity request to resolve peer identity.
ems-sn-check Enable/disable verification of EMS serial
number.
option - disable
Option Description
enable Enable EMS serial number verification.
disable Disable EMS serial number verification.
enforce-unique-
id
Enable/disable peer ID uniqueness check. option - disable
Parameter Description Type Size Default
Option Description
disable Disable peer ID uniqueness enforcement.
keep-new Enforce peer ID uniqueness, keep new connection if collision found.
keep-old Enforce peer ID uniqueness, keep old connection if collision found.
esn * Extended sequence number (ESN)
negotiation.
option - disable
Option Description
require Require extended sequence number.
allow Allow extended sequence number.
disable Disable extended sequence number.
exchange-fgt-
device-id
Enable/disable device identifier exchange
with peer FortiGate units for use of VPN
monitor data by FortiManager.
option - disable
Option Description
enable Enable exchange of FortiGate device identifier.
disable Disable exchange of FortiGate device identifier.
fallback-tcp-
threshold
Timeout in seconds before falling back
IKE/IPsec traffic to tcp.
integer Minimum
value: 1
Maximum
value: 300
15
fec-base Number of base Forward Error Correction
packets.
integer Minimum
value: 1
Maximum
value: 20
10
fec-codec Forward Error Correction
encoding/decoding algorithm.
option - rs
Option Description
rs Reed-Solomon FEC algorithm.
xor XOR FEC algorithm.
fec-egress Enable/disable Forward Error Correction for
egress IPsec traffic.
option - disable
Parameter Description Type Size Default
Option Description
enable Enable Forward Error Correction for egress IPsec traffic.
disable Disable Forward Error Correction for egress IPsec traffic.
fec-health-check SD-WAN health check. string Maximum
length: 35
fec-ingress Enable/disable Forward Error Correction for
ingress IPsec traffic.
option - disable
Option Description
enable Enable Forward Error Correction for ingress IPsec traffic.
disable Disable Forward Error Correction for ingress IPsec traffic.
fec-mapping-
profile
Forward Error Correction (FEC) mapping
profile.
string Maximum
length: 35
fec-receive-
timeout
Timeout in milliseconds before dropping
Forward Error Correction packets.
integer Minimum
value: 1
Maximum
value: 1000
50
fec-redundant Number of redundant Forward Error
Correction packets.
integer Minimum
value: 1
Maximum
value: 5
1
fec-send-timeout Timeout in milliseconds before sending
Forward Error Correction packets.
integer Minimum
value: 1
Maximum
value: 1000
5
fgsp-sync Enable/disable IPsec syncing of tunnels for
FGSP IPsec.
option - disable
Option Description
enable Enable IPsec syncing of tunnels to other cluster members.
disable Disable IPsec syncing of tunnels to other cluster members.
fortinet-esp Enable/disable Fortinet ESP encapsulaton. option - disable
Option Description
enable Enable Fortinet ESP encapsulation.
disable Disable Fortinet ESP encapsulaton.
Parameter Description Type Size Default
fragmentation Enable/disable fragment IKE message on
re-transmission.
option - enable
Option Description
enable Enable intra-IKE fragmentation support on re-transmission.
disable Disable intra-IKE fragmentation support.
fragmentation-
mtu
IKE fragmentation MTU. integer Minimum
value: 500
Maximum
value: 16000
1200
group-
authentication
Enable/disable IKEv2 IDi group
authentication.
option - disable
Option Description
enable Enable IKEv2 IDi group authentication.
disable Disable IKEv2 IDi group authentication.
group-
authentication-
secret
Password for IKEv2 ID group
authentication. ASCII string or hexadecimal
indicated by a leading 0x.
password-3 Not
Specified
ha-sync-esp-
seqno
Enable/disable sequence number jump
ahead for IPsec HA.
option - enable
Option Description
enable Enable HA syncing of ESP sequence numbers.
disable Disable HA syncing of ESP sequence numbers.
idle-timeout Enable/disable IPsec tunnel idle timeout. option - disable
Option Description
enable Enable IPsec tunnel idle timeout.
disable Disable IPsec tunnel idle timeout.
idle-
timeoutinterval
IPsec tunnel idle timeout in minutes. integer Minimum
value: 5
Maximum
value: 43200
15
ike-version IKE protocol version. option - 1
Parameter Description Type Size Default
Option Description
1 Use IKEv1 protocol.
2 Use IKEv2 protocol.
inbound-dscp-
copy
Enable/disable copy the dscp in the ESP
header to the inner IP Header.
option - disable
Option Description
enable Enable copy the dscp in the ESP header to the inner IP Header.
disable Disable copy the dscp in the ESP header to the inner IP Header.
include-local-lan Enable/disable allow local LAN access on
unity clients.
option - disable
Option Description
disable Disable local LAN access on Unity clients.
enable Enable local LAN access on Unity clients.
interface Local physical, aggregate, or VLAN
outgoing interface.
string Maximum
length: 35
internal-domain-
list <domain-
name>
One or more internal domain names in
quotes separated by spaces.
Domain name.
string Maximum
length: 79
ip-delay-interval IP address reuse delay interval in seconds. integer Minimum
value: 0
Maximum
value: 28800
0
ipv4-dns-server1 IPv4 DNS server 1. ipv4-address Not
Specified
0.0.0.0
ipv4-dns-server2 IPv4 DNS server 2. ipv4-address Not
Specified
0.0.0.0
ipv4-dns-server3 IPv4 DNS server 3. ipv4-address Not
Specified
0.0.0.0
ipv4-end-ip End of IPv4 range. ipv4-address Not
Specified
0.0.0.0
ipv4-name IPv4 address name. string Maximum
length: 79
ipv4-netmask IPv4 Netmask. ipv4-
netmask
Not
Specified
255.255.255.255
Parameter Description Type Size Default
ipv4-split-
exclude
IPv4 subnets that should not be sent over
the IPsec tunnel.
string Maximum
length: 79
ipv4-split-include IPv4 split-include subnets. string Maximum
length: 79
ipv4-start-ip Start of IPv4 range. ipv4-address Not
Specified
0.0.0.0
ipv4-wins-
server1
WINS server 1. ipv4-address Not
Specified
0.0.0.0
ipv4-wins-
server2
WINS server 2. ipv4-address Not
Specified
0.0.0.0
ipv6-dns-server1 IPv6 DNS server 1. ipv6-address Not
Specified
::
ipv6-dns-server2 IPv6 DNS server 2. ipv6-address Not
Specified
::
ipv6-dns-server3 IPv6 DNS server 3. ipv6-address Not
Specified
::
ipv6-end-ip End of IPv6 range. ipv6-address Not
Specified
::
ipv6-name IPv6 address name. string Maximum
length: 79
ipv6-prefix IPv6 prefix. integer Minimum
value: 1
Maximum
value: 128
128
ipv6-split-
exclude
IPv6 subnets that should not be sent over
the IPsec tunnel.
string Maximum
length: 79
ipv6-split-include IPv6 split-include subnets. string Maximum
length: 79
ipv6-start-ip Start of IPv6 range. ipv6-address Not
Specified
::
keepalive NAT-T keep alive interval. integer Minimum
value: 5
Maximum
value: 900
10
Parameter Description Type Size Default
keylife Time to wait in seconds before phase 1
encryption key expires.
integer Minimum
value: 120
Maximum
value:
172800
86400
kms Key Management Services server. string Maximum
length: 35
link-cost VPN tunnel underlay link cost. integer Minimum
value: 0
Maximum
value: 255
0
local-gw Local VPN gateway. ipv4-address Not
Specified
0.0.0.0
localid Local ID. string Maximum
length: 63
localid-type Local ID type. option - auto
Option Description
auto Select ID type automatically.
fqdn Use fully qualified domain name.
user-fqdn Use user fully qualified domain name.
keyid Use key-id string.
address Use local IP address.
asn1dn Use ASN.1 distinguished name.
loopback-
asymroute
Enable/disable asymmetric routing for IKE
traffic on loopback interface.
option - enable
Option Description
enable Allow ingress/egress IKE traffic to be routed over different interfaces.
disable Ingress/egress IKE traffic must be routed over the same interface.
mesh-selector-
type
Add selectors containing subsets of the
configuration depending on traffic.
option - disable
Option Description
disable Disable.
subnet Enable addition of matching subnet selector.
host Enable addition of host to host selector.
Parameter Description Type Size Default
mode ID protection mode used to establish a
secure channel.
option - main
Option Description
aggressive Aggressive mode.
main Main mode.
mode-cfg Enable/disable configuration method. option - disable
Option Description
disable Disable Configuration Method.
enable Enable Configuration Method.
mode-cfg-allow-
client-selector
Enable/disable mode-cfg client to use
custom phase2 selectors.
option - disable
Option Description
disable Mode-cfg client to use wildcard selectors.
enable Mode-cfg client to use custom selectors.
name IPsec remote gateway name. string Maximum
length: 35
nattraversal Enable/disable NAT traversal. option - enable
Option Description
enable Enable IPsec NAT traversal.
disable Disable IPsec NAT traversal.
forced Force IPsec NAT traversal on.
negotiate-
timeout
IKE SA negotiation timeout in seconds. integer Minimum
value: 1
Maximum
value: 300
30
network-id VPN gateway network ID. integer Minimum
value: 0
Maximum
value: 255
0
network-overlay Enable/disable network overlays. option - disable
Parameter Description Type Size Default
Option Description
disable Disable network overlays.
enable Enable network overlays.
npu-offload * Enable/disable offloading NPU. option - enable
Option Description
enable Enable NPU offloading.
disable Disable NPU offloading.
peer Accept this peer certificate. string Maximum
length: 35
peergrp Accept this peer certificate group. string Maximum
length: 35
peerid Accept this peer identity. string Maximum
length: 255
peertype Accept this peer type. option - peer
Option Description
any Accept any peer ID.
one Accept this peer ID.
dialup Accept peer ID in dialup group.
peer Accept this peer certificate.
peergrp Accept this peer certificate group.
ppk Enable/disable IKEv2 Postquantum
Preshared Key (PPK).
option - disable
Option Description
disable Disable use of IKEv2 Postquantum Preshared Key (PPK).
allow Allow, but do not require, use of IKEv2 Postquantum Preshared Key (PPK).
require Require use of IKEv2 Postquantum Preshared Key (PPK).
ppk-identity IKEv2 Postquantum Preshared Key
Identity.
string Maximum
length: 35
ppk-secret IKEv2 Postquantum Preshared Key (ASCII
string or hexadecimal encoded with a
leading 0x).
password-3 Not
Specified
Parameter Description Type Size Default
priority Priority for routes added by IKE. integer Minimum
value: 1
Maximum
value: 65535
1
proposal Phase1 proposal. option -
Option Description
des-md5 des-md5
des-sha1 des-sha1
des-sha256 des-sha256
des-sha384 des-sha384
des-sha512 des-sha512
3des-md5 3des-md5
3des-sha1 3des-sha1
3des-sha256 3des-sha256
3des-sha384 3des-sha384
3des-sha512 3des-sha512
aes128-md5 aes128-md5
aes128-sha1 aes128-sha1
aes128-sha256 aes128-sha256
aes128-sha384 aes128-sha384
aes128-sha512 aes128-sha512
aes128gcm-prfsha1 aes128gcm-prfsha1
aes128gcm-prfsha256 aes128gcm-prfsha256
aes128gcm-prfsha384 aes128gcm-prfsha384
aes128gcm-prfsha512 aes128gcm-prfsha512
aes192-md5 aes192-md5
aes192-sha1 aes192-sha1
aes192-sha256 aes192-sha256
aes192-sha384 aes192-sha384
aes192-sha512 aes192-sha512
aes256-md5 aes256-md5
Parameter Description Type Size Default
Option Description
aes256-sha1 aes256-sha1
aes256-sha256 aes256-sha256
aes256-sha384 aes256-sha384
aes256-sha512 aes256-sha512
aes256gcm-prfsha1 aes256gcm-prfsha1
aes256gcm-prfsha256 aes256gcm-prfsha256
aes256gcm-prfsha384 aes256gcm-prfsha384
aes256gcm-prfsha512 aes256gcm-prfsha512
chacha20poly1305-prfsha1 chacha20poly1305-prfsha1
chacha20poly1305-prfsha256 chacha20poly1305-prfsha256
chacha20poly1305-prfsha384 chacha20poly1305-prfsha384
chacha20poly1305-prfsha512 chacha20poly1305-prfsha512
aria128-md5 aria128-md5
aria128-sha1 aria128-sha1
aria128-sha256 aria128-sha256
aria128-sha384 aria128-sha384
aria128-sha512 aria128-sha512
aria192-md5 aria192-md5
aria192-sha1 aria192-sha1
aria192-sha256 aria192-sha256
aria192-sha384 aria192-sha384
aria192-sha512 aria192-sha512
aria256-md5 aria256-md5
aria256-sha1 aria256-sha1
aria256-sha256 aria256-sha256
aria256-sha384 aria256-sha384
aria256-sha512 aria256-sha512
seed-md5 seed-md5
seed-sha1 seed-sha1
Parameter Description Type Size Default
Option Description
seed-sha256 seed-sha256
seed-sha384 seed-sha384
seed-sha512 seed-sha512
psksecret Pre-shared secret for PSK authentication
(ASCII string or hexadecimal encoded with
a leading 0x).
password-3 Not
Specified
psksecret-
remote
Pre-shared secret for remote side PSK
authentication (ASCII string or hexadecimal
encoded with a leading 0x).
password-3 Not
Specified
qkd Enable/disable use of Quantum Key
Distribution (QKD) server.
option - disable
Option Description
disable Disable use of a Quantum Key Distribution (QKD) server.
allow Allow, but do not require, use of a Quantum Key Distribution (QKD) server.
require Require use of a Quantum Key Distribution (QKD) server.
qkd-profile Quantum Key Distribution (QKD) server
profile.
string Maximum
length: 35
reauth Enable/disable re-authentication upon IKE
SA lifetime expiration.
option - disable
Option Description
disable Disable IKE SA re-authentication.
enable Enable IKE SA re-authentication.
rekey Enable/disable phase1 rekey. option - enable
Option Description
enable Enable phase1 rekey.
disable Disable phase1 rekey.
remote-gw Remote VPN gateway. ipv4-address Not
Specified
0.0.0.0
remote-gw-
country
IPv4 addresses associated to a specific
country.
string Maximum
length: 2
Parameter Description Type Size Default
remote-gw-end-
ip
Last IPv4 address in the range. ipv4-
address-any
Not
Specified
0.0.0.0
remote-gw-
match
Set type of IPv4 remote gateway address
matching.
option - any
Option Description
any Match any IPv4 gateway address.
ipmask Match IPv4 gateway address and mask.
iprange Match IPv4 gateway address range.
geography Match IPv4 gateway address from a specified country.
remote-gw-start-
ip
First IPv4 address in the range. ipv4-
address-any
Not
Specified
0.0.0.0
remote-gw-
subnet
IPv4 address and subnet mask. ipv4-
classnet-any
Not
Specified
0.0.0.0 0.0.0.0
remote-gw6-
country
IPv6 addresses associated to a specific
country.
string Maximum
length: 2
remote-gw6-end-
ip
Last IPv6 address in the range. ipv6-address Not
Specified
::
remote-gw6-
match
Set type of IPv6 remote gateway address
matching.
option - any
Option Description
any Match any IPv6 gateway address.
ipprefix Match IPv6 gateway address and prefix.
iprange Match IPv6 gateway address range.
geography Match IPv6 gateway address from a specified country.
remote-gw6-
start-ip
First IPv6 address in the range. ipv6-address Not
Specified
::
remote-gw6-
subnet
IPv6 address and prefix. ipv6-network Not
Specified
::/0
remotegw-ddns Domain name of remote gateway. For
example, name.ddns.com.
string Maximum
length: 63
rsa-signature-
format
Digital Signature Authentication RSA
signature format.
option - pkcs1
Parameter Description Type Size Default
Option Description
pkcs1 RSASSA PKCS#1 v1.5.
pss RSASSA Probabilistic Signature Scheme (PSS).
rsa-signature-
hash-override
Enable/disable IKEv2 RSA signature hash
algorithm override.
option - disable
Option Description
enable Enable IKEv2 RSA signature hash algorithm override.
disable Disable IKEv2 RSA signature hash algorithm override.
save-password Enable/disable saving XAuth username
and password on VPN clients.
option - disable
Option Description
disable Disable saving XAuth username and password on VPN clients.
enable Enable saving XAuth username and password on VPN clients.
send-cert-chain Enable/disable sending certificate chain. option - enable
Option Description
enable Enable sending certificate chain.
disable Disable sending certificate chain.
signature-hash-
alg
Digital Signature Authentication hash
algorithms.
option - sha2-512
Option Description
sha1 SHA1.
sha2-256 SHA2-256.
sha2-384 SHA2-384.
sha2-512 SHA2-512.
split-include-
service
Split-include services. string Maximum
length: 79
suite-b Use Suite-B. option - disable
Option Description
disable Do not use UI suite.
Parameter Description Type Size Default
Option Description
suite-b-gcm-128 Use Suite-B-GCM-128.
suite-b-gcm-256 Use Suite-B-GCM-256.
transport Set IKE transport protocol. option - udp
Option Description
udp Use UDP transport for IKE.
udp-fallback-tcp Use UDP transport for IKE, with fallback to TCP transport.
tcp Use TCP transport for IKE.
type Remote gateway type. option - static
Option Description
static Remote VPN gateway has fixed IP address.
dynamic Remote VPN gateway has dynamic IP address.
ddns Remote VPN gateway has dynamic IP address and is a dynamic DNS
client.
unity-support Enable/disable support for Cisco UNITY
Configuration Method extensions.
option - enable
Option Description
disable Disable Cisco Unity Configuration Method Extensions.
enable Enable Cisco Unity Configuration Method Extensions.
usrgrp User group name for dialup peers. string Maximum
length: 35
wizard-type GUI VPN Wizard Type. option - custom
Option Description
custom Custom VPN configuration.
dialup-forticlient Dial Up - FortiClient Windows, Mac and Android.
dialup-ios Dial Up - iPhone / iPad Native IPsec Client.
dialup-android Dial Up - Android Native IPsec Client.
dialup-windows Dial Up - Windows Native IPsec Client.
dialup-cisco Dial Up - Cisco IPsec Client.
Parameter Description Type Size Default
Option Description
static-fortigate Site to Site - FortiGate.
dialup-fortigate Dial Up - FortiGate.
static-cisco Site to Site - Cisco.
dialup-cisco-fw Dialup Up - Cisco Firewall.
simplified-static-
fortigate
Site to Site - FortiGate (SD-WAN).
hub-fortigate-
auto-discovery
Hub role in a Hub-and-Spoke auto-discovery VPN.
spoke-fortigate-
auto-discovery
Spoke role in a Hub-and-Spoke auto-discovery VPN.
xauthtype XAuth type. option - disable
Option Description
disable Disable.
client Enable as client.
pap Enable as server PAP.
chap Enable as server CHAP.
auto Enable as server auto.
- This parameter may not exist in some models.
config ipv4-exclude-range
Parameter Description Type Size Default
end-ip End of IPv4 exclusive range. ipv4-
address
Not Specified 0.0.0.0
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
start-ip Start of IPv4 exclusive range. ipv4-
address
Not Specified 0.0.0.0
config ipv6-exclude-range
Parameter Description Type Size Default
end-ip End of IPv6 exclusive range. ipv6-
address
Not Specified ::
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
start-ip Start of IPv6 exclusive range. ipv6-
address
Not Specified ::

### config vpn ipsec phase2-interface

Configure VPN autokey tunnel.

#### Syntax

config vpn ipsec phase2-interface
Description: Configure VPN autokey tunnel.
edit <name>
set add-route [phase1|enable|...]
set auto-discovery-forwarder [phase1|enable|...]
set auto-discovery-sender [phase1|enable|...]
set auto-negotiate [enable|disable]
set comments {var-string}
set dhcp-ipsec [enable|disable]
set dhgrp {option1}, {option2}, ...
set diffserv [enable|disable]
set diffservcode {user}
set dst-addr-type [subnet|range|...]
set dst-end-ip {ipv4-address-any}
set dst-end-ip6 {ipv6-address}
set dst-name {string}
set dst-name6 {string}
set dst-port {integer}
set dst-start-ip {ipv4-address-any}
set dst-start-ip6 {ipv6-address}
set dst-subnet {ipv4-classnet-any}
set dst-subnet6 {ipv6-prefix}
set encapsulation [tunnel-mode|transport-mode]
set inbound-dscp-copy [phase1|enable|...]
set initiator-ts-narrow [enable|disable]
set ipv4-df [enable|disable]
set keepalive [enable|disable]
set keylife-type [seconds|kbs|...]
set keylifekbs {integer}
set keylifeseconds {integer}
set l2tp [enable|disable]
set pfs [enable|disable]
set phase1name {string}
set proposal {option1}, {option2}, ...
set protocol {integer}
set replay [enable|disable]
set route-overlap [use-old|use-new|...]
set single-source [enable|disable]
set src-addr-type [subnet|range|...]
set src-end-ip {ipv4-address-any}
set src-end-ip6 {ipv6-address}
set src-name {string}
set src-name6 {string}
set src-port {integer}
set src-start-ip {ipv4-address-any}
set src-start-ip6 {ipv6-address}
set src-subnet {ipv4-classnet-any}
set src-subnet6 {ipv6-prefix}
next
end

#### Parameters

config vpn ipsec phase2-interface
Parameter Description Type Size Default
add-route Enable/disable automatic route addition. option - phase1
Option Description
phase1 Add route according to phase1 add-route setting.
enable Add route for remote proxy ID.
disable Do not add route for remote proxy ID.
auto-discovery-
forwarder
Enable/disable forwarding short-cut messages. option - phase1
Option Description
phase1 Forward short-cut messages according to the phase1 auto-discovery-
forwarder setting.
enable Enable forwarding auto-discovery short-cut messages.
disable Disable forwarding auto-discovery short-cut messages.
auto-discovery-
sender
Enable/disable sending short-cut messages. option - phase1
Option Description
phase1 Send short-cut messages according to the phase1 auto-discovery-sender
setting.
enable Enable sending auto-discovery short-cut messages.
disable Disable sending auto-discovery short-cut messages.
Parameter Description Type Size Default
auto-negotiate Enable/disable IPsec SA auto-negotiation. option - disable
Option Description
enable Enable setting.
disable Disable setting.
comments Comment. var-string Maximum
length: 255
dhcp-ipsec Enable/disable DHCP-IPsec. option - disable
Option Description
enable Enable setting.
disable Disable setting.
dhgrp Phase2 DH group. option - 14
Option Description
1 DH Group 1.
2 DH Group 2.
5 DH Group 5.
14 DH Group 14.
15 DH Group 15.
16 DH Group 16.
17 DH Group 17.
18 DH Group 18.
19 DH Group 19.
20 DH Group 20.
21 DH Group 21.
27 DH Group 27.
28 DH Group 28.
29 DH Group 29.
30 DH Group 30.
31 DH Group 31.
32 DH Group 32.
Parameter Description Type Size Default
diffserv Enable/disable applying DSCP value to the
IPsec tunnel outer IP header.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
diffservcode DSCP value to be applied to the IPsec tunnel
outer IP header.
user Not Specified
dst-addr-type Remote proxy ID type. option - subnet
Option Description
subnet IPv4 subnet.
range IPv4 range.
ip IPv4 IP.
name IPv4 firewall address or group name.
subnet6 IPv6 subnet.
range6 IPv6 range.
ip6 IPv6 IP.
name6 IPv6 firewall address or group name.
dst-end-ip Remote proxy ID IPv4 end. ipv4-
address-any
Not Specified 0.0.0.0
dst-end-ip6 Remote proxy ID IPv6 end. ipv6-
address
Not Specified ::
dst-name Remote proxy ID name. string Maximum
length: 79
dst-name6 Remote proxy ID name. string Maximum
length: 79
dst-port Quick mode destination port. integer Minimum
value: 0
Maximum
value: 65535
0
dst-start-ip Remote proxy ID IPv4 start. ipv4-
address-any
Not Specified 0.0.0.0
dst-start-ip6 Remote proxy ID IPv6 start. ipv6-
address
Not Specified ::
Parameter Description Type Size Default
dst-subnet Remote proxy ID IPv4 subnet. ipv4-
classnet-any
Not Specified 0.0.0.0
0.0.0.0
dst-subnet6 Remote proxy ID IPv6 subnet. ipv6-prefix Not Specified ::/0
encapsulation ESP encapsulation mode. option - tunnel-mode
Option Description
tunnel-mode Use tunnel mode encapsulation.
transport-mode Use transport mode encapsulation.
inbound-dscp-
copy
Enable/disable copying of the DSCP in the ESP
header to the inner IP header.
option - phase1
Option Description
phase1 copy the DCSP in the ESP header to the inner IP Header according to the
phase1 inbound_dscp_copy setting.
enable Enable copying of the DSCP in the ESP header to the inner IP header.
disable Disable copying of the DSCP in the ESP header to the inner IP header.
initiator-ts-
narrow
Enable/disable traffic selector narrowing for
IKEv2 initiator.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
ipv4-df Enable/disable setting and resetting of IPv4
'Don't Fragment' bit.
option - disable
Option Description
enable Set IPv4 DF the same as original packet.
disable Reset IPv4 DF.
keepalive Enable/disable keep alive. option - disable
Option Description
enable Enable setting.
disable Disable setting.
keylife-type Keylife type. option - seconds
Parameter Description Type Size Default
Option Description
seconds Key life in seconds.
kbs Key life in kilobytes.
both Key life both.
keylifekbs Phase2 key life in number of kilobytes of traffic. integer Minimum
value: 5120
Maximum
value:
4294967295
5120
keylifeseconds Phase2 key life in time in seconds. integer Minimum
value: 120
Maximum
value: 172800
43200
l2tp Enable/disable L2TP over IPsec. option - disable
Option Description
enable Enable L2TP over IPsec.
disable Disable L2TP over IPsec.
name IPsec tunnel name. string Maximum
length: 35
pfs Enable/disable PFS feature. option - enable
Option Description
enable Enable setting.
disable Disable setting.
phase1name Phase 1 determines the options required for
phase 2.
string Maximum
length: 15
proposal Phase2 proposal. option -
Option Description
null-md5 null-md5
null-sha1 null-sha1
null-sha256 null-sha256
null-sha384 null-sha384
Parameter Description Type Size Default
Option Description
null-sha512 null-sha512
des-null des-null
des-md5 des-md5
des-sha1 des-sha1
des-sha256 des-sha256
des-sha384 des-sha384
des-sha512 des-sha512
3des-null 3des-null
3des-md5 3des-md5
3des-sha1 3des-sha1
3des-sha256 3des-sha256
3des-sha384 3des-sha384
3des-sha512 3des-sha512
aes128-null aes128-null
aes128-md5 aes128-md5
aes128-sha1 aes128-sha1
aes128-sha256 aes128-sha256
aes128-sha384 aes128-sha384
aes128-sha512 aes128-sha512
aes128gcm aes128gcm
aes192-null aes192-null
aes192-md5 aes192-md5
aes192-sha1 aes192-sha1
aes192-sha256 aes192-sha256
aes192-sha384 aes192-sha384
aes192-sha512 aes192-sha512
aes256-null aes256-null
aes256-md5 aes256-md5
aes256-sha1 aes256-sha1
Parameter Description Type Size Default
Option Description
aes256-sha256 aes256-sha256
aes256-sha384 aes256-sha384
aes256-sha512 aes256-sha512
aes256gcm aes256gcm
chacha20poly1305 chacha20poly1305
aria128-null aria128-null
aria128-md5 aria128-md5
aria128-sha1 aria128-sha1
aria128-sha256 aria128-sha256
aria128-sha384 aria128-sha384
aria128-sha512 aria128-sha512
aria192-null aria192-null
aria192-md5 aria192-md5
aria192-sha1 aria192-sha1
aria192-sha256 aria192-sha256
aria192-sha384 aria192-sha384
aria192-sha512 aria192-sha512
aria256-null aria256-null
aria256-md5 aria256-md5
aria256-sha1 aria256-sha1
aria256-sha256 aria256-sha256
aria256-sha384 aria256-sha384
aria256-sha512 aria256-sha512
seed-null seed-null
seed-md5 seed-md5
seed-sha1 seed-sha1
seed-sha256 seed-sha256
seed-sha384 seed-sha384
seed-sha512 seed-sha512
Parameter Description Type Size Default
protocol Quick mode protocol selector. integer Minimum
value: 0
Maximum
value: 255
0
replay Enable/disable replay detection. option - enable
Option Description
enable Enable setting.
disable Disable setting.
route-overlap Action for overlapping routes. option - use-new
Option Description
use-old Use the old route and do not add the new route.
use-new Delete the old route and add the new route.
allow Allow overlapping routes.
single-source Enable/disable single source IP restriction. option - disable
Option Description
enable Only single source IP will be accepted.
disable Source IP range will be accepted.
src-addr-type Local proxy ID type. option - subnet
Option Description
subnet IPv4 subnet.
range IPv4 range.
ip IPv4 IP.
name IPv4 firewall address or group name.
subnet6 IPv6 subnet.
range6 IPv6 range.
ip6 IPv6 IP.
name6 IPv6 firewall address or group name.
src-end-ip Local proxy ID end. ipv4-
address-any
Not Specified 0.0.0.0
Parameter Description Type Size Default
src-end-ip6 Local proxy ID IPv6 end. ipv6-
address
Not Specified ::
src-name Local proxy ID name. string Maximum
length: 79
src-name6 Local proxy ID name. string Maximum
length: 79
src-port Quick mode source port. integer Minimum
value: 0
Maximum
value: 65535
0
src-start-ip Local proxy ID start. ipv4-
address-any
Not Specified 0.0.0.0
src-start-ip6 Local proxy ID IPv6 start. ipv6-
address
Not Specified ::
src-subnet Local proxy ID subnet. ipv4-
classnet-any
Not Specified 0.0.0.0
0.0.0.0
src-subnet6 Local proxy ID IPv6 subnet. ipv6-prefix Not Specified ::/0

### config vpn ipsec phase2

Configure VPN autokey tunnel.

#### Syntax

config vpn ipsec phase2
Description: Configure VPN autokey tunnel.
edit <name>
set add-route [phase1|enable|...]
set auto-negotiate [enable|disable]
set comments {var-string}
set dhcp-ipsec [enable|disable]
set dhgrp {option1}, {option2}, ...
set diffserv [enable|disable]
set diffservcode {user}
set dst-addr-type [subnet|range|...]
set dst-end-ip {ipv4-address-any}
set dst-end-ip6 {ipv6-address}
set dst-name {string}
set dst-name6 {string}
set dst-port {integer}
set dst-start-ip {ipv4-address-any}
set dst-start-ip6 {ipv6-address}
set dst-subnet {ipv4-classnet-any}
set dst-subnet6 {ipv6-prefix}
set encapsulation [tunnel-mode|transport-mode]
set inbound-dscp-copy [phase1|enable|...]
set initiator-ts-narrow [enable|disable]
set ipv4-df [enable|disable]
set keepalive [enable|disable]
set keylife-type [seconds|kbs|...]
set keylifekbs {integer}
set keylifeseconds {integer}
set l2tp [enable|disable]
set pfs [enable|disable]
set phase1name {string}
set proposal {option1}, {option2}, ...
set protocol {integer}
set replay [enable|disable]
set route-overlap [use-old|use-new|...]
set selector-match [exact|subset|...]
set single-source [enable|disable]
set src-addr-type [subnet|range|...]
set src-end-ip {ipv4-address-any}
set src-end-ip6 {ipv6-address}
set src-name {string}
set src-name6 {string}
set src-port {integer}
set src-start-ip {ipv4-address-any}
set src-start-ip6 {ipv6-address}
set src-subnet {ipv4-classnet-any}
set src-subnet6 {ipv6-prefix}
set use-natip [enable|disable]
next
end

#### Parameters

config vpn ipsec phase2
Parameter Description Type Size Default
add-route Enable/disable automatic route addition. option - phase1
Option Description
phase1 Add route according to phase1 add-route setting.
enable Add route for remote proxy ID.
disable Do not add route for remote proxy ID.
auto-negotiate Enable/disable IPsec SA auto-negotiation. option - disable
Option Description
enable Enable setting.
disable Disable setting.
comments Comment. var-string Maximum
length: 255
dhcp-ipsec Enable/disable DHCP-IPsec. option - disable
Parameter Description Type Size Default
Option Description
enable Enable setting.
disable Disable setting.
dhgrp Phase2 DH group. option - 14
Option Description
1 DH Group 1.
2 DH Group 2.
5 DH Group 5.
14 DH Group 14.
15 DH Group 15.
16 DH Group 16.
17 DH Group 17.
18 DH Group 18.
19 DH Group 19.
20 DH Group 20.
21 DH Group 21.
27 DH Group 27.
28 DH Group 28.
29 DH Group 29.
30 DH Group 30.
31 DH Group 31.
32 DH Group 32.
diffserv Enable/disable applying DSCP value to the
IPsec tunnel outer IP header.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
diffservcode DSCP value to be applied to the IPsec tunnel
outer IP header.
user Not Specified
dst-addr-type Remote proxy ID type. option - subnet
Parameter Description Type Size Default
Option Description
subnet IPv4 subnet.
range IPv4 range.
ip IPv4 IP.
name IPv4 firewall address or group name.
dst-end-ip Remote proxy ID IPv4 end. ipv4-
address-any
Not Specified 0.0.0.0
dst-end-ip6 Remote proxy ID IPv6 end. ipv6-
address
Not Specified ::
dst-name Remote proxy ID name. string Maximum
length: 79
dst-name6 Remote proxy ID name. string Maximum
length: 79
dst-port Quick mode destination port. integer Minimum
value: 0
Maximum
value: 65535
0
dst-start-ip Remote proxy ID IPv4 start. ipv4-
address-any
Not Specified 0.0.0.0
dst-start-ip6 Remote proxy ID IPv6 start. ipv6-
address
Not Specified ::
dst-subnet Remote proxy ID IPv4 subnet. ipv4-
classnet-any
Not Specified 0.0.0.0
0.0.0.0
dst-subnet6 Remote proxy ID IPv6 subnet. ipv6-prefix Not Specified ::/0
encapsulation ESP encapsulation mode. option - tunnel-mode
Option Description
tunnel-mode Use tunnel mode encapsulation.
transport-mode Use transport mode encapsulation.
inbound-dscp-
copy
Enable/disable copying of the DSCP in the ESP
header to the inner IP header.
option - phase1
Option Description
phase1 copy the DCSP in the ESP header to the inner IP Header according to the
phase1 inbound_dscp_copy setting.
Parameter Description Type Size Default
Option Description
enable Enable copying of the DSCP in the ESP header to the inner IP header.
disable Disable copying of the DSCP in the ESP header to the inner IP header.
initiator-ts-
narrow
Enable/disable traffic selector narrowing for
IKEv2 initiator.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
ipv4-df Enable/disable setting and resetting of IPv4
'Don't Fragment' bit.
option - disable
Option Description
enable Set IPv4 DF the same as original packet.
disable Reset IPv4 DF.
keepalive Enable/disable keep alive. option - disable
Option Description
enable Enable setting.
disable Disable setting.
keylife-type Keylife type. option - seconds
Option Description
seconds Key life in seconds.
kbs Key life in kilobytes.
both Key life both.
keylifekbs Phase2 key life in number of kilobytes of traffic. integer Minimum
value: 5120
Maximum
value:
4294967295
5120
keylifeseconds Phase2 key life in time in seconds. integer Minimum
value: 120
Maximum
value: 172800
43200
Parameter Description Type Size Default
l2tp Enable/disable L2TP over IPsec. option - disable
Option Description
enable Enable L2TP over IPsec.
disable Disable L2TP over IPsec.
name IPsec tunnel name. string Maximum
length: 35
pfs Enable/disable PFS feature. option - enable
Option Description
enable Enable setting.
disable Disable setting.
phase1name Phase 1 determines the options required for
phase 2.
string Maximum
length: 35
proposal Phase2 proposal. option -
Option Description
null-md5 null-md5
null-sha1 null-sha1
null-sha256 null-sha256
null-sha384 null-sha384
null-sha512 null-sha512
des-null des-null
des-md5 des-md5
des-sha1 des-sha1
des-sha256 des-sha256
des-sha384 des-sha384
des-sha512 des-sha512
3des-null 3des-null
3des-md5 3des-md5
3des-sha1 3des-sha1
3des-sha256 3des-sha256
Parameter Description Type Size Default
Option Description
3des-sha384 3des-sha384
3des-sha512 3des-sha512
aes128-null aes128-null
aes128-md5 aes128-md5
aes128-sha1 aes128-sha1
aes128-sha256 aes128-sha256
aes128-sha384 aes128-sha384
aes128-sha512 aes128-sha512
aes128gcm aes128gcm
aes192-null aes192-null
aes192-md5 aes192-md5
aes192-sha1 aes192-sha1
aes192-sha256 aes192-sha256
aes192-sha384 aes192-sha384
aes192-sha512 aes192-sha512
aes256-null aes256-null
aes256-md5 aes256-md5
aes256-sha1 aes256-sha1
aes256-sha256 aes256-sha256
aes256-sha384 aes256-sha384
aes256-sha512 aes256-sha512
aes256gcm aes256gcm
chacha20poly1305 chacha20poly1305
aria128-null aria128-null
aria128-md5 aria128-md5
aria128-sha1 aria128-sha1
aria128-sha256 aria128-sha256
aria128-sha384 aria128-sha384
aria128-sha512 aria128-sha512
Parameter Description Type Size Default
Option Description
aria192-null aria192-null
aria192-md5 aria192-md5
aria192-sha1 aria192-sha1
aria192-sha256 aria192-sha256
aria192-sha384 aria192-sha384
aria192-sha512 aria192-sha512
aria256-null aria256-null
aria256-md5 aria256-md5
aria256-sha1 aria256-sha1
aria256-sha256 aria256-sha256
aria256-sha384 aria256-sha384
aria256-sha512 aria256-sha512
seed-null seed-null
seed-md5 seed-md5
seed-sha1 seed-sha1
seed-sha256 seed-sha256
seed-sha384 seed-sha384
seed-sha512 seed-sha512
protocol Quick mode protocol selector. integer Minimum
value: 0
Maximum
value: 255
0
replay Enable/disable replay detection. option - enable
Option Description
enable Enable setting.
disable Disable setting.
route-overlap Action for overlapping routes. option - use-new
Option Description
use-old Use the old route and do not add the new route.
Parameter Description Type Size Default
Option Description
use-new Delete the old route and add the new route.
allow Allow overlapping routes.
selector-match Match type to use when comparing selectors. option - auto
Option Description
exact Match selectors exactly.
subset Match selectors by subset.
auto Use subset or exact match depending on selector address type.
single-source Enable/disable single source IP restriction. option - disable
Option Description
enable Only single source IP will be accepted.
disable Source IP range will be accepted.
src-addr-type Local proxy ID type. option - subnet
Option Description
subnet IPv4 subnet.
range IPv4 range.
ip IPv4 IP.
name IPv4 firewall address or group name.
src-end-ip Local proxy ID end. ipv4-
address-any
Not Specified 0.0.0.0
src-end-ip6 Local proxy ID IPv6 end. ipv6-
address
Not Specified ::
src-name Local proxy ID name. string Maximum
length: 79
src-name6 Local proxy ID name. string Maximum
length: 79
src-port Quick mode source port. integer Minimum
value: 0
Maximum
value: 65535
0
Parameter Description Type Size Default
src-start-ip Local proxy ID start. ipv4-
address-any
Not Specified 0.0.0.0
src-start-ip6 Local proxy ID IPv6 start. ipv6-
address
Not Specified ::
src-subnet Local proxy ID subnet. ipv4-
classnet-any
Not Specified 0.0.0.0
0.0.0.0
src-subnet6 Local proxy ID IPv6 subnet. ipv6-prefix Not Specified ::/0
use-natip Enable to use the FortiGate public IP as the
source selector when outbound NAT is used.
option - enable
Option Description
enable Replace source selector with interface IP when using outbound NAT.
disable Do not modify source selector when using outbound NAT.

### config vpn kmip-server

KMIP server entry configuration.

#### Syntax

config vpn kmip-server
Description: KMIP server entry configuration.
edit <name>
set interface {string}
set interface-select-method [auto|sdwan|...]
set password {password}
set server-identity-check [enable|disable]
config server-list
Description: KMIP server list.
edit <id>
set cert {string}
set port {integer}
set server {string}
set status [enable|disable]
next
end
set source-ip {string}
set ssl-min-proto-version [default|SSLv3|...]
set username {string}
next
end
