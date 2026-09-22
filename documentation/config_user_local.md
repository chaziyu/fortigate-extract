# config user local

> Source: `config user local.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
Option Description
fortitoken FortiToken authentication.
email Email one time password.
sms SMS one time password.
two-factor-filter Filter used to
synchronize
users to
FortiToken
Cloud.
string Maximum
length:
2047
two-factor-
notification
Notification
method for user
activation by
FortiToken
Cloud.
option -
Option Description
email Email notification for activation code.
sms SMS notification for activation code.
type Authentication
type for LDAP
searches.
option - simple
Option Description
simple Simple password authentication without search.
anonymous Bind using anonymous user search.
regular Bind using username/password and then search.
user-info-
exchange-
server
MS Exchange
server from
which to fetch
user information.
string Maximum
length: 35
username Username (full
DN) for initial
binding.
string Maximum
length: 511

### config user local

Configure local users.

#### Syntax

config user local
Description: Configure local users.
edit <name>
set auth-concurrent-override [enable|disable]
set auth-concurrent-value {integer}
set authtimeout {integer}
set email-to {string}
set fortitoken {string}
set id {integer}
set ldap-server {string}
set passwd {password}
set passwd-policy {string}
set passwd-time {user}
set ppk-identity {string}
set ppk-secret {password-3}
set qkd-profile {string}
set radius-server {string}
set sms-custom-server {string}
set sms-phone {string}
set sms-server [fortiguard|custom]
set status [enable|disable]
set tacacs+-server {string}
set two-factor [disable|fortitoken|...]
set two-factor-authentication [fortitoken|email|...]
set two-factor-notification [email|sms]
set type [password|radius|...]
set username-sensitivity [disable|enable]
set workstation {string}
next
end

#### Parameters

config user local
Parameter Description Type Size Default
auth-concurrent-
override
Enable/disable overriding the policy-auth-
concurrent under config system global.
option - disable
Option Description
enable Enable auth-concurrent-override.
disable Disable auth-concurrent-override.
auth-concurrent-
value
Maximum number of concurrent logins permitted
from the same user.
integer Minimum
value: 0
Maximum
value: 100
0
authtimeout Time in minutes before the authentication timeout
for a user is reached.
integer Minimum
value: 0
Maximum
value: 1440
0
Parameter Description Type Size Default
email-to Two-factor recipient's email address. string Maximum
length: 63
fortitoken Two-factor recipient's FortiToken serial number. string Maximum
length: 16
id User ID. Read-only. integer Minimum
value: 0
Maximum
value:
4294967295
0
ldap-server Name of LDAP server with which the user must
authenticate.
string Maximum
length: 35
name Local user name. string Maximum
length: 64
passwd User's password. password Not Specified
passwd-policy Password policy to apply to this user, as defined
in config user password-policy.
string Maximum
length: 35
passwd-time Time of the last password update. user Not Specified
ppk-identity IKEv2 Postquantum Preshared Key Identity. string Maximum
length: 35
ppk-secret IKEv2 Postquantum Preshared Key (ASCII string
or hexadecimal encoded with a leading 0x).
password-3 Not Specified
qkd-profile Quantum Key Distribution (QKD) profile. string Maximum
length: 35
radius-server Name of RADIUS server with which the user must
authenticate.
string Maximum
length: 35
sms-custom-
server
Two-factor recipient's SMS server. string Maximum
length: 35
sms-phone Two-factor recipient's mobile phone number. string Maximum
length: 15
sms-server Send SMS through FortiGuard or other external
server.
option - fortiguard
Option Description
fortiguard Send SMS by FortiGuard.
custom Send SMS by custom server.
status Enable/disable allowing the local user to
authenticate with the FortiGate unit.
option - enable
Parameter Description Type Size Default
Option Description
enable Enable user.
disable Disable user.
tacacs+-server Name of TACACS+ server with which the user
must authenticate.
string Maximum
length: 35
two-factor Enable/disable two-factor authentication. option - disable
Option Description
disable disable
fortitoken FortiToken
fortitoken-cloud FortiToken Cloud Service.
email Email authentication code.
sms SMS authentication code.
two-factor-
authentication
Authentication method by FortiToken Cloud. option -
Option Description
fortitoken FortiToken authentication.
email Email one time password.
sms SMS one time password.
two-factor-
notification
Notification method for user activation by
FortiToken Cloud.
option -
Option Description
email Email notification for activation code.
sms SMS notification for activation code.
type Authentication method. option - password
Option Description
password Password authentication.
radius RADIUS server authentication.
tacacs+ TACACS+ server authentication.
ldap LDAP server authentication.
Parameter Description Type Size Default
username-
sensitivity
Enable/disable case and accent sensitivity when
performing username matching (accents are
stripped and case is ignored when disabled).
option - enable
Option Description
disable Ignore case and accents. Username at prompt not required to match case or
accents.
enable Do not ignore case and accents. Username at prompt must be an exact
match.
workstation Name of the remote user workstation, if you want
to limit the user to authenticate only from a
particular workstation.
string Maximum
length: 35

### config user nac-policy

Configure NAC policy matching pattern to identify matching NAC devices.

#### Syntax

config user nac-policy
Description: Configure NAC policy matching pattern to identify matching NAC devices.
edit <name>
set category [device|firewall-user|...]
set description {string}
set ems-tag {string}
set family {string}
set firewall-address {string}
set fortivoice-tag {string}
set host {string}
set hw-vendor {string}
set hw-version {string}
set mac {string}
set match-period {integer}
set match-type [dynamic|override]
set os {string}
set severity <severity-num1>, <severity-num2>, ...
set src {string}
set ssid-policy {string}
set status [enable|disable]
set sw-version {string}
set switch-fortilink {string}
set switch-group <name1>, <name2>, ...
set switch-mac-policy {string}
set type {string}
set user {string}
set user-group {string}
next
end
