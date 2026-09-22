# config vpn ssl

> Source: `config vpn ssl.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

set server {string}
next
end

#### Parameters

config vpn qkd
Parameter Description Type Size Default
certificate
<name>
Names of up to 4 certificates to offer to the KME.
Certificate name.
string Maximum
length: 79
comment Comment. var-string Maximum
length: 255
id Quantum Key Distribution ID assigned by the KME. string Maximum
length: 291
name Quantum Key Distribution configuration name. string Maximum
length: 35
peer Authenticate Quantum Key Device's certificate with the
peer/peergrp.
string Maximum
length: 35
port Port to connect to on the KME. integer Minimum
value: 1
Maximum
value:
65535
0
server IPv4, IPv6 or DNS address of the KME. string Maximum
length: 63

### config vpn ssl client

Client.

#### Syntax

config vpn ssl client
Description: Client.
edit <name>
set certificate {string}
set class-id {integer}
set comment {var-string}
set distance {integer}
set interface {string}
set ipv4-subnets {string}
set ipv6-subnets {string}
set peer {string}
set port {integer}
set priority {integer}
set psk {password-3}
set realm {string}
set server {string}
set source-ip {string}
set status [enable|disable]
set user {string}
next
end

#### Parameters

config vpn ssl client
Parameter Description Type Size Default
certificate Certificate to offer to SSL-VPN server if it requests
one.
string Maximum
length: 35
class-id Traffic class ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
comment Comment. var-string Maximum
length: 255
distance Distance for routes added by SSL-VPN. integer Minimum
value: 1
Maximum
value: 255
10
interface SSL interface to send/receive traffic over. string Maximum
length: 15
ipv4-subnets IPv4 subnets that the client is protecting. string Maximum
length: 79
ipv6-subnets IPv6 subnets that the client is protecting. string Maximum
length: 79
name SSL-VPN tunnel name. string Maximum
length: 35
peer Authenticate peer's certificate with the peer/peergrp. string Maximum
length: 35
port SSL-VPN server port. integer Minimum
value: 1
Maximum
value: 65535
443
priority Priority for routes added by SSL-VPN. integer Minimum
value: 1
Maximum
value: 65535
1
psk Pre-shared secret to authenticate with the server
(ASCII string or hexadecimal encoded with a leading
0x).
password-3 Not Specified
Parameter Description Type Size Default
realm Realm name configured on SSL-VPN server. string Maximum
length: 35
server IPv4, IPv6 or DNS address of the SSL-VPN server. string Maximum
length: 63
source-ip IPv4 or IPv6 address to use as a source for the SSL-
VPN connection to the server.
string Maximum
length: 63
status Enable/disable this SSL-VPN client configuration. option - enable
Option Description
enable Enable the SSL-VPN configuration.
disable Disable the SSL-VPN configuration.
user Username to offer to the peer to authenticate the
client.
string Maximum
length: 35

### config vpn ssl settings

Configure SSL-VPN.

#### Syntax

config vpn ssl settings
Description: Configure SSL-VPN.
set algorithm [high|medium|...]
set auth-session-check-source-ip [enable|disable]
set auth-timeout {integer}
config authentication-rule
Description: Authentication rule for SSL-VPN.
edit <id>
set auth [any|local|...]
set cipher [any|high|...]
set client-cert [enable|disable]
set groups <name1>, <name2>, ...
set portal {string}
set realm {string}
set source-address <name1>, <name2>, ...
set source-address-negate [enable|disable]
set source-address6 <name1>, <name2>, ...
set source-address6-negate [enable|disable]
set source-interface <name1>, <name2>, ...
set user-peer {string}
set users <name1>, <name2>, ...
next
end
set auto-tunnel-static-route [enable|disable]
set banned-cipher {option1}, {option2}, ...
set browser-language-detection [enable|disable]
set check-referer [enable|disable]
set ciphersuite {option1}, {option2}, ...
set client-sigalgs [no-rsa-pss|all]
set default-portal {string}
set deflate-compression-level {integer}
set deflate-min-data-size {integer}
set dns-server1 {ipv4-address}
set dns-server2 {ipv4-address}
set dns-suffix {var-string}
set dtls-heartbeat-fail-count {integer}
set dtls-heartbeat-idle-timeout {integer}
set dtls-heartbeat-interval {integer}
set dtls-hello-timeout {integer}
set dtls-max-proto-ver [dtls1-0|dtls1-2]
set dtls-min-proto-ver [dtls1-0|dtls1-2]
set dtls-tunnel [enable|disable]
set dual-stack-mode [enable|disable]
set encode-2f-sequence [enable|disable]
set encrypt-and-store-password [enable|disable]
set force-two-factor-auth [enable|disable]
set header-x-forwarded-for [pass|add|...]
set hsts-include-subdomains [enable|disable]
set http-compression [enable|disable]
set http-only-cookie [enable|disable]
set http-request-body-timeout {integer}
set http-request-header-timeout {integer}
set https-redirect [enable|disable]
set idle-timeout {integer}
set ipv6-dns-server1 {ipv6-address}
set ipv6-dns-server2 {ipv6-address}
set ipv6-wins-server1 {ipv6-address}
set ipv6-wins-server2 {ipv6-address}
set login-attempt-limit {integer}
set login-block-time {integer}
set login-timeout {integer}
set port {integer}
set port-precedence [enable|disable]
set reqclientcert [enable|disable]
set saml-redirect-port {integer}
set server-hostname {string}
set servercert {string}
set source-address <name1>, <name2>, ...
set source-address-negate [enable|disable]
set source-address6 <name1>, <name2>, ...
set source-address6-negate [enable|disable]
set source-interface <name1>, <name2>, ...
set ssl-client-renegotiation [disable|enable]
set ssl-insert-empty-fragment [enable|disable]
set ssl-max-proto-ver [tls1-0|tls1-1|...]
set ssl-min-proto-ver [tls1-0|tls1-1|...]
set status [enable|disable]
set transform-backward-slashes [enable|disable]
set tunnel-addr-assigned-method [first-available|round-robin]
set tunnel-connect-without-reauth [enable|disable]
set tunnel-ip-pools <name1>, <name2>, ...
set tunnel-ipv6-pools <name1>, <name2>, ...
set tunnel-user-session-timeout {integer}
set unsafe-legacy-renegotiation [enable|disable]
set url-obscuration [enable|disable]
set user-peer {string}
set wins-server1 {ipv4-address}
set wins-server2 {ipv4-address}
set x-content-type-options [enable|disable]
set ztna-trusted-client [enable|disable]
end

#### Parameters

config vpn ssl settings
Parameter Description Type Size Default
algorithm Force the SSL-VPN security level. High allows
only high. Medium allows medium and high. Low
allows any.
option - high
Option Description
high High algorithms.
medium High and medium algorithms.
default default
low All algorithms.
auth-session-
check-source-ip
Enable/disable checking of source IP for
authentication session.
option - enable
Option Description
enable Enable checking of source IP for authentication session.
disable Disable checking of source IP for authentication session.
auth-timeout SSL-VPN authentication timeout. integer Minimum
value: 0
Maximum
value: 259200
28800
auto-tunnel-
static-route
Enable/disable to auto-create static routes for
the SSL-VPN tunnel IP addresses.
option - enable
Option Description
enable Enable setting.
disable Disable setting.
banned-cipher Select one or more cipher technologies that
cannot be used in SSL-VPN negotiations. Only
applies to TLS 1.2 and below.
option - SHA1 SHA256
SHA384
Parameter Description Type Size Default
Option Description
RSA Ban the use of cipher suites using RSA key.
DHE Ban the use of cipher suites using authenticated ephemeral DH key
agreement.
ECDHE Ban the use of cipher suites using authenticated ephemeral ECDH key
agreement.
DSS Ban the use of cipher suites using DSS authentication.
ECDSA Ban the use of cipher suites using ECDSA authentication.
AES Ban the use of cipher suites using either 128 or 256 bit AES.
AESGCM Ban the use of cipher suites AES in Galois Counter Mode (GCM).
CAMELLIA Ban the use of cipher suites using either 128 or 256 bit CAMELLIA.
3DES Ban the use of cipher suites using triple DES
SHA1 Ban the use of cipher suites using HMAC-SHA1.
SHA256 Ban the use of cipher suites using HMAC-SHA256.
SHA384 Ban the use of cipher suites using HMAC-SHA384.
STATIC Ban the use of cipher suites using static keys.
CHACHA20 Ban the use of cipher suites using ChaCha20.
ARIA Ban the use of cipher suites using ARIA.
AESCCM Ban the use of cipher suites using AESCCM.
browser-
language-
detection
Enable/disable overriding the configured system
language based on the preferred language of
the browser.
option - enable
Option Description
enable Enable setting.
disable Disable setting.
check-referer Enable/disable verification of referer field in
HTTP request header.
option - disable
Option Description
enable Enable verification of referer field in HTTP request header.
disable Disable verification of referer field in HTTP request header.
Parameter Description Type Size Default
ciphersuite Select one or more TLS 1.3 ciphersuites to
enable. Does not affect ciphers in TLS 1.2 and
below. At least one must be enabled. To disable
all, set ssl-max-proto-ver to tls1-2 or below.
option - TLS-AES-128-
GCM-SHA256
TLS-AES-256-
GCM-SHA384
TLS-
CHACHA20-
POLY1305-
SHA256
Option Description
TLS-AES-128-
GCM-SHA256
Enable TLS-AES-128-GCM-SHA256 in TLS 1.3.
TLS-AES-256-
GCM-SHA384
Enable TLS-AES-256-GCM-SHA384 in TLS 1.3.
TLS-
CHACHA20-
POLY1305-
SHA256
Enable TLS-CHACHA20-POLY1305-SHA256 in TLS 1.3.
TLS-AES-128-
CCM-SHA256
Enable TLS-AES-128-CCM-SHA256 in TLS 1.3.
TLS-AES-128-
CCM-8-SHA256
Enable TLS-AES-128-CCM-8-SHA256 in TLS 1.3.
client-sigalgs Set signature algorithms related to client
authentication. Affects TLS version <= 1.2 only.
option - all
Option Description
no-rsa-pss Disable RSA-PSS signature algorithms for client authentication.
all Enable all supported signature algorithms for client authentication.
default-portal Default SSL-VPN portal. string Maximum
length: 35
deflate-
compression-
level
Compression level (0~9). integer Minimum
value: 0
Maximum
value: 9
6
deflate-min-
data-size
Minimum amount of data that triggers
compression.
integer Minimum
value: 200
Maximum
value: 65535
300
Parameter Description Type Size Default
dns-server1 DNS server 1. ipv4-
address
Not Specified 0.0.0.0
dns-server2 DNS server 2. ipv4-
address
Not Specified 0.0.0.0
dns-suffix DNS suffix used for SSL-VPN clients. var-string Maximum
length: 253
dtls-heartbeat-
fail-count
Number of missing heartbeats before the
connection is considered dropped.
integer Minimum
value: 3
Maximum
value: 10
3
dtls-heartbeat-
idle-timeout
Idle timeout before DTLS heartbeat is sent. integer Minimum
value: 3
Maximum
value: 10
3
dtls-heartbeat-
interval
Interval between DTLS heartbeat. integer Minimum
value: 3
Maximum
value: 10
3
dtls-hello-
timeout
SSLVPN maximum DTLS hello timeout. integer Minimum
value: 10
Maximum
value: 60
10
dtls-max-proto-
ver
DTLS maximum protocol version. option - dtls1-2
Option Description
dtls1-0 DTLS version 1.0.
dtls1-2 DTLS version 1.2.
dtls-min-proto-
ver
DTLS minimum protocol version. option - dtls1-0
Option Description
dtls1-0 DTLS version 1.0.
dtls1-2 DTLS version 1.2.
dtls-tunnel Enable/disable DTLS to prevent eavesdropping,
tampering, or message forgery.
option - enable
Parameter Description Type Size Default
Option Description
enable Enable setting.
disable Disable setting.
dual-stack-
mode
Tunnel mode: enable parallel IPv4 and IPv6
tunnel. Web mode: support IPv4 and IPv6
bookmarks in the portal.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
encode-2f-
sequence
Encode \2F sequence to forward slash in URLs. option - disable
Option Description
enable Enable setting.
disable Disable setting.
encrypt-and-
store-password
Encrypt and store user passwords for SSL-VPN
web sessions.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
force-two-
factor-auth
Enable/disable only PKI users with two-factor
authentication for SSL-VPNs.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
header-x-
forwarded-for
Forward the same, add, or remove HTTP
header.
option - add
Option Description
pass Forward the same HTTP header.
add Add the HTTP header.
remove Remove the HTTP header.
Parameter Description Type Size Default
hsts-include-
subdomains
Add HSTS includeSubDomains response
header.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
http-
compression
Enable/disable to allow HTTP compression over
SSL-VPN tunnels.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
http-only-cookie Enable/disable SSL-VPN support for HttpOnly
cookies.
option - enable
Option Description
enable Enable setting.
disable Disable setting.
http-request-
body-timeout
SSL-VPN session is disconnected if an HTTP
request body is not received within this time.
integer Minimum
value: 0
Maximum
value:
4294967295
30
http-request-
header-timeout
SSL-VPN session is disconnected if an HTTP
request header is not received within this time.
integer Minimum
value: 0
Maximum
value:
4294967295
20
https-redirect Enable/disable redirect of port 80 to SSL-VPN
port.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
idle-timeout SSL-VPN disconnects if idle for specified time in
seconds.
integer Minimum
value: 0
Maximum
value: 259200
300
Parameter Description Type Size Default
ipv6-dns-
server1
IPv6 DNS server 1. ipv6-
address
Not Specified ::
ipv6-dns-
server2
IPv6 DNS server 2. ipv6-
address
Not Specified ::
ipv6-wins-
server1
IPv6 WINS server 1. ipv6-
address
Not Specified ::
ipv6-wins-
server2
IPv6 WINS server 2. ipv6-
address
Not Specified ::
login-attempt-
limit
SSL-VPN maximum login attempt times before
block.
integer Minimum
value: 0
Maximum
value:
4294967295
2
login-block-time Time for which a user is blocked from logging in
after too many failed login attempts.
integer Minimum
value: 0
Maximum
value:
4294967295
60
login-timeout SSLVPN maximum login timeout. integer Minimum
value: 10
Maximum
value: 180
30
port SSL-VPN access port. integer Minimum
value: 1
Maximum
value: 65535
10443
port-
precedence
Enable/disable, Enable means that if SSL-VPN
connections are allowed on an interface admin
GUI connections are blocked on that interface.
option - enable
Option Description
enable Enable setting.
disable Disable setting.
reqclientcert Enable/disable to require client certificates for all
SSL-VPN users.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
Parameter Description Type Size Default
saml-redirect-
port
SAML local redirect port in the machine running
FortiClient. 0 is to disable redirection on FGT
side.
integer Minimum
value: 0
Maximum
value: 65535
8020
server-
hostname
Server hostname for HTTPS. When set, will be
used for SSL VPN web proxy host header for
any redirection.
string Maximum
length: 255
servercert Name of the server certificate to be used for
SSL-VPNs.
string Maximum
length: 35
source-address
<name>
Source address of incoming traffic.
Address name.
string Maximum
length: 79
source-
address-negate
Enable/disable negated source address match. option - disable
Option Description
enable Enable setting.
disable Disable setting.
source-
address6
<name>
IPv6 source address of incoming traffic.
IPv6 address name.
string Maximum
length: 79
source-
address6-
negate
Enable/disable negated source IPv6 address
match.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
source-
interface
<name>
SSL-VPN source interface of incoming traffic.
Interface name.
string Maximum
length: 35
ssl-client-
renegotiation
Enable/disable to allow client renegotiation by
the server if the tunnel goes down.
option - disable
Option Description
disable Abort any SSL connection that attempts to renegotiate.
enable Allow a SSL client to renegotiate.
Parameter Description Type Size Default
ssl-insert-
empty-fragment
Enable/disable insertion of empty fragment. option - enable
Option Description
enable Enable setting.
disable Disable setting.
ssl-max-proto-
ver
SSL maximum protocol version. option - tls1-3
Option Description
tls1-0 TLS version 1.0.
tls1-1 TLS version 1.1.
tls1-2 TLS version 1.2.
tls1-3 TLS version 1.3.
ssl-min-proto-
ver
SSL minimum protocol version. option - tls1-2
Option Description
tls1-0 TLS version 1.0.
tls1-1 TLS version 1.1.
tls1-2 TLS version 1.2.
tls1-3 TLS version 1.3.
status Enable/disable SSL-VPN. option - enable
Option Description
enable Enable SSL-VPN.
disable Disable SSL-VPN.
transform-
backward-
slashes
Transform backward slashes to forward slashes
in URLs.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
Parameter Description Type Size Default
tunnel-addr-
assigned-
method
Method used for assigning address for tunnel. option - first-available
Option Description
first-available Assign the first available address from the pools.
round-robin Assign the available address from the pool with a round robin fashion.
tunnel-connect-
without-reauth
Enable/disable tunnel connection without re-
authorization if previous connection dropped.
option - disable
Option Description
enable Enable tunnel connection without re-authorization.
disable Disable tunnel connection without re-authorization.
tunnel-ip-pools
<name>
Names of the IPv4 IP Pool firewall objects that
define the IP addresses reserved for remote
clients.
Address name.
string Maximum
length: 79
tunnel-ipv6-
pools <name>
Names of the IPv6 IP Pool firewall objects that
define the IP addresses reserved for remote
clients.
Address name.
string Maximum
length: 79
tunnel-user-
session-timeout
Number of seconds after which user sessions
are cleaned up after tunnel connection is
dropped.
integer Minimum
value: 1
Maximum
value: 86400
30
unsafe-legacy-
renegotiation
Enable/disable unsafe legacy re-negotiation. option - disable
Option Description
enable Enable setting.
disable Disable setting.
url-obscuration Enable/disable to obscure the host name of the
URL of the web browser display.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
Parameter Description Type Size Default
user-peer Name of user peer. string Maximum
length: 35
wins-server1 WINS server 1. ipv4-
address
Not Specified 0.0.0.0
wins-server2 WINS server 2. ipv4-
address
Not Specified 0.0.0.0
x-content-type-
options
Add HTTP X-Content-Type-Options header. option - enable
Option Description
enable Enable setting.
disable Disable setting.
ztna-trusted-
client
Enable/disable verification of device certificate
for SSLVPN ZTNA session.
option - disable
Option Description
enable Enable verification of device certificate for SSLVPN ZTNA session.
disable Disable verification of device certificate for SSLVPN ZTNA session.
config authentication-rule
Parameter Description Type Size Default
auth SSL-VPN authentication method restriction. option - any
Option Description
any Any
local Local
radius RADIUS
tacacs+ TACACS+
ldap LDAP
peer PEER
cipher SSL-VPN cipher strength. option - high
Option Description
any Any cipher strength.
Parameter Description Type Size Default
Option Description
high High cipher strength (>= 168 bits).
medium Medium cipher strength (>= 128 bits).
client-cert Enable/disable SSL-VPN client certificate restrictive. option - disable
Option Description
enable Enable setting.
disable Disable setting.
groups
<name>
User groups.
Group name.
string Maximum
length: 79
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
portal SSL-VPN portal. string Maximum
length: 35
realm SSL-VPN realm. string Maximum
length: 35
source-
address
<name>
Source address of incoming traffic.
Address name.
string Maximum
length: 79
source-
address-
negate
Enable/disable negated source address match. option - disable
Option Description
enable Enable setting.
disable Disable setting.
source-
address6
<name>
IPv6 source address of incoming traffic.
IPv6 address name.
string Maximum
length: 79
source-
address6-
negate
Enable/disable negated source IPv6 address match. option - disable
Parameter Description Type Size Default
Option Description
enable Enable setting.
disable Disable setting.
source-
interface
<name>
SSL-VPN source interface of incoming traffic.
Interface name.
string Maximum
length: 35
user-peer Name of user peer. string Maximum
length: 35
users <name> User name.
User name.
string Maximum
length: 79

### config vpn ssl web host-check-software

SSL-VPN host check software.

#### Syntax

config vpn ssl web host-check-software
Description: SSL-VPN host check software.
edit <name>
config check-item-list
Description: Check item list.
edit <id>
set action [require|deny]
set md5s <id1>, <id2>, ...
set target {string}
set type [file|registry|...]
set version {string}
next
end
set guid {user}
set os-type [windows|macos]
set type [av|fw]
set version {string}
next
end

#### Parameters

config vpn ssl web host-check-software
Parameter Description Type Size Default
guid Globally unique ID. user Not
Specified
name Name. string Maximum
length: 63
Parameter Description Type Size Default
os-type OS type. option - windows
Option Description
windows Microsoft Windows operating system.
macos Apple MacOS operating system.
type Type. option - av
Option Description
av AntiVirus.
fw Firewall.
version Version. string Maximum
length: 35
config check-item-list
Parameter Description Type Size Default
action Action. option - require
Option Description
require Require.
deny Deny.
id ID. integer Minimum
value: 0
Maximum
value:
65535
0
md5s <id> MD5 checksum.
Hex string of MD5 checksum.
string Maximum
length: 32
target Target. string Maximum
length: 255
type Type. option - file
Option Description
file File.
registry Registry.
process Process.
Parameter Description Type Size Default
version Version. string Maximum
length: 35

### config vpn ssl web portal

Portal.

#### Syntax

config vpn ssl web portal
Description: Portal.
edit <name>
set allow-user-access {option1}, {option2}, ...
set auto-connect [enable|disable]
config bookmark-group
Description: Portal bookmark group.
edit <name>
config bookmarks
Description: Bookmark table.
edit <name>
set additional-params {var-string}
set apptype [ftp|rdp|...]
set color-depth [32|16|...]
set description {var-string}
set domain {var-string}
set folder {var-string}
config form-data
Description: Form data.
edit <name>
set value {var-string}
next
end
set height {integer}
set host {var-string}
set keyboard-layout [ar-101|ar-102|...]
set load-balancing-info {var-string}
set logon-password {password}
set logon-user {var-string}
set port {integer}
set preconnection-blob {var-string}
set preconnection-id {integer}
set restricted-admin [enable|disable]
set security [any|rdp|...]
set send-preconnection-id [enable|disable]
set sso [disable|static|...]
set sso-credential [sslvpn-login|alternative]
set sso-credential-sent-once [enable|disable]
set sso-password {password}
set sso-username {var-string}
set url {var-string}
set vnc-keyboard-layout [default|da|...]
set width {integer}
next
end
next
end
set client-src-range [enable|disable]
set clipboard [enable|disable]
set custom-lang {string}
set customize-forticlient-download-url [enable|disable]
set default-protocol [web|ftp|...]
set default-window-height {integer}
set default-window-width {integer}
set dhcp-ip-overlap [use-new|use-old]
set dhcp-ra-giaddr {ipv4-address}
set dhcp6-ra-linkaddr {ipv6-address}
set display-bookmark [enable|disable]
set display-connection-tools [enable|disable]
set display-history [enable|disable]
set display-status [enable|disable]
set dns-server1 {ipv4-address}
set dns-server2 {ipv4-address}
set dns-suffix {var-string}
set exclusive-routing [enable|disable]
set focus-bookmark [enable|disable]
set forticlient-download [enable|disable]
set forticlient-download-method [direct|ssl-vpn]
set heading {string}
set hide-sso-credential [enable|disable]
set host-check [none|av|...]
set host-check-interval {integer}
set host-check-policy <name1>, <name2>, ...
set ip-mode [range|user-group|...]
set ip-pools <name1>, <name2>, ...
set ipv6-dns-server1 {ipv6-address}
set ipv6-dns-server2 {ipv6-address}
set ipv6-exclusive-routing [enable|disable]
set ipv6-pools <name1>, <name2>, ...
set ipv6-service-restriction [enable|disable]
set ipv6-split-tunneling [enable|disable]
set ipv6-split-tunneling-routing-address <name1>, <name2>, ...
set ipv6-split-tunneling-routing-negate [enable|disable]
set ipv6-tunnel-mode [enable|disable]
set ipv6-wins-server1 {ipv6-address}
set ipv6-wins-server2 {ipv6-address}
set keep-alive [enable|disable]
config landing-page
Description: Landing page options.
config form-data
Description: Form data.
edit <name>
set value {var-string}
next
end
set sso [disable|static|...]
set sso-credential [sslvpn-login|alternative]
set sso-password {password}
set sso-username {var-string}
set url {var-string}
end
set landing-page-mode [enable|disable]
set limit-user-logins [enable|disable]
set mac-addr-action [allow|deny]
set mac-addr-check [enable|disable]
config mac-addr-check-rule
Description: Client MAC address check rule.
edit <name>
set mac-addr-list <addr1>, <addr2>, ...
set mac-addr-mask {integer}
next
end
set macos-forticlient-download-url {var-string}
set os-check [enable|disable]
config os-check-list
Description: SSL-VPN OS checks. Read-only.
edit <name>
set action [deny|allow|...]
set latest-patch-level {user}
set tolerance {integer}
next
end
set prefer-ipv6-dns [enable|disable]
set redir-url {var-string}
set rewrite-ip-uri-ui [enable|disable]
set save-password [enable|disable]
set service-restriction [enable|disable]
set skip-check-for-browser [enable|disable]
set skip-check-for-unsupported-os [enable|disable]
set smb-max-version [smbv1|smbv2|...]
set smb-min-version [smbv1|smbv2|...]
set smb-ntlmv1-auth [enable|disable]
set smbv1 [enable|disable]
config split-dns
Description: Split DNS for SSL-VPN.
edit <id>
set dns-server1 {ipv4-address}
set dns-server2 {ipv4-address}
set domains {var-string}
set ipv6-dns-server1 {ipv6-address}
set ipv6-dns-server2 {ipv6-address}
next
end
set split-tunneling [enable|disable]
set split-tunneling-routing-address <name1>, <name2>, ...
set split-tunneling-routing-negate [enable|disable]
set theme [jade|neutrino|...]
set tunnel-mode [enable|disable]
set use-sdwan [enable|disable]
set user-bookmark [enable|disable]
set user-group-bookmark [enable|disable]
set web-mode [enable|disable]
set windows-forticlient-download-url {var-string}
set wins-server1 {ipv4-address}
set wins-server2 {ipv4-address}
next
end

#### Parameters

config vpn ssl web portal
Parameter Description Type Size Default
allow-user-
access
Allow user access to SSL-VPN applications. option - web ftp
smb sftp
telnet ssh
vnc rdp
ping
Option Description
web HTTP/HTTPS access.
ftp FTP access.
smb SMB/CIFS access.
sftp SFTP access.
telnet TELNET access.
ssh SSH access.
vnc VNC access.
rdp RDP access.
ping PING access.
auto-connect Enable/disable automatic connect by client when
system is up.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
client-src-range Allow client to add source range for the tunnel traffic. option - disable
Option Description
enable Enable setting.
disable Disable setting.
clipboard Enable to support RDP/VPC clipboard functionality. option - enable
Option Description
enable Enable support of RDP/VNC clipboard.
disable Disable support of RDP/VNC clipboard.
Parameter Description Type Size Default
custom-lang Change the web portal display language. Overrides
config system global set language. You can use config
system custom-language and execute system custom-
language to add custom language files.
string Maximum
length: 35
customize-
forticlient-
download-url
Enable support of customized download URL for
FortiClient.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
default-protocol Application type that is set by default. option - web
Option Description
web HTTP/HTTPS.
ftp FTP.
telnet Telnet.
smb SMB/CIFS.
vnc VNC.
rdp RDP.
ssh SSH.
sftp SFTP.
default-window-
height
Screen height. integer Minimum
value: 0
Maximum
value:
65535
768
default-window-
width
Screen width. integer Minimum
value: 0
Maximum
value:
65535
1024
dhcp-ip-overlap Configure overlapping DHCP IP allocation
assignment.
option - use-new
Parameter Description Type Size Default
Option Description
use-new Assign DHCP lease to new client and remove old client lease.
use-old Preserve previous client IP allocation and disconnect new client.
dhcp-ra-giaddr Relay agent gateway IP address to use in the giaddr
field of DHCP requests.
ipv4-
address
Not
Specified
0.0.0.0
dhcp6-ra-
linkaddr
Relay agent IPv6 link address to use in DHCP6
requests.
ipv6-
address
Not
Specified
::
display-
bookmark
Enable to display the web portal bookmark widget. option - enable
Option Description
enable Enable setting.
disable Disable setting.
display-
connection-
tools
Enable to display the web portal connection tools
widget.
option - enable
Option Description
enable Enable setting.
disable Disable setting.
display-history Enable to display the web portal user login history
widget.
option - enable
Option Description
enable Enable setting.
disable Disable setting.
display-status Enable to display the web portal status widget. option - enable
Option Description
enable Enable setting.
disable Disable setting.
dns-server1 IPv4 DNS server 1. ipv4-
address
Not
Specified
0.0.0.0
dns-server2 IPv4 DNS server 2. ipv4-
address
Not
Specified
0.0.0.0
Parameter Description Type Size Default
dns-suffix DNS suffix. var-string Maximum
length: 253
exclusive-
routing
Enable/disable all traffic go through tunnel only. option - disable
Option Description
enable Enable setting.
disable Disable setting.
focus-
bookmark
Enable to prioritize the placement of the bookmark
section over the quick-connection section in the SSL-
VPN application.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
forticlient-
download
Enable/disable download option for FortiClient. option - enable
Option Description
enable Enable setting.
disable Disable setting.
forticlient-
download-
method
FortiClient download method. option - direct
Option Description
direct Download via direct link.
ssl-vpn Download via SSL-VPN.
heading Web portal heading message. string Maximum
length: 31
SSL-VPN
Portal
hide-sso-
credential
Enable to prevent SSO credential being sent to client. option - enable
Option Description
enable Enable setting.
disable Disable setting.
Parameter Description Type Size Default
host-check Type of host checking performed on endpoints. option - none
Option Description
none No host checking.
av AntiVirus software recognized by the Windows Security Center.
fw Firewall software recognized by the Windows Security Center.
av-fw AntiVirus and firewall software recognized by the Windows Security Center.
custom Custom.
host-check-
interval
Periodic host check interval. Value of 0 means
disabled and host checking only happens when the
endpoint connects.
integer Minimum
value: 120
Maximum
value:
259200
0
host-check-
policy <name>
One or more policies to require the endpoint to have
specific security software.
Host check software list name.
string Maximum
length: 79
ip-mode Method by which users of this SSL-VPN tunnel obtain
IP addresses.
option - range
Option Description
range Use the IP addresses available for all SSL-VPN users as defined by the SSL
settings command.
user-group Use the IP addresses associated with individual users or user groups
(usually from external auth servers).
dhcp Use IP addresses obtained from external DHCP server.
no-ip Do not assign IP address.
ip-pools
<name>
IPv4 firewall source address objects reserved for SSL-
VPN tunnel mode clients.
Address name.
string Maximum
length: 79
ipv6-dns-
server1
IPv6 DNS server 1. ipv6-
address
Not
Specified
::
ipv6-dns-
server2
IPv6 DNS server 2. ipv6-
address
Not
Specified
::
ipv6-exclusive-
routing
Enable/disable all IPv6 traffic go through tunnel only. option - disable
Parameter Description Type Size Default
Option Description
enable Enable setting.
disable Disable setting.
ipv6-pools
<name>
IPv6 firewall source address objects reserved for SSL-
VPN tunnel mode clients.
Address name.
string Maximum
length: 79
ipv6-service-
restriction
Enable/disable IPv6 tunnel service restriction. option - disable
Option Description
enable Enable setting.
disable Disable setting.
ipv6-split-
tunneling
Enable/disable IPv6 split tunneling. option - enable
Option Description
enable Enable setting.
disable Disable setting.
ipv6-split-
tunneling-
routing-address
<name>
IPv6 SSL-VPN tunnel mode firewall address objects
that override firewall policy destination addresses to
control split-tunneling access.
Address name.
string Maximum
length: 79
ipv6-split-
tunneling-
routing-negate
Enable to negate IPv6 split tunneling routing address. option - disable
Option Description
enable Enable setting.
disable Disable setting.
ipv6-tunnel-
mode
Enable/disable IPv6 SSL-VPN tunnel mode. option - disable
Option Description
enable Enable setting.
disable Disable setting.
Parameter Description Type Size Default
ipv6-wins-
server1
IPv6 WINS server 1. ipv6-
address
Not
Specified
::
ipv6-wins-
server2
IPv6 WINS server 2. ipv6-
address
Not
Specified
::
keep-alive Enable/disable automatic reconnect for FortiClient
connections.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
landing-page-
mode
Enable/disable SSL-VPN landing page mode. option - disable
Option Description
enable Enable setting.
disable Disable setting.
limit-user-logins Enable to limit each user to one SSL-VPN session at a
time.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
mac-addr-
action
Client MAC address action. option - allow
Option Description
allow Allow connection when client MAC address is matched.
deny Deny connection when client MAC address is matched.
mac-addr-
check
Enable/disable MAC address host checking. option - disable
Option Description
enable Enable setting.
disable Disable setting.
Parameter Description Type Size Default
macos-
forticlient-
download-url
Download URL for Mac FortiClient. var-string Maximum
length: 1023
name Portal name. string Maximum
length: 35
os-check Enable to let the FortiGate decide action based on
client OS.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
prefer-ipv6-dns Prefer to query IPv6 DNS server first if enabled. option - disable
Option Description
enable Enable setting.
disable Disable setting.
redir-url Client login redirect URL. var-string Maximum
length: 255
rewrite-ip-uri-ui Rewrite contents for URI contains IP and /ui/. option - disable
Option Description
enable Enable contents rewrite for URI contains "IP-address/ui/".
disable Disable contents rewrite for URI contains "IP-address/ui/".
save-password Enable/disable FortiClient saving the user's password. option - disable
Option Description
enable Enable setting.
disable Disable setting.
service-
restriction
Enable/disable tunnel service restriction. option - disable
Option Description
enable Enable setting.
disable Disable setting.
Parameter Description Type Size Default
skip-check-for-
browser
Enable to skip host check for browser support. option - enable
Option Description
enable Enable setting.
disable Disable setting.
skip-check-for-
unsupported-os
Enable to skip host check if client OS does not support
it.
option - enable
Option Description
enable Enable setting.
disable Disable setting.
smb-max-
version
SMB maximum client protocol version. option - smbv3
Option Description
smbv1 SMB version 1.
smbv2 SMB version 2.
smbv3 SMB version 3.
smb-min-
version
SMB minimum client protocol version. option - smbv2
Option Description
smbv1 SMB version 1.
smbv2 SMB version 2.
smbv3 SMB version 3.
smb-ntlmv1-
auth
Enable support of NTLMv1 for Samba authentication. option - disable
Option Description
enable Enable setting.
disable Disable setting.
smbv1 SMB version 1. option - disable
Parameter Description Type Size Default
Option Description
enable enable
disable disable
split-tunneling Enable/disable IPv4 split tunneling. option - enable
Option Description
enable Enable setting.
disable Disable setting.
split-tunneling-
routing-address
<name>
IPv4 SSL-VPN tunnel mode firewall address objects
that override firewall policy destination addresses to
control split-tunneling access.
Address name.
string Maximum
length: 79
split-tunneling-
routing-negate
Enable to negate split tunneling routing address. option - disable
Option Description
enable Enable setting.
disable Disable setting.
theme Web portal color scheme. option - security-
fabric
Option Description
jade Jade theme.
neutrino Neutrino theme.
mariner Mariner theme.
graphite Graphite theme.
melongene Melongene theme.
jet-stream Jet Stream theme.
security-fabric Security Fabric theme.
dark-matter Dark Matter theme.
onyx Onyx theme.
eclipse Eclipse theme.
tunnel-mode Enable/disable IPv4 SSL-VPN tunnel mode. option - disable
Parameter Description Type Size Default
Option Description
enable Enable setting.
disable Disable setting.
use-sdwan Use SD-WAN rules to get output interface. option - disable
Option Description
enable Enable setting.
disable Disable setting.
user-bookmark Enable to allow web portal users to create their own
bookmarks.
option - enable
Option Description
enable Enable setting.
disable Disable setting.
user-group-
bookmark
Enable to allow web portal users to create bookmarks
for all users in the same user group.
option - enable
Option Description
enable Enable setting.
disable Disable setting.
web-mode Enable/disable SSL-VPN web mode. option - disable
Option Description
enable Enable setting.
disable Disable setting.
windows-
forticlient-
download-url
Download URL for Windows FortiClient. var-string Maximum
length: 1023
wins-server1 IPv4 WINS server 1. ipv4-
address
Not
Specified
0.0.0.0
wins-server2 IPv4 WINS server 1. ipv4-
address
Not
Specified
0.0.0.0
config bookmark-group
Parameter Description Type Size Default
name Bookmark group name. string Maximum
length: 35
config bookmarks
Parameter Description Type Size Default
additional-
params
Additional parameters. var-string Maximum
length: 128
apptype Application type. option - web
Option Description
ftp FTP.
rdp RDP.
sftp SFTP.
smb SMB/CIFS.
ssh SSH.
telnet Telnet.
vnc VNC.
web HTTP/HTTPS.
color-depth Color depth per pixel. option - 16
Option Description
32 32bits per pixel.
16 16bits per pixel.
8 8bits per pixel.
description Description. var-string Maximum
length: 128
domain Login domain. var-string Maximum
length: 128
folder Network shared file folder parameter. var-string Maximum
length: 128
Parameter Description Type Size Default
height Screen height. integer Minimum
value: 0
Maximum
value: 65535
0
host Host name/IP parameter. var-string Maximum
length: 128
keyboard-layout Keyboard layout. option - en-us
Option Description
ar-101 Arabic (101).
ar-102 Arabic (102).
ar-102-azerty Arabic (102) AZERTY.
can-mul Canadian Multilingual Standard.
cz Czech.
cz-qwerty Czech (QWERTY).
cz-pr Czech Programmers.
da Danish.
nl Dutch.
de German.
de-ch German, Switzerland.
de-ibm German (IBM).
en-uk English, United Kingdom.
en-uk-ext English, United Kingdom Extended.
en-us English, United States.
en-us-dvorak English, United States-Dvorak.
es Spanish.
es-var Spanish Variation.
fi Finnish.
fi-sami Finnish with Sami.
fr French.
fr-apple French, Apple.
fr-ca French, Canada.
Parameter Description Type Size Default
Option Description
fr-ch French, Switzerland.
fr-be French, Belgium.
hr Croatian.
hu Hungarian.
hu-101 Hungarian 101-Key.
it Italian.
it-142 Italian (142).
ja Japanese.
ja-106 Japanese 106/109 key.
ko Korean.
la-am Latin American.
lt Lithuanian.
lt-ibm Lithuanian IBM.
lt-std Lithuanian Standard.
lav-std Latvian (Standard).
lav-leg Latvian (Legacy).
mk Macedonian (FYROM).
mk-std Macedonia (FYROM) - Standard.
no Norwegian.
no-sami Norwegian with Sami.
pol-214 Polish (214).
pol-pr Polish (Programmers).
pt Portuguese.
pt-br Portuguese (Brazilian ABNT).
pt-br-abnt2 Portuguese (Brazilian ABNT2).
ru Russian.
ru-mne Russian - Mnemonic.
ru-t Russian (Typewriter).
sl Slovenian.
Parameter Description Type Size Default
Option Description
sv Swedish.
sv-sami Swedish with Sami.
tuk Turkmen.
tur-f Turkish F.
tur-q Turkish Q.
zh-sym-sg-us Chinese (Simplified, Singapore) - US keyboard.
zh-sym-us Chinese (Simplified) - US Keyboard.
zh-tr-hk Chinese (Traditional, Hong Kong S.A.R.).
zh-tr-mo Chinese (Traditional Macao S.A.R.) - US Keyboard.
zh-tr-us Chinese (Traditional) - US keyboard.
load-balancing-
info
The load balancing information or cookie which
should be provided to the connection broker.
var-string Maximum
length: 511
logon-password Logon password. password Not Specified
logon-user Logon user. var-string Maximum
length: 35
name Bookmark name. string Maximum
length: 35
port Remote port. integer Minimum
value: 0
Maximum
value: 65535
0
preconnection-
blob
An arbitrary string which identifies the RDP
source.
var-string Maximum
length: 511
preconnection-id The numeric ID of the RDP source. integer Minimum
value: 0
Maximum
value:
4294967295
0
restricted-admin Enable/disable restricted admin mode for RDP. option - disable
Option Description
enable Enable restricted admin mode for RDP.
disable Disable restricted admin mode for RDP.
Parameter Description Type Size Default
security Security mode for RDP connection. option - any
Option Description
any Allow the server to choose the type of security.
rdp Standard RDP encryption.
nla Network Level Authentication.
tls TLS encryption.
send-
preconnection-id
Enable/disable sending of preconnection ID. option - disable
Option Description
enable Enable sending of preconnection ID.
disable Disable sending of preconnection ID.
sso Single sign-on. option - disable
Option Description
disable Disable SSO.
static Static SSO.
auto Auto SSO.
sso-credential Single sign-on credentials. option - sslvpn-
login
Option Description
sslvpn-login SSL-VPN login.
alternative Alternative.
sso-credential-
sent-once
Single sign-on credentials are only sent once to
remote server.
option - disable
Option Description
enable Single sign-on credentials are only sent once to remote server.
disable Single sign-on credentials are sent to remote server for every HTTP
request.
sso-password SSO password. password Not Specified
sso-username SSO user name. var-string Maximum
length: 35
Parameter Description Type Size Default
url URL parameter. var-string Maximum
length: 128
vnc-keyboard-
layout
Keyboard layout. option - default
Option Description
default Default.
da Danish.
nl Dutch.
en-uk English, United Kingdom.
en-uk-ext English, United Kingdom Extended.
fi Finnish.
fr French.
fr-be French, Belgium.
fr-ca-mul French, Canadian Multilingual Std.
de German.
de-ch German, Switzerland.
it Italian.
it-142 Italian (142).
pt Portuguese.
pt-br-abnt2 Portuguese (Brazilian ABNT2).
no Norwegian.
gd Scottish Gaelic.
es Spanish.
sv Swedish.
us-intl United States-International.
width Screen width. integer Minimum
value: 0
Maximum
value: 65535
0
config form-data
Parameter Description Type Size Default
name Name. string Maximum
length: 35
value Value. var-string Maximum
length: 63
config form-data
Parameter Description Type Size Default
name Name. string Maximum
length: 35
value Value. var-string Maximum
length: 63
config landing-page
Parameter Description Type Size Default
sso Single sign-on. option - disable
Option Description
disable Disable SSO.
static Static SSO.
auto Auto SSO.
sso-credential Single sign-on credentials. option - sslvpn-login
Option Description
sslvpn-login SSL-VPN login.
alternative Alternative.
sso-password SSO password. password Not
Specified
sso-username SSO user name. var-string Maximum
length: 35
url Landing page URL. var-string Maximum
length: 511
config form-data
Parameter Description Type Size Default
name Name. string Maximum
length: 35
value Value. var-string Maximum
length: 63
config form-data
Parameter Description Type Size Default
name Name. string Maximum
length: 35
value Value. var-string Maximum
length: 63
config mac-addr-check-rule
Parameter Description Type Size Default
mac-addr-list
<addr>
Client MAC address list.
Client MAC address.
mac-
address
Not
Specified
mac-addr-
mask
Client MAC address mask. integer Minimum
value: 1
Maximum
value: 48
48
name Client MAC address check rule name. string Maximum
length: 35
config os-check-list
Parameter Description Type Size Default
action OS check options. option - allow
Option Description
deny Deny all OS versions.
allow Allow any OS version.
check-up-to-date Verify OS is up-to-date.
latest-patch-
level
Latest OS patch level. user Not
Specified
0
Parameter Description Type Size Default
name Name. string Maximum
length: 35
tolerance OS patch level tolerance. integer Minimum
value: 0
Maximum
value:
65535
0
config split-dns
Parameter Description Type Size Default
dns-server1 DNS server 1. ipv4-
address
Not Specified 0.0.0.0
dns-server2 DNS server 2. ipv4-
address
Not Specified 0.0.0.0
domains Split DNS domains used for SSL-VPN clients
separated by comma.
var-string Maximum
length: 1024
id ID. integer Minimum
value: 0
Maximum
value:
4294967294
0
ipv6-dns-
server1
IPv6 DNS server 1. ipv6-
address
Not Specified ::
ipv6-dns-
server2
IPv6 DNS server 2. ipv6-
address
Not Specified ::

### config vpn ssl web realm

Realm.

#### Syntax

config vpn ssl web realm
Description: Realm.
edit <url-path>
set login-page {var-string}
set max-concurrent-user {integer}
set nas-ip {ipv4-address}
set radius-port {integer}
set radius-server {string}
set virtual-host {var-string}
set virtual-host-only [enable|disable]
set virtual-host-server-cert {string}
next
end

#### Parameters

config vpn ssl web realm
Parameter Description Type Size Default
login-page Replacement HTML for SSL-VPN login page. var-string Maximum
length:
32768
max-
concurrent-
user
Maximum concurrent users. integer Minimum
value: 0
Maximum
value:
65535
0
nas-ip IP address used as a NAS-IP to communicate with the
RADIUS server.
ipv4-
address
Not
Specified
0.0.0.0
radius-port RADIUS service port number. integer Minimum
value: 0
Maximum
value:
65535
0
radius-server RADIUS server associated with realm. string Maximum
length: 35
url-path URL path to access SSL-VPN login page. string Maximum
length: 35
virtual-host Virtual host name for realm. var-string Maximum
length: 255
virtual-host-
only
Enable/disable enforcement of virtual host method for
SSL-VPN client access.
option - disable
Option Description
enable Enable setting.
disable Disable setting.
virtual-host-
server-cert
Name of the server certificate to used for this realm. string Maximum
length: 35

### config vpn ssl web user-bookmark

Configure SSL-VPN user bookmark.

#### Syntax

config vpn ssl web user-bookmark
Description: Configure SSL-VPN user bookmark.
edit <name>
config bookmarks
Description: Bookmark table.
edit <name>
set additional-params {var-string}
set apptype [ftp|rdp|...]
set color-depth [32|16|...]
set description {var-string}
set domain {var-string}
set folder {var-string}
config form-data
Description: Form data.
edit <name>
set value {var-string}
next
end
set height {integer}
set host {var-string}
set keyboard-layout [ar-101|ar-102|...]
set load-balancing-info {var-string}
set logon-password {password}
set logon-user {var-string}
set port {integer}
set preconnection-blob {var-string}
set preconnection-id {integer}
set restricted-admin [enable|disable]
set security [any|rdp|...]
set send-preconnection-id [enable|disable]
set sso [disable|static|...]
set sso-credential [sslvpn-login|alternative]
set sso-credential-sent-once [enable|disable]
set sso-password {password}
set sso-username {var-string}
set url {var-string}
set vnc-keyboard-layout [default|da|...]
set width {integer}
next
end
set custom-lang {string}
next
end

#### Parameters

config vpn ssl web user-bookmark
Parameter Description Type Size Default
custom-lang Personal language. string Maximum
length: 35
name User and group name. string Maximum
length: 101
config bookmarks
Parameter Description Type Size Default
additional-
params
Additional parameters. var-string Maximum
length: 128
apptype Application type. option - web
Option Description
ftp FTP.
rdp RDP.
sftp SFTP.
smb SMB/CIFS.
ssh SSH.
telnet Telnet.
vnc VNC.
web HTTP/HTTPS.
color-depth Color depth per pixel. option - 16
Option Description
32 32bits per pixel.
16 16bits per pixel.
8 8bits per pixel.
description Description. var-string Maximum
length: 128
domain Login domain. var-string Maximum
length: 128
folder Network shared file folder parameter. var-string Maximum
length: 128
height Screen height. integer Minimum
value: 0
Maximum
value: 65535
0
host Host name/IP parameter. var-string Maximum
length: 128
keyboard-layout Keyboard layout. option - en-us
Parameter Description Type Size Default
Option Description
ar-101 Arabic (101).
ar-102 Arabic (102).
ar-102-azerty Arabic (102) AZERTY.
can-mul Canadian Multilingual Standard.
cz Czech.
cz-qwerty Czech (QWERTY).
cz-pr Czech Programmers.
da Danish.
nl Dutch.
de German.
de-ch German, Switzerland.
de-ibm German (IBM).
en-uk English, United Kingdom.
en-uk-ext English, United Kingdom Extended.
en-us English, United States.
en-us-dvorak English, United States-Dvorak.
es Spanish.
es-var Spanish Variation.
fi Finnish.
fi-sami Finnish with Sami.
fr French.
fr-apple French, Apple.
fr-ca French, Canada.
fr-ch French, Switzerland.
fr-be French, Belgium.
hr Croatian.
hu Hungarian.
hu-101 Hungarian 101-Key.
it Italian.
Parameter Description Type Size Default
Option Description
it-142 Italian (142).
ja Japanese.
ja-106 Japanese 106/109 key.
ko Korean.
la-am Latin American.
lt Lithuanian.
lt-ibm Lithuanian IBM.
lt-std Lithuanian Standard.
lav-std Latvian (Standard).
lav-leg Latvian (Legacy).
mk Macedonian (FYROM).
mk-std Macedonia (FYROM) - Standard.
no Norwegian.
no-sami Norwegian with Sami.
pol-214 Polish (214).
pol-pr Polish (Programmers).
pt Portuguese.
pt-br Portuguese (Brazilian ABNT).
pt-br-abnt2 Portuguese (Brazilian ABNT2).
ru Russian.
ru-mne Russian - Mnemonic.
ru-t Russian (Typewriter).
sl Slovenian.
sv Swedish.
sv-sami Swedish with Sami.
tuk Turkmen.
tur-f Turkish F.
tur-q Turkish Q.
zh-sym-sg-us Chinese (Simplified, Singapore) - US keyboard.
Parameter Description Type Size Default
Option Description
zh-sym-us Chinese (Simplified) - US Keyboard.
zh-tr-hk Chinese (Traditional, Hong Kong S.A.R.).
zh-tr-mo Chinese (Traditional Macao S.A.R.) - US Keyboard.
zh-tr-us Chinese (Traditional) - US keyboard.
load-balancing-
info
The load balancing information or cookie which
should be provided to the connection broker.
var-string Maximum
length: 511
logon-password Logon password. password Not Specified
logon-user Logon user. var-string Maximum
length: 35
name Bookmark name. string Maximum
length: 35
port Remote port. integer Minimum
value: 0
Maximum
value: 65535
0
preconnection-
blob
An arbitrary string which identifies the RDP
source.
var-string Maximum
length: 511
preconnection-id The numeric ID of the RDP source. integer Minimum
value: 0
Maximum
value:
4294967295
0
restricted-admin Enable/disable restricted admin mode for RDP. option - disable
Option Description
enable Enable restricted admin mode for RDP.
disable Disable restricted admin mode for RDP.
security Security mode for RDP connection. option - any
Option Description
any Allow the server to choose the type of security.
rdp Standard RDP encryption.
nla Network Level Authentication.
tls TLS encryption.
Parameter Description Type Size Default
send-
preconnection-id
Enable/disable sending of preconnection ID. option - disable
Option Description
enable Enable sending of preconnection ID.
disable Disable sending of preconnection ID.
sso Single sign-on. option - disable
Option Description
disable Disable SSO.
static Static SSO.
auto Auto SSO.
sso-credential Single sign-on credentials. option - sslvpn-
login
Option Description
sslvpn-login SSL-VPN login.
alternative Alternative.
sso-credential-
sent-once
Single sign-on credentials are only sent once to
remote server.
option - disable
Option Description
enable Single sign-on credentials are only sent once to remote server.
disable Single sign-on credentials are sent to remote server for every HTTP
request.
sso-password SSO password. password Not Specified
sso-username SSO user name. var-string Maximum
length: 35
url URL parameter. var-string Maximum
length: 128
vnc-keyboard-
layout
Keyboard layout. option - default
Option Description
default Default.
da Danish.
Parameter Description Type Size Default
Option Description
nl Dutch.
en-uk English, United Kingdom.
en-uk-ext English, United Kingdom Extended.
fi Finnish.
fr French.
fr-be French, Belgium.
fr-ca-mul French, Canadian Multilingual Std.
de German.
de-ch German, Switzerland.
it Italian.
it-142 Italian (142).
pt Portuguese.
pt-br-abnt2 Portuguese (Brazilian ABNT2).
no Norwegian.
gd Scottish Gaelic.
es Spanish.
sv Swedish.
us-intl United States-International.
width Screen width. integer Minimum
value: 0
Maximum
value: 65535
0
config form-data
Parameter Description Type Size Default
name Name. string Maximum
length: 35
value Value. var-string Maximum
length: 63

### config vpn ssl web user-group-bookmark

Configure SSL-VPN user group bookmark.
