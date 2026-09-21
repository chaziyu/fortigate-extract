# config user group

> Source: `config user group.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
source-ip6 IPv6 source for communications to FSSO
agent.
ipv6-
address
Not
Specified
::
ssl Enable/disable use of SSL. option - disable
Option Description
enable Enable use of SSL.
disable Disable use of SSL.
ssl-server-
host-ip-check
Enable/disable server host/IP
verification.
option - disable
Option Description
enable Enable server host/IP verification.
disable Disable server host/IP verification.
ssl-trusted-
cert
Trusted server certificate or CA
certificate.
string Maximum
length: 79
type Server type. option - default
Option Description
default All other unspecified types of servers.
fortinac FortiNAC server.
user-info-
server
LDAP server to get user information. string Maximum
length: 35

### config user group

Configure user groups.

#### Syntax

config user group
Description: Configure user groups.
edit <name>
set auth-concurrent-override [enable|disable]
set auth-concurrent-value {integer}
set authtimeout {integer}
set company [optional|mandatory|...]
set email [disable|enable]
set expire {integer}
set expire-type [immediately|first-successful-login]
set group-type [firewall|fsso-service|...]
config guest
Description: Guest User.
edit <id>
set comment {var-string}
set company {string}
set email {string}
set expiration {user}
set mobile-phone {string}
set name {string}
set password {password}
set sponsor {string}
set user-id {string}
next
end
set http-digest-realm {string}
set id {integer}
config match
Description: Group matches.
edit <id>
set group-name {string}
set server-name {string}
next
end
set max-accounts {integer}
set member <name1>, <name2>, ...
set mobile-phone [disable|enable]
set multiple-guest-add [disable|enable]
set password [auto-generate|specify|...]
set sms-custom-server {string}
set sms-server [fortiguard|custom]
set sponsor [optional|mandatory|...]
set sso-attribute-value {string}
set user-id [email|auto-generate|...]
set user-name [disable|enable]
next
end

#### Parameters

config user group
Parameter Description Type Size Default
auth-
concurrent-
override
Enable/disable overriding the global number of
concurrent authentication sessions for this user
group.
option - disable
Option Description
enable Enable auth-concurrent-override.
disable Disable auth-concurrent-override.
auth-
concurrent-
value
Maximum number of concurrent authenticated
connections per user.
integer Minimum
value: 0
Maximum
value: 100
0
Parameter Description Type Size Default
authtimeout Authentication timeout in minutes for this user
group. 0 to use the global user setting auth-
timeout.
integer Minimum
value: 0
Maximum
value: 43200
0
company Set the action for the company guest user field. option - optional
Option Description
optional Optional.
mandatory Mandatory.
disabled Disabled.
email Enable/disable the guest user email address field. option - enable
Option Description
disable Disable setting.
enable Enable setting.
expire Time in seconds before guest user accounts
expire.
integer Minimum
value: 1
Maximum
value:
31536000
14400
expire-type Determine when the expiration countdown begins. option - immediately
Option Description
immediately Immediately.
first-successful-
login
First successful login.
group-type Set the group to be for firewall authentication,
FSSO, RSSO, or guest users.
option - firewall
Option Description
firewall Firewall.
fsso-service Fortinet Single Sign-On Service.
rsso RADIUS based Single Sign-On Service.
guest Guest.
http-digest-
realm
Realm attribute for MD5-digest authentication. string Maximum
length: 35
Parameter Description Type Size Default
id Group ID. Read-only. integer Minimum
value: 0
Maximum
value:
4294967295
0
max-accounts Maximum number of guest accounts that can be
created for this group (0 means unlimited).
integer Minimum
value: 0
Maximum
value: 1024 **
0
member
<name>
Names of users, peers, LDAP severs, RADIUS
servers or external idp servers to add to the user
group.
Group member name.
string Maximum
length: 511
mobile-phone Enable/disable the guest user mobile phone
number field.
option - disable
Option Description
disable Disable setting.
enable Enable setting.
multiple-
guest-add
Enable/disable addition of multiple guests. option - disable
Option Description
disable Disable setting.
enable Enable setting.
name Group name. string Maximum
length: 35
password Guest user password type. option - auto-generate
Option Description
auto-generate Automatically generate.
specify Specify.
disable Disable.
sms-custom-
server
SMS server. string Maximum
length: 35
sms-server Send SMS through FortiGuard or other external
server.
option - fortiguard
Parameter Description Type Size Default
Option Description
fortiguard Send SMS by FortiGuard.
custom Send SMS by custom server.
sponsor Set the action for the sponsor guest user field. option - optional
Option Description
optional Optional.
mandatory Mandatory.
disabled Disabled.
sso-attribute-
value
Name of the RADIUS user group that this local
user group represents.
string Maximum
length: 511
user-id Guest user ID type. option - email
Option Description
email Email address.
auto-generate Automatically generate.
specify Specify.
user-name Enable/disable the guest user name entry. option - disable
Option Description
disable Disable setting.
enable Enable setting.
** Values may differ between models.
config guest
Parameter Description Type Size Default
comment Comment. var-string Maximum
length: 255
company Set the action for the company guest user field. string Maximum
length: 35
email Email. string Maximum
length: 64
expiration Expire time. user Not Specified
Parameter Description Type Size Default
id Guest ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
mobile-phone Mobile phone. string Maximum
length: 35
name Guest name. string Maximum
length: 64
password Guest password. password Not Specified
sponsor Set the action for the sponsor guest user field. string Maximum
length: 35
user-id Guest ID. string Maximum
length: 64
config match
Parameter Description Type Size Default
group-name Name of matching user or group on remote
authentication server.
string Maximum
length: 511
id ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
server-name Name of remote auth server. string Maximum
length: 35

### config user krb-keytab

Configure Kerberos keytab entries.

#### Syntax

config user krb-keytab
Description: Configure Kerberos keytab entries.
edit <name>
set keytab {string}
set ldap-server <name1>, <name2>, ...
set pac-data [enable|disable]
set principal {string}
next
end
