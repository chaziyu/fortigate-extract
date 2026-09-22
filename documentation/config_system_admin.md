# config system admin

> Source: `config system admin.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
email Account email. string Maximum
length: 255
id Account id. string Maximum
length: 255
privatekey Account Private Key. string Maximum
length: 8191
status Account status. string Maximum
length: 127
url Account url. string Maximum
length: 511

### config system admin

Configure admin users.

#### Syntax

config system admin
Description: Configure admin users.
edit <name>
set accprofile {string}
set accprofile-override [enable|disable]
set allow-remove-admin-session [enable|disable]
set comments {var-string}
set email-to {string}
set force-password-change [enable|disable]
set fortitoken {string}
set guest-auth [disable|enable]
set guest-lang {string}
set guest-usergroups <name1>, <name2>, ...
set ip6-trusthost1 {ipv6-prefix}
set ip6-trusthost10 {ipv6-prefix}
set ip6-trusthost2 {ipv6-prefix}
set ip6-trusthost3 {ipv6-prefix}
set ip6-trusthost4 {ipv6-prefix}
set ip6-trusthost5 {ipv6-prefix}
set ip6-trusthost6 {ipv6-prefix}
set ip6-trusthost7 {ipv6-prefix}
set ip6-trusthost8 {ipv6-prefix}
set ip6-trusthost9 {ipv6-prefix}
set password {password-2}
set password-expire {user}
set peer-auth [enable|disable]
set peer-group {string}
set remote-auth [enable|disable]
set remote-group {string}
set schedule {string}
set sms-custom-server {string}
set sms-phone {string}
set sms-server [fortiguard|custom]
set ssh-certificate {string}
set ssh-public-key1 {user}
set ssh-public-key2 {user}
set ssh-public-key3 {user}
set trusthost1 {ipv4-classnet}
set trusthost10 {ipv4-classnet}
set trusthost2 {ipv4-classnet}
set trusthost3 {ipv4-classnet}
set trusthost4 {ipv4-classnet}
set trusthost5 {ipv4-classnet}
set trusthost6 {ipv4-classnet}
set trusthost7 {ipv4-classnet}
set trusthost8 {ipv4-classnet}
set trusthost9 {ipv4-classnet}
set two-factor [disable|fortitoken|...]
set two-factor-authentication [fortitoken|email|...]
set two-factor-notification [email|sms]
set vdom <name1>, <name2>, ...
set vdom-override [enable|disable]
set wildcard [enable|disable]
next
end

#### Parameters

config system admin
Parameter Description Type Size Default
accprofile Access profile for this administrator. Access profiles
control administrator access to FortiGate features.
string Maximum
length: 35
accprofile-
override
Enable to use the name of an access profile
provided by the remote authentication server to
control the FortiGate features that this administrator
can access.
option - disable
Option Description
enable Enable access profile override.
disable Disable access profile override.
allow-remove-
admin-session
Enable/disable allow admin session to be removed
by privileged admin users.
option - enable
Option Description
enable Enable allow-remove option.
disable Disable allow-remove option.
comments Comment. var-string Maximum
length: 255
email-to This administrator's email address. string Maximum
length: 63
Parameter Description Type Size Default
force-password-
change
Enable/disable force password change on next
login.
option - disable
Option Description
enable Enable force password change on next login.
disable Disable force password change on next login.
fortitoken This administrator's FortiToken serial number. string Maximum
length: 16
guest-auth Enable/disable guest authentication. option - disable
Option Description
disable Disable guest authentication.
enable Enable guest authentication.
guest-lang Guest management portal language. string Maximum
length: 35
guest-
usergroups
<name>
Select guest user groups.
Select guest user groups.
string Maximum
length: 79
ip6-trusthost1 Any IPv6 address from which the administrator can
connect to the FortiGate unit. Default allows access
from any IPv6 address.
ipv6-prefix Not
Specified
::/0
ip6-trusthost10 Any IPv6 address from which the administrator can
connect to the FortiGate unit. Default allows access
from any IPv6 address.
ipv6-prefix Not
Specified
::/0
ip6-trusthost2 Any IPv6 address from which the administrator can
connect to the FortiGate unit. Default allows access
from any IPv6 address.
ipv6-prefix Not
Specified
::/0
ip6-trusthost3 Any IPv6 address from which the administrator can
connect to the FortiGate unit. Default allows access
from any IPv6 address.
ipv6-prefix Not
Specified
::/0
ip6-trusthost4 Any IPv6 address from which the administrator can
connect to the FortiGate unit. Default allows access
from any IPv6 address.
ipv6-prefix Not
Specified
::/0
ip6-trusthost5 Any IPv6 address from which the administrator can
connect to the FortiGate unit. Default allows access
from any IPv6 address.
ipv6-prefix Not
Specified
::/0
Parameter Description Type Size Default
ip6-trusthost6 Any IPv6 address from which the administrator can
connect to the FortiGate unit. Default allows access
from any IPv6 address.
ipv6-prefix Not
Specified
::/0
ip6-trusthost7 Any IPv6 address from which the administrator can
connect to the FortiGate unit. Default allows access
from any IPv6 address.
ipv6-prefix Not
Specified
::/0
ip6-trusthost8 Any IPv6 address from which the administrator can
connect to the FortiGate unit. Default allows access
from any IPv6 address.
ipv6-prefix Not
Specified
::/0
ip6-trusthost9 Any IPv6 address from which the administrator can
connect to the FortiGate unit. Default allows access
from any IPv6 address.
ipv6-prefix Not
Specified
::/0
name User name. string Maximum
length: 64
password Admin user password. password-2 Not
Specified
password-expire Password expire time. user Not
Specified
peer-auth Set to enable peer certificate authentication (for
HTTPS admin access).
option - disable
Option Description
enable Enable peer.
disable Disable peer.
peer-group Name of peer group defined under config user group
which has PKI members. Used for peer certificate
authentication (for HTTPS admin access).
string Maximum
length: 35
remote-auth Enable/disable authentication using a remote
RADIUS, LDAP, or TACACS+ server.
option - disable
Option Description
enable Enable remote authentication.
disable Disable remote authentication.
remote-group User group name used for remote auth. string Maximum
length: 35
schedule Firewall schedule used to restrict when the
administrator can log in. No schedule means no
restrictions.
string Maximum
length: 35
Parameter Description Type Size Default
sms-custom-
server
Custom SMS server to send SMS messages to. string Maximum
length: 35
sms-phone Phone number on which the administrator receives
SMS messages.
string Maximum
length: 15
sms-server Send SMS messages using the FortiGuard SMS
server or a custom server.
option - fortiguard
Option Description
fortiguard Send SMS by FortiGuard.
custom Send SMS by custom server.
ssh-certificate Select the certificate to be used by the FortiGate for
authentication with an SSH client.
string Maximum
length: 35
ssh-public-key1 Public key of an SSH client. The client is
authenticated without being asked for credentials.
Create the public-private key pair in the SSH client
application.
user Not
Specified
ssh-public-key2 Public key of an SSH client. The client is
authenticated without being asked for credentials.
Create the public-private key pair in the SSH client
application.
user Not
Specified
ssh-public-key3 Public key of an SSH client. The client is
authenticated without being asked for credentials.
Create the public-private key pair in the SSH client
application.
user Not
Specified
trusthost1 Any IPv4 address or subnet address and netmask
from which the administrator can connect to the
FortiGate unit. Default allows access from any IPv4
address.
ipv4-
classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost10 Any IPv4 address or subnet address and netmask
from which the administrator can connect to the
FortiGate unit. Default allows access from any IPv4
address.
ipv4-
classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost2 Any IPv4 address or subnet address and netmask
from which the administrator can connect to the
FortiGate unit. Default allows access from any IPv4
address.
ipv4-
classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost3 Any IPv4 address or subnet address and netmask
from which the administrator can connect to the
FortiGate unit. Default allows access from any IPv4
address.
ipv4-
classnet
Not
Specified
0.0.0.0
0.0.0.0
Parameter Description Type Size Default
trusthost4 Any IPv4 address or subnet address and netmask
from which the administrator can connect to the
FortiGate unit. Default allows access from any IPv4
address.
ipv4-
classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost5 Any IPv4 address or subnet address and netmask
from which the administrator can connect to the
FortiGate unit. Default allows access from any IPv4
address.
ipv4-
classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost6 Any IPv4 address or subnet address and netmask
from which the administrator can connect to the
FortiGate unit. Default allows access from any IPv4
address.
ipv4-
classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost7 Any IPv4 address or subnet address and netmask
from which the administrator can connect to the
FortiGate unit. Default allows access from any IPv4
address.
ipv4-
classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost8 Any IPv4 address or subnet address and netmask
from which the administrator can connect to the
FortiGate unit. Default allows access from any IPv4
address.
ipv4-
classnet
Not
Specified
0.0.0.0
0.0.0.0
trusthost9 Any IPv4 address or subnet address and netmask
from which the administrator can connect to the
FortiGate unit. Default allows access from any IPv4
address.
ipv4-
classnet
Not
Specified
0.0.0.0
0.0.0.0
two-factor Enable/disable two-factor authentication. option - disable
Option Description
disable Disable two-factor authentication.
fortitoken Use FortiToken or FortiToken mobile two-factor authentication.
fortitoken-cloud FortiToken Cloud Service.
email Send a two-factor authentication code to the configured email-to email
address.
sms Send a two-factor authentication code to the configured sms-server and
sms-phone.
two-factor-
authentication
Authentication method by FortiToken Cloud. option -
Parameter Description Type Size Default
Option Description
fortitoken FortiToken authentication.
email Email one time password.
sms SMS one time password.
two-factor-
notification
Notification method for user activation by FortiToken
Cloud.
option -
Option Description
email Email notification for activation code.
sms SMS notification for activation code.
vdom <name> Virtual domain(s) that the administrator can access.
Virtual domain name.
string Maximum
length: 79
vdom-override Enable to use the names of VDOMs provided by the
remote authentication server to control the VDOMs
that this administrator can access.
option - disable
Option Description
enable Enable VDOM override.
disable Disable VDOM override.
wildcard Enable/disable wildcard RADIUS authentication. option - disable
Option Description
enable Enable username wildcard.
disable Disable username wildcard.

### config system affinity-interrupt

This command is available for model(s): FortiGate 100F, FortiGate 101F, FortiGate 120G,
FortiGate 121G, FortiGate 200F, FortiGate 201F, FortiGate 4200F, FortiGate 4201F,
FortiGate 4400F, FortiGate 4401F, FortiGate 80F DSL, FortiGate 90G, FortiGate 91G,
FortiGate-VM for Aliyun, FortiGate-VM for AWS, FortiGate-VM for Azure, FortiGate-VM for
GCP, FortiGate-VM for OPC, FortiGate-VM64, FortiWiFi 80F 2R 3G4G DSL, FortiWiFi 81F 2R
3G4G DSL.
It is not available for: FortiGate 1000D, FortiGate 1000F, FortiGate 1001F, FortiGate 1100E,
FortiGate 1101E, FortiGate 140E-POE, FortiGate 140E, FortiGate 1800F, FortiGate 1801F,
FortiGate 2000E, FortiGate 200E, FortiGate 201E, FortiGate 2200E, FortiGate 2201E,
FortiGate 2500E, FortiGate 2600F, FortiGate 2601F, FortiGate 3000D, FortiGate 3000F,
FortiGate 3001F, FortiGate 300E, FortiGate 301E, FortiGate 3100D, FortiGate 3200D,
FortiGate 3200F, FortiGate 3201F, FortiGate 3300E, FortiGate 3301E, FortiGate 3400E,
FortiGate 3401E, FortiGate 3500F, FortiGate 3501F, FortiGate 3600E, FortiGate 3601E,
FortiGate 3700D, FortiGate 3700F, FortiGate 3701F, FortiGate 3960E, FortiGate 3980E,
FortiGate 400E Bypass, FortiGate 400E, FortiGate 400F, FortiGate 401E, FortiGate 401F,
FortiGate 5001E1, FortiGate 5001E, FortiGate 500E, FortiGate 501E, FortiGate 600E,
FortiGate 600F, FortiGate 601E, FortiGate 601F, FortiGate 60E DSLJ, FortiGate 60E DSL,
FortiGate 60E-POE, FortiGate 60E, FortiGate 61E, FortiGate 800D, FortiGate 80E-POE,
FortiGate 80E, FortiGate 81E-POE, FortiGate 81E, FortiGate 900D, FortiGate 900G,
FortiGate 901G, FortiGate 90E, FortiGate 91E, FortiGateRugged 70F, FortiWiFi 60E DSLJ,
FortiWiFi 60E DSL, FortiWiFi 60E, FortiWiFi 61E.
Configure interrupt affinity.

#### Syntax

config system affinity-interrupt
Description: Configure interrupt affinity.
edit <id>
set affinity-cpumask {string}
set default-affinity-cpumask {string}
set interrupt {string}
next
end

#### Parameters

config system affinity-interrupt
Parameter Description Type Size Default
affinity-
cpumask
Affinity setting (64-bit hexadecimal value in the format
of 0xxxxxxxxxxxxxxxxx).
string Maximum
length: 127
default-
affinity-
cpumask
Default affinity setting (64-bit hexadecimal value in
the format of 0xxxxxxxxxxxxxxxxx). Read-only.
string Maximum
length: 127
