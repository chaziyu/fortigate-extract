# config firewall vip

> Source: `config firewall vip.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
Option Description
enable Enable this TTL policy.
disable Disable this TTL policy.
ttl Value/range to match against the packet's Time to
Live value.
user Not Specified

### config firewall vendor-mac

Show vendor and the MAC address they have. Read-only.

#### Syntax

config firewall vendor-mac
Description: Show vendor and the MAC address they have. Read-only.
edit <id>
set mac-number {integer}
set name {string}
set obsolete {integer}
next
end

#### Parameters

config firewall vendor-mac
Parameter Description Type Size Default
id Vendor ID. Read-only. integer Minimum
value: 0
Maximum
value:
4294967295
0
mac-number Total number of MAC addresses. Read-only. integer Minimum
value: 0
Maximum
value:
4294967295
0
name Vendor name. Read-only. string Maximum
length: 63
obsolete Indicates whether the Vendor ID can be used. Read-
only.
integer Minimum
value: 0
Maximum
value: 255
0

### config firewall vip

Configure virtual IP for IPv4.

#### Syntax

config firewall vip
Description: Configure virtual IP for IPv4.
edit <name>
set add-nat46-route [disable|enable]
set arp-reply [disable|enable]
set color {integer}
set comment {var-string}
set dns-mapping-ttl {integer}
set extaddr <name1>, <name2>, ...
set extintf {string}
set extip {user}
set extport {user}
set gratuitous-arp-interval {integer}
set gslb-domain-name {string}
set gslb-hostname {string}
config gslb-public-ips
Description: Publicly accessible IP addresses for the FortiGSLB service.
edit <index>
set ip {ipv4-address-any}
next
end
set h2-support [enable|disable]
set h3-support [enable|disable]
set http-cookie-age {integer}
set http-cookie-domain {string}
set http-cookie-domain-from-host [disable|enable]
set http-cookie-generation {integer}
set http-cookie-path {string}
set http-cookie-share [disable|same-ip]
set http-ip-header [enable|disable]
set http-ip-header-name {string}
set http-multiplex [enable|disable]
set http-multiplex-max-concurrent-request {integer}
set http-multiplex-max-request {integer}
set http-multiplex-ttl {integer}
set http-redirect [enable|disable]
set https-cookie-secure [disable|enable]
set id {integer}
set ipv6-mappedip {user}
set ipv6-mappedport {user}
set ldb-method [static|round-robin|...]
set mapped-addr {string}
set mappedip <range1>, <range2>, ...
set mappedport {user}
set max-embryonic-connections {integer}
set monitor <name1>, <name2>, ...
set nat-source-vip [disable|enable]
set nat44 [disable|enable]
set nat46 [disable|enable]
set one-click-gslb-server [disable|enable]
set outlook-web-access [disable|enable]
set persistence [none|http-cookie|...]
set portforward [disable|enable]
set portmapping-type [1-to-1|m-to-n]
set protocol [tcp|udp|...]
config quic
Description: QUIC setting.
set ack-delay-exponent {integer}
set active-connection-id-limit {integer}
set active-migration [enable|disable]
set grease-quic-bit [enable|disable]
set max-ack-delay {integer}
set max-datagram-frame-size {integer}
set max-idle-timeout {integer}
set max-udp-payload-size {integer}
end
config realservers
Description: Select the real servers that this server load balancing VIP will
distribute traffic to.
edit <id>
set address {string}
set client-ip {user}
set healthcheck [disable|enable|...]
set holddown-interval {integer}
set http-host {string}
set ip {user}
set max-connections {integer}
set monitor <name1>, <name2>, ...
set port {integer}
set status [active|standby|...]
set translate-host [enable|disable]
set type [ip|address]
set weight {integer}
next
end
set server-type [http|https|...]
set service <name1>, <name2>, ...
set src-filter <range1>, <range2>, ...
set src-vip-filter [disable|enable]
set srcintf-filter <interface-name1>, <interface-name2>, ...
set ssl-accept-ffdhe-groups [enable|disable]
set ssl-algorithm [high|medium|...]
set ssl-certificate <name1>, <name2>, ...
config ssl-cipher-suites
Description: SSL/TLS cipher suites acceptable from a client, ordered by
priority.
edit <priority>
set cipher [TLS-AES-128-GCM-SHA256|TLS-AES-256-GCM-SHA384|...]
set versions {option1}, {option2}, ...
next
end
set ssl-client-fallback [disable|enable]
set ssl-client-rekey-count {integer}
set ssl-client-renegotiation [allow|deny|...]
set ssl-client-session-state-max {integer}
set ssl-client-session-state-timeout {integer}
set ssl-client-session-state-type [disable|time|...]
set ssl-dh-bits [768|1024|...]
set ssl-hpkp [disable|enable|...]
set ssl-hpkp-age {integer}
set ssl-hpkp-backup {string}
set ssl-hpkp-include-subdomains [disable|enable]
set ssl-hpkp-primary {string}
set ssl-hpkp-report-uri {var-string}
set ssl-hsts [disable|enable]
set ssl-hsts-age {integer}
set ssl-hsts-include-subdomains [disable|enable]
set ssl-http-location-conversion [enable|disable]
set ssl-http-match-host [enable|disable]
set ssl-max-version [ssl-3.0|tls-1.0|...]
set ssl-min-version [ssl-3.0|tls-1.0|...]
set ssl-mode [half|full]
set ssl-pfs [require|deny|...]
set ssl-send-empty-frags [enable|disable]
set ssl-server-algorithm [high|medium|...]
config ssl-server-cipher-suites
Description: SSL/TLS cipher suites to offer to a server, ordered by priority.
edit <priority>
set cipher [TLS-AES-128-GCM-SHA256|TLS-AES-256-GCM-SHA384|...]
set versions {option1}, {option2}, ...
next
end
set ssl-server-max-version [ssl-3.0|tls-1.0|...]
set ssl-server-min-version [ssl-3.0|tls-1.0|...]
set ssl-server-renegotiation [enable|disable]
set ssl-server-session-state-max {integer}
set ssl-server-session-state-timeout {integer}
set ssl-server-session-state-type [disable|time|...]
set status [disable|enable]
set type [static-nat|load-balance|...]
set uuid {uuid}
set weblogic-server [disable|enable]
set websphere-server [disable|enable]
next
end

#### Parameters

config firewall vip
Parameter Description Type Size Default
add-nat46-route Enable/disable adding NAT46 route. option - enable
Option Description
disable Disable adding NAT46 route.
enable Enable adding NAT46 route.
arp-reply Enable to respond to ARP requests for this
virtual IP address. Enabled by default.
option - enable
Option Description
disable Disable ARP reply.
enable Enable ARP reply.
Parameter Description Type Size Default
color Color of icon on the GUI. integer Minimum
value: 0
Maximum
value: 32
0
comment Comment. var-string Maximum
length: 255
dns-mapping-ttl DNS mapping TTL. integer Minimum
value: 0
Maximum
value: 604800
0
extaddr <name> External FQDN address name.
Address name.
string Maximum
length: 79
extintf Interface connected to the source network
that receives the packets that will be
forwarded to the destination network.
string Maximum
length: 35
extip IP address or address range on the external
interface that you want to map to an address
or address range on the destination network.
user Not Specified
extport Incoming port number range that you want to
map to a port number range on the
destination network.
user Not Specified
gratuitous-arp-
interval
Enable to have the VIP send gratuitous
ARPs. 0=disabled. Set from 5 up to 8640000
seconds to enable.
integer Minimum
value: 5
Maximum
value:
8640000
0
gslb-domain-
name
Domain to use when integrating with
FortiGSLB.
string Maximum
length: 255
gslb-hostname Hostname to use within the configured
FortiGSLB domain.
string Maximum
length: 35
h2-support Enable/disable HTTP2 support. option - enable
Option Description
enable Enable HTTP2 support.
disable Disable HTTP2 support.
h3-support Enable/disable HTTP3/QUIC support. option - disable
Parameter Description Type Size Default
Option Description
enable Enable HTTP3/QUIC support.
disable Disable HTTP3/QUIC support.
http-cookie-age Time in minutes that client web browsers
should keep a cookie. Default is 60 minutes.
0 = no time limit.
integer Minimum
value: 0
Maximum
value: 525600
60
http-cookie-
domain
Domain that HTTP cookie persistence
should apply to.
string Maximum
length: 35
http-cookie-
domain-from-
host
Enable/disable use of HTTP cookie domain
from host field in HTTP.
option - disable
Option Description
disable Disable use of HTTP cookie domain from host field in HTTP (use http-
cooke-domain setting).
enable Enable use of HTTP cookie domain from host field in HTTP.
http-cookie-
generation
Generation of HTTP cookie to be accepted.
Changing invalidates all existing cookies.
integer Minimum
value: 0
Maximum
value:
4294967295
0
http-cookie-path Limit HTTP cookie persistence to the
specified path.
string Maximum
length: 35
http-cookie-share Control sharing of cookies across virtual
servers. Use of same-ip means a cookie from
one virtual server can be used by another.
Disable stops cookie sharing.
option - same-ip
Option Description
disable Only allow HTTP cookie to match this virtual server.
same-ip Allow HTTP cookie to match any virtual server with same IP.
http-ip-header For HTTP multiplexing, enable to add the
original client IP address in the XForwarded-
For HTTP header.
option - disable
Parameter Description Type Size Default
Option Description
enable Enable adding HTTP header.
disable Disable adding HTTP header.
http-ip-header-
name
For HTTP multiplexing, enter a custom
HTTPS header name. The original client IP
address is added to this header. If empty, X-
Forwarded-For is used.
string Maximum
length: 35
http-multiplex Enable/disable HTTP multiplexing. option - disable
Option Description
enable Enable HTTP session multiplexing.
disable Disable HTTP session multiplexing.
http-multiplex-
max-concurrent-
request
Maximum number of concurrent requests
that a multiplex server can handle.
integer Minimum
value: 0
Maximum
value:
2147483647
0
http-multiplex-
max-request
Maximum number of requests that a
multiplex server can handle before
disconnecting sessions.
integer Minimum
value: 0
Maximum
value:
2147483647
0
http-multiplex-ttl Time-to-live for idle connections to servers. integer Minimum
value: 0
Maximum
value:
2147483647
15
http-redirect Enable/disable redirection of HTTP to
HTTPS.
option - disable
Option Description
enable Enable redirection of HTTP to HTTPS.
disable Disable redirection of HTTP to HTTPS.
https-cookie-
secure
Enable/disable verification that inserted
HTTPS cookies are secure.
option - disable
Parameter Description Type Size Default
Option Description
disable Do not mark cookie as secure, allow sharing between an HTTP and HTTPS
connection.
enable Mark inserted cookie as secure, cookie can only be used for HTTPS a
connection.
id Custom defined ID. integer Minimum
value: 0
Maximum
value: 65535
0
ipv6-mappedip Range of mapped IPv6 addresses. Specify
the start IPv6 address followed by a space
and the end IPv6 address.
user Not Specified
ipv6-mappedport IPv6 port number range on the destination
network to which the external port number
range is mapped.
user Not Specified
ldb-method Method used to distribute sessions to real
servers.
option - static
Option Description
static Distribute to server based on source IP.
round-robin Distribute to server based round robin order.
weighted Distribute to server based on weight.
least-session Distribute to server with lowest session count.
least-rtt Distribute to server with lowest Round-Trip-Time.
first-alive Distribute to the first server that is alive.
http-host Distribute to server based on host field in HTTP header.
mapped-addr Mapped FQDN address name. string Maximum
length: 79
mappedip
<range>
IP address or address range on the
destination network to which the external IP
address is mapped.
Mapped IP range.
string Maximum
length: 79
mappedport Port number range on the destination
network to which the external port number
range is mapped.
user Not Specified
Parameter Description Type Size Default
max-embryonic-
connections
Maximum number of incomplete
connections.
integer Minimum
value: 0
Maximum
value: 100000
1000
monitor <name> Name of the health check monitor to use
when polling to determine a virtual server's
connectivity status.
Health monitor name.
string Maximum
length: 79
name Virtual IP name. string Maximum
length: 79
nat-source-vip Enable/disable forcing the source NAT
mapped IP to the external IP for all traffic.
option - disable
Option Description
disable Force only the source NAT mapped IP to the external IP for traffic
egressing the external interface of the VIP.
enable Force the source NAT mapped IP to the external IP for all traffic.
nat44 Enable/disable NAT44. option - enable
Option Description
disable Disable NAT44.
enable Enable NAT44.
nat46 Enable/disable NAT46. option - disable
Option Description
disable Disable NAT46.
enable Enable NAT46.
one-click-gslb-
server
Enable/disable one click GSLB server
integration with FortiGSLB.
option - disable
Option Description
disable Disable integration with FortiGSLB.
enable Enable integration with FortiGSLB.
outlook-web-
access
Enable to add the Front-End-Https header
for Microsoft Outlook Web Access.
option - disable
Parameter Description Type Size Default
Option Description
disable Disable Outlook Web Access support.
enable Enable Outlook Web Access support.
persistence Configure how to make sure that clients
connect to the same server every time they
make a request that is part of the same
session.
option - none
Option Description
none None.
http-cookie HTTP cookie.
ssl-session-id SSL session ID.
portforward Enable/disable port forwarding. option - disable
Option Description
disable Disable port forward.
enable Enable port forward.
portmapping-
type
Port mapping type. option - 1-to-1
Option Description
1-to-1 One to one.
m-to-n Many to many.
protocol Protocol to use when forwarding packets. option - tcp
Option Description
tcp TCP.
udp UDP.
sctp SCTP.
icmp ICMP.
server-type Protocol to be load balanced by the virtual
server (also called the server load balance
virtual IP).
option -
Parameter Description Type Size Default
Option Description
http HTTP.
https HTTPS.
imaps IMAPS.
pop3s POP3S.
smtps SMTPS.
ssl SSL.
tcp TCP.
udp UDP.
ip IP.
service <name> Service name.
Service name.
string Maximum
length: 79
src-filter
<range>
Source address filter. Each address must be
either an IP/subnet (x.x.x.x/n) or a range
(x.x.x.x-y.y.y.y). Separate addresses with
spaces.
Source-filter range.
string Maximum
length: 79
src-vip-filter Enable/disable use of 'src-filter' to match
destinations for the reverse SNAT rule.
option - disable
Option Description
disable Match any destination for the reverse SNAT rule.
enable Match only destinations in 'src-filter' for the reverse SNAT rule.
srcintf-filter
<interface-
name>
Interfaces to which the VIP applies. Separate
the names with spaces.
Interface name.
string Maximum
length: 79
ssl-accept-ffdhe-
groups
Enable/disable FFDHE cipher suite for SSL
key exchange.
option - enable
Option Description
enable Accept FFDHE groups.
disable Do not accept FFDHE groups.
ssl-algorithm Permitted encryption algorithms for SSL
sessions according to encryption strength.
option - high
Parameter Description Type Size Default
Option Description
high High encryption. Allow only AES and ChaCha.
medium Medium encryption. Allow AES, ChaCha, 3DES, and RC4.
low Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.
custom Custom encryption. Use config ssl-cipher-suites to select the cipher suites
that are allowed.
ssl-certificate
<name>
Name of the certificate to use for SSL
handshake.
Certificate list.
string Maximum
length: 79
ssl-client-fallback Enable/disable support for preventing
Downgrade Attacks on client connections
(RFC 7507).
option - enable
Option Description
disable Disable.
enable Enable.
ssl-client-rekey-
count
Maximum length of data in MB before
triggering a client rekey (0 = disable).
integer Minimum
value: 200
Maximum
value:
1048576
0
ssl-client-
renegotiation
Allow, deny, or require secure renegotiation
of client sessions to comply with RFC 5746.
option - secure
Option Description
allow Allow a SSL client to renegotiate.
deny Abort any client initiated SSL re-negotiation attempt.
secure Abort any client initiated SSL re-negotiation attempt that does not use RFC
5746 Secure Renegotiation.
ssl-client-
session-state-
max
Maximum number of client to FortiGate SSL
session states to keep.
integer Minimum
value: 1
Maximum
value: 10000
1000
ssl-client-
session-state-
timeout
Number of minutes to keep client to
FortiGate SSL session state.
integer Minimum
value: 1
Maximum
value: 14400
30
Parameter Description Type Size Default
ssl-client-
session-state-
type
How to expire SSL sessions for the segment
of the SSL connection between the client and
the FortiGate.
option - both
Option Description
disable Do not keep session states.
time Expire session states after this many minutes.
count Expire session states when this maximum is reached.
both Expire session states based on time or count, whichever occurs first.
ssl-dh-bits Number of bits to use in the Diffie-Hellman
exchange for RSA encryption of SSL
sessions.
option - 2048
Option Description
768 768-bit Diffie-Hellman prime.
1024 1024-bit Diffie-Hellman prime.
1536 1536-bit Diffie-Hellman prime.
2048 2048-bit Diffie-Hellman prime.
3072 3072-bit Diffie-Hellman prime.
4096 4096-bit Diffie-Hellman prime.
ssl-hpkp Enable/disable including HPKP header in
response.
option - disable
Option Description
disable Do not add a HPKP header to each HTTP response.
enable Add a HPKP header to each a HTTP response.
report-only Add a HPKP Report-Only header to each HTTP response.
ssl-hpkp-age Number of seconds the client should honor
the HPKP setting.
integer Minimum
value: 60
Maximum
value:
157680000
5184000
ssl-hpkp-backup Certificate to generate backup HPKP pin
from.
string Maximum
length: 79
ssl-hpkp-include-
subdomains
Indicate that HPKP header applies to all
subdomains.
option - disable
Parameter Description Type Size Default
Option Description
disable HPKP header does not apply to subdomains.
enable HPKP header applies to subdomains.
ssl-hpkp-primary Certificate to generate primary HPKP pin
from.
string Maximum
length: 79
ssl-hpkp-report-
uri
URL to report HPKP violations to. var-string Maximum
length: 255
ssl-hsts Enable/disable including HSTS header in
response.
option - disable
Option Description
disable Do not add a HSTS header to each a HTTP response.
enable Add a HSTS header to each HTTP response.
ssl-hsts-age Number of seconds the client should honor
the HSTS setting.
integer Minimum
value: 60
Maximum
value:
157680000
5184000
ssl-hsts-include-
subdomains
Indicate that HSTS header applies to all
subdomains.
option - disable
Option Description
disable HSTS header does not apply to subdomains.
enable HSTS header applies to subdomains.
ssl-http-location-
conversion
Enable to replace HTTP with HTTPS in the
reply's Location HTTP header field.
option - disable
Option Description
enable Enable HTTP location conversion.
disable Disable HTTP location conversion.
ssl-http-match-
host
Enable/disable HTTP host matching for
location conversion.
option - enable
Option Description
enable Match HTTP host in response header.
disable Do not match HTTP host.
Parameter Description Type Size Default
ssl-max-version Highest SSL/TLS version acceptable from a
client.
option - tls-1.3
Option Description
ssl-3.0 SSL 3.0.
tls-1.0 TLS 1.0.
tls-1.1 TLS 1.1.
tls-1.2 TLS 1.2.
tls-1.3 TLS 1.3.
ssl-min-version Lowest SSL/TLS version acceptable from a
client.
option - tls-1.1
Option Description
ssl-3.0 SSL 3.0.
tls-1.0 TLS 1.0.
tls-1.1 TLS 1.1.
tls-1.2 TLS 1.2.
tls-1.3 TLS 1.3.
ssl-mode Apply SSL offloading between the client and
the FortiGate (half) or from the client to the
FortiGate and from the FortiGate to the
server (full).
option - half
Option Description
half Client to FortiGate SSL.
full Client to FortiGate and FortiGate to Server SSL.
ssl-pfs Select the cipher suites that can be used for
SSL perfect forward secrecy (PFS). Applies
to both client and server sessions.
option - require
Option Description
require Allow only Diffie-Hellman cipher-suites, so PFS is applied.
deny Allow only non-Diffie-Hellman cipher-suites, so PFS is not applied.
allow Allow use of any cipher suite so PFS may or may not be used depending on
the cipher suite selected.
Parameter Description Type Size Default
ssl-send-empty-
frags
Enable/disable sending empty fragments to
avoid CBC IV attacks (SSL 3.0 & TLS 1.0
only). May need to be disabled for
compatibility with older systems.
option - enable
Option Description
enable Send empty fragments.
disable Do not send empty fragments.
ssl-server-
algorithm
Permitted encryption algorithms for the
server side of SSL full mode sessions
according to encryption strength.
option - client
Option Description
high High encryption. Allow only AES and ChaCha.
medium Medium encryption. Allow AES, ChaCha, 3DES, and RC4.
low Low encryption. Allow AES, ChaCha, 3DES, RC4, and DES.
custom Custom encryption. Use ssl-server-cipher-suites to select the cipher suites
that are allowed.
client Use the same encryption algorithms for both client and server sessions.
ssl-server-max-
version
Highest SSL/TLS version acceptable from a
server. Use the client setting by default.
option - client
Option Description
ssl-3.0 SSL 3.0.
tls-1.0 TLS 1.0.
tls-1.1 TLS 1.1.
tls-1.2 TLS 1.2.
tls-1.3 TLS 1.3.
client Use same value as client configuration.
ssl-server-min-
version
Lowest SSL/TLS version acceptable from a
server. Use the client setting by default.
option - client
Option Description
ssl-3.0 SSL 3.0.
tls-1.0 TLS 1.0.
Parameter Description Type Size Default
Option Description
tls-1.1 TLS 1.1.
tls-1.2 TLS 1.2.
tls-1.3 TLS 1.3.
client Use same value as client configuration.
ssl-server-
renegotiation
Enable/disable secure renegotiation to
comply with RFC 5746.
option - enable
Option Description
enable Enable secure renegotiation.
disable Disable secure renegotiation.
ssl-server-
session-state-
max
Maximum number of FortiGate to Server SSL
session states to keep.
integer Minimum
value: 1
Maximum
value: 10000
100
ssl-server-
session-state-
timeout
Number of minutes to keep FortiGate to
Server SSL session state.
integer Minimum
value: 1
Maximum
value: 14400
60
ssl-server-
session-state-
type
How to expire SSL sessions for the segment
of the SSL connection between the server
and the FortiGate.
option - both
Option Description
disable Do not keep session states.
time Expire session states after this many minutes.
count Expire session states when this maximum is reached.
both Expire session states based on time or count, whichever occurs first.
status Enable/disable VIP. option - enable
Option Description
disable Disable the VIP.
enable Enable the VIP.
Parameter Description Type Size Default
type Configure a static NAT, load balance, server
load balance, access proxy, DNS translation,
or FQDN VIP.
option - static-nat
Option Description
static-nat Static NAT.
load-balance Load balance.
server-load-
balance
Server load balance.
dns-translation DNS translation.
fqdn Fully qualified domain name.
access-proxy Access proxy.
uuid Universally Unique Identifier (UUID;
automatically assigned but can be manually
reset).
uuid Not Specified 00000000-0000-
0000-0000-
000000000000
weblogic-server Enable to add an HTTP header to indicate
SSL offloading for a WebLogic server.
option - disable
Option Description
disable Do not add HTTP header indicating SSL offload for WebLogic server.
enable Add HTTP header indicating SSL offload for WebLogic server.
websphere-
server
Enable to add an HTTP header to indicate
SSL offloading for a WebSphere server.
option - disable
Option Description
disable Do not add HTTP header indicating SSL offload for WebSphere server.
enable Add HTTP header indicating SSL offload for WebSphere server.
config gslb-public-ips
Parameter Description Type Size Default
index Index of this public IP setting. integer Minimum
value: 0
Maximum
value:
4294967295
0
ip The publicly accessible IP address. ipv4-
address-
any
Not Specified 0.0.0.0
config quic
Parameter Description Type Size Default
ack-delay-
exponent
ACK delay exponent. integer Minimum
value: 1
Maximum
value: 20
3
active-
connection-id-
limit
Active connection ID limit. integer Minimum
value: 1
Maximum
value: 8
2
active-
migration
Enable/disable active migration. option - disable
Option Description
enable Enable active migration.
disable Disable active migration.
grease-quic-
bit
Enable/disable grease QUIC bit. option - enable
Option Description
enable Enable grease QUIC bit.
disable Disable grease QUIC bit.
max-ack-
delay
Maximum ACK delay in milliseconds. integer Minimum
value: 1
Maximum
value:
16383
25
max-
datagram-
frame-size
Maximum datagram frame size in bytes. integer Minimum
value: 1
Maximum
value: 1500
1500
max-idle-
timeout
Maximum idle timeout milliseconds. integer Minimum
value: 1
Maximum
value:
60000
30000
max-udp-
payload-size
Maximum UDP payload size in bytes. integer Minimum
value: 1200
Maximum
value: 1500
1500
config realservers
Parameter Description Type Size Default
address Dynamic address of the real server. string Maximum
length: 79
client-ip Only clients in this IP range can connect to this real
server.
user Not Specified
healthcheck Enable to check the responsiveness of the real
server before forwarding traffic.
option - vip
Option Description
disable Disable per server health check.
enable Enable per server health check.
vip Use health check defined in VIP.
holddown-
interval
Time in seconds that the system waits before re-
activating a previously down active server in the
active-standby mode. This is to prevent any flapping
issues.
integer Minimum
value: 30
Maximum
value: 65535
300
http-host HTTP server domain name in HTTP header. string Maximum
length: 63
id Real server ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
ip IP address of the real server. user Not Specified
max-
connections
Max number of active connections that can be
directed to the real server. When reached, sessions
are sent to other real servers.
integer Minimum
value: 0
Maximum
value:
2147483647
0
monitor
<name>
Name of the health check monitor to use when
polling to determine a virtual server's connectivity
status.
Health monitor name.
string Maximum
length: 79
port Port for communicating with the real server. Required
if port forwarding is enabled.
integer Minimum
value: 1
Maximum
value: 65535
0
Parameter Description Type Size Default
status Set the status of the real server to active so that it can
accept traffic, or on standby or disabled so no traffic
is sent.
option - active
Option Description
active Server status active.
standby Server status standby.
disable Server status disable.
translate-host Enable/disable translation of hostname/IP from
virtual server to real server.
option - enable
Option Description
enable Enable virtual hostname/IP translation.
disable Disable virtual hostname/IP translation.
type Type of address. option - ip
Option Description
ip Standard IPv4 address.
address Dynamic address object.
weight Weight of the real server. If weighted load balancing
is enabled, the server with the highest weight gets
more connections.
integer Minimum
value: 1
Maximum
value: 255
1
config ssl-cipher-suites
Parameter Description Type Size Default
cipher Cipher suite name. option -
Option Description
TLS-AES-128-
GCM-SHA256
Cipher suite TLS-AES-128-GCM-SHA256.
TLS-AES-256-
GCM-SHA384
Cipher suite TLS-AES-256-GCM-SHA384.
Parameter Description Type Size Default
Option Description
TLS-
CHACHA20-
POLY1305-
SHA256
Cipher suite TLS-CHACHA20-POLY1305-SHA256.
TLS-ECDHE-
RSA-WITH-
CHACHA20-
POLY1305-
SHA256
Cipher suite TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-ECDHE-
ECDSA-WITH-
CHACHA20-
POLY1305-
SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-DHE-RSA-
WITH-
CHACHA20-
POLY1305-
SHA256
Cipher suite TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-DHE-RSA-
WITH-AES-128-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA.
TLS-DHE-RSA-
WITH-AES-256-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA.
TLS-DHE-RSA-
WITH-AES-128-
CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-DHE-RSA-
WITH-AES-128-
GCM-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-DHE-RSA-
WITH-AES-256-
CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA256.
TLS-DHE-RSA-
WITH-AES-256-
GCM-SHA384
Cipher suite TLS-DHE-RSA-WITH-AES-256-GCM-SHA384.
Parameter Description Type Size Default
Option Description
TLS-DHE-DSS-
WITH-AES-128-
CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA.
TLS-DHE-DSS-
WITH-AES-256-
CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA.
TLS-DHE-DSS-
WITH-AES-128-
CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA256.
TLS-DHE-DSS-
WITH-AES-128-
GCM-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-GCM-SHA256.
TLS-DHE-DSS-
WITH-AES-256-
CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA256.
TLS-DHE-DSS-
WITH-AES-256-
GCM-SHA384
Cipher suite TLS-DHE-DSS-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-
RSA-WITH-AES-
128-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-
RSA-WITH-AES-
128-CBC-
SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-ECDHE-
RSA-WITH-AES-
128-GCM-
SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-
RSA-WITH-AES-
256-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA.
TLS-ECDHE-
RSA-WITH-AES-
256-CBC-
SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384.
Parameter Description Type Size Default
Option Description
TLS-ECDHE-
RSA-WITH-AES-
256-GCM-
SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-
ECDSA-WITH-
AES-128-CBC-
SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-
ECDSA-WITH-
AES-128-CBC-
SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256.
TLS-ECDHE-
ECDSA-WITH-
AES-128-GCM-
SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-
ECDSA-WITH-
AES-256-CBC-
SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA.
TLS-ECDHE-
ECDSA-WITH-
AES-256-CBC-
SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-
ECDSA-WITH-
AES-256-GCM-
SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384.
TLS-RSA-WITH-
AES-128-CBC-
SHA
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA.
TLS-RSA-WITH-
AES-256-CBC-
SHA
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA.
TLS-RSA-WITH-
AES-128-CBC-
SHA256
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA256.
Parameter Description Type Size Default
Option Description
TLS-RSA-WITH-
AES-128-GCM-
SHA256
Cipher suite TLS-RSA-WITH-AES-128-GCM-SHA256.
TLS-RSA-WITH-
AES-256-CBC-
SHA256
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA256.
TLS-RSA-WITH-
AES-256-GCM-
SHA384
Cipher suite TLS-RSA-WITH-AES-256-GCM-SHA384.
TLS-RSA-WITH-
CAMELLIA-128-
CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-RSA-WITH-
CAMELLIA-256-
CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA.
TLS-RSA-WITH-
CAMELLIA-128-
CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-RSA-WITH-
CAMELLIA-256-
CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-
WITH-3DES-
EDE-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-DHE-RSA-
WITH-
CAMELLIA-128-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-DHE-DSS-
WITH-
CAMELLIA-128-
CBC-SHA
Cipher suite TLS-DSS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-DHE-RSA-
WITH-
CAMELLIA-256-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA.
Parameter Description Type Size Default
Option Description
TLS-DHE-DSS-
WITH-
CAMELLIA-256-
CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA.
TLS-DHE-RSA-
WITH-
CAMELLIA-128-
CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-DSS-
WITH-
CAMELLIA-128-
CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-RSA-
WITH-
CAMELLIA-256-
CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-DSS-
WITH-
CAMELLIA-256-
CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-
WITH-SEED-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-SEED-CBC-SHA.
TLS-DHE-DSS-
WITH-SEED-
CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-SEED-CBC-SHA.
TLS-DHE-RSA-
WITH-ARIA-128-
CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-RSA-
WITH-ARIA-256-
CBC-SHA384
Cipher suite TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-DHE-DSS-
WITH-ARIA-128-
CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-DSS-
WITH-ARIA-256-
CBC-SHA384
Cipher suite TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384.
Parameter Description Type Size Default
Option Description
TLS-RSA-WITH-
SEED-CBC-SHA
Cipher suite TLS-RSA-WITH-SEED-CBC-SHA.
TLS-RSA-WITH-
ARIA-128-CBC-
SHA256
Cipher suite TLS-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-RSA-WITH-
ARIA-256-CBC-
SHA384
Cipher suite TLS-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-
RSA-WITH-
ARIA-128-CBC-
SHA256
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-ECDHE-
RSA-WITH-
ARIA-256-CBC-
SHA384
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-
ECDSA-WITH-
ARIA-128-CBC-
SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC_SHA256.
TLS-ECDHE-
ECDSA-WITH-
ARIA-256-CBC-
SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC_SHA384.
TLS-ECDHE-
RSA-WITH-RC4-
128-SHA
Cipher suite TLS-ECDHE-RSA-WITH-RC4-128-SHA.
TLS-ECDHE-
RSA-WITH-
3DES-EDE-
CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-DHE-DSS-
WITH-3DES-
EDE-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA.
TLS-RSA-WITH-
3DES-EDE-
CBC-SHA
Cipher suite TLS-RSA-WITH-3DES-EDE-CBC-SHA.
Parameter Description Type Size Default
Option Description
TLS-RSA-WITH-
RC4-128-MD5
Cipher suite TLS-RSA-WITH-RC4-128-MD5.
TLS-RSA-WITH-
RC4-128-SHA
Cipher suite TLS-RSA-WITH-RC4-128-SHA.
TLS-DHE-RSA-
WITH-DES-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-DES-CBC-SHA.
TLS-DHE-DSS-
WITH-DES-
CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-DES-CBC-SHA.
TLS-RSA-WITH-
DES-CBC-SHA
Cipher suite TLS-RSA-WITH-DES-CBC-SHA.
priority SSL/TLS cipher suites priority. integer Minimum
value: 0
Maximum
value:
4294967295
0
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
config ssl-server-cipher-suites
Parameter Description Type Size Default
cipher Cipher suite name. option -
Parameter Description Type Size Default
Option Description
TLS-AES-128-
GCM-SHA256
Cipher suite TLS-AES-128-GCM-SHA256.
TLS-AES-256-
GCM-SHA384
Cipher suite TLS-AES-256-GCM-SHA384.
TLS-
CHACHA20-
POLY1305-
SHA256
Cipher suite TLS-CHACHA20-POLY1305-SHA256.
TLS-ECDHE-
RSA-WITH-
CHACHA20-
POLY1305-
SHA256
Cipher suite TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-ECDHE-
ECDSA-WITH-
CHACHA20-
POLY1305-
SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-DHE-RSA-
WITH-
CHACHA20-
POLY1305-
SHA256
Cipher suite TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256.
TLS-DHE-RSA-
WITH-AES-128-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA.
TLS-DHE-RSA-
WITH-AES-256-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA.
TLS-DHE-RSA-
WITH-AES-128-
CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-DHE-RSA-
WITH-AES-128-
GCM-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-DHE-RSA-
WITH-AES-256-
CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-AES-256-CBC-SHA256.
Parameter Description Type Size Default
Option Description
TLS-DHE-RSA-
WITH-AES-256-
GCM-SHA384
Cipher suite TLS-DHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-DHE-DSS-
WITH-AES-128-
CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA.
TLS-DHE-DSS-
WITH-AES-256-
CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA.
TLS-DHE-DSS-
WITH-AES-128-
CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-CBC-SHA256.
TLS-DHE-DSS-
WITH-AES-128-
GCM-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-128-GCM-SHA256.
TLS-DHE-DSS-
WITH-AES-256-
CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-AES-256-CBC-SHA256.
TLS-DHE-DSS-
WITH-AES-256-
GCM-SHA384
Cipher suite TLS-DHE-DSS-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-
RSA-WITH-AES-
128-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-
RSA-WITH-AES-
128-CBC-
SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256.
TLS-ECDHE-
RSA-WITH-AES-
128-GCM-
SHA256
Cipher suite TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-
RSA-WITH-AES-
256-CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA.
Parameter Description Type Size Default
Option Description
TLS-ECDHE-
RSA-WITH-AES-
256-CBC-
SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-
RSA-WITH-AES-
256-GCM-
SHA384
Cipher suite TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384.
TLS-ECDHE-
ECDSA-WITH-
AES-128-CBC-
SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA.
TLS-ECDHE-
ECDSA-WITH-
AES-128-CBC-
SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256.
TLS-ECDHE-
ECDSA-WITH-
AES-128-GCM-
SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256.
TLS-ECDHE-
ECDSA-WITH-
AES-256-CBC-
SHA
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA.
TLS-ECDHE-
ECDSA-WITH-
AES-256-CBC-
SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384.
TLS-ECDHE-
ECDSA-WITH-
AES-256-GCM-
SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384.
TLS-RSA-WITH-
AES-128-CBC-
SHA
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA.
TLS-RSA-WITH-
AES-256-CBC-
SHA
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA.
Parameter Description Type Size Default
Option Description
TLS-RSA-WITH-
AES-128-CBC-
SHA256
Cipher suite TLS-RSA-WITH-AES-128-CBC-SHA256.
TLS-RSA-WITH-
AES-128-GCM-
SHA256
Cipher suite TLS-RSA-WITH-AES-128-GCM-SHA256.
TLS-RSA-WITH-
AES-256-CBC-
SHA256
Cipher suite TLS-RSA-WITH-AES-256-CBC-SHA256.
TLS-RSA-WITH-
AES-256-GCM-
SHA384
Cipher suite TLS-RSA-WITH-AES-256-GCM-SHA384.
TLS-RSA-WITH-
CAMELLIA-128-
CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-RSA-WITH-
CAMELLIA-256-
CBC-SHA
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA.
TLS-RSA-WITH-
CAMELLIA-128-
CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-RSA-WITH-
CAMELLIA-256-
CBC-SHA256
Cipher suite TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-
WITH-3DES-
EDE-CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-DHE-RSA-
WITH-
CAMELLIA-128-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA.
TLS-DHE-DSS-
WITH-
CAMELLIA-128-
CBC-SHA
Cipher suite TLS-DSS-RSA-WITH-CAMELLIA-128-CBC-SHA.
Parameter Description Type Size Default
Option Description
TLS-DHE-RSA-
WITH-
CAMELLIA-256-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA.
TLS-DHE-DSS-
WITH-
CAMELLIA-256-
CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA.
TLS-DHE-RSA-
WITH-
CAMELLIA-128-
CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-DSS-
WITH-
CAMELLIA-128-
CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256.
TLS-DHE-RSA-
WITH-
CAMELLIA-256-
CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-DSS-
WITH-
CAMELLIA-256-
CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256.
TLS-DHE-RSA-
WITH-SEED-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-SEED-CBC-SHA.
TLS-DHE-DSS-
WITH-SEED-
CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-SEED-CBC-SHA.
TLS-DHE-RSA-
WITH-ARIA-128-
CBC-SHA256
Cipher suite TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-RSA-
WITH-ARIA-256-
CBC-SHA384
Cipher suite TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384.
Parameter Description Type Size Default
Option Description
TLS-DHE-DSS-
WITH-ARIA-128-
CBC-SHA256
Cipher suite TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256.
TLS-DHE-DSS-
WITH-ARIA-256-
CBC-SHA384
Cipher suite TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384.
TLS-RSA-WITH-
SEED-CBC-SHA
Cipher suite TLS-RSA-WITH-SEED-CBC-SHA.
TLS-RSA-WITH-
ARIA-128-CBC-
SHA256
Cipher suite TLS-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-RSA-WITH-
ARIA-256-CBC-
SHA384
Cipher suite TLS-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-
RSA-WITH-
ARIA-128-CBC-
SHA256
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256.
TLS-ECDHE-
RSA-WITH-
ARIA-256-CBC-
SHA384
Cipher suite TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384.
TLS-ECDHE-
ECDSA-WITH-
ARIA-128-CBC-
SHA256
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC_SHA256.
TLS-ECDHE-
ECDSA-WITH-
ARIA-256-CBC-
SHA384
Cipher suite TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC_SHA384.
TLS-ECDHE-
RSA-WITH-RC4-
128-SHA
Cipher suite TLS-ECDHE-RSA-WITH-RC4-128-SHA.
TLS-ECDHE-
RSA-WITH-
3DES-EDE-
CBC-SHA
Cipher suite TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA.
Parameter Description Type Size Default
Option Description
TLS-DHE-DSS-
WITH-3DES-
EDE-CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA.
TLS-RSA-WITH-
3DES-EDE-
CBC-SHA
Cipher suite TLS-RSA-WITH-3DES-EDE-CBC-SHA.
TLS-RSA-WITH-
RC4-128-MD5
Cipher suite TLS-RSA-WITH-RC4-128-MD5.
TLS-RSA-WITH-
RC4-128-SHA
Cipher suite TLS-RSA-WITH-RC4-128-SHA.
TLS-DHE-RSA-
WITH-DES-
CBC-SHA
Cipher suite TLS-DHE-RSA-WITH-DES-CBC-SHA.
TLS-DHE-DSS-
WITH-DES-
CBC-SHA
Cipher suite TLS-DHE-DSS-WITH-DES-CBC-SHA.
TLS-RSA-WITH-
DES-CBC-SHA
Cipher suite TLS-RSA-WITH-DES-CBC-SHA.
priority SSL/TLS cipher suites priority. integer Minimum
value: 0
Maximum
value:
4294967295
0
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

### config firewall vip6

Configure virtual IP for IPv6.
