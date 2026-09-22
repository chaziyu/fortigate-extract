# config ips sensor

> Source: `config ips sensor.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

config metadata
Parameter Description Type Size Default
id ID. Read-only. integer Minimum
value: 0
Maximum
value:
4294967295
0
metaid Meta ID. Read-only. integer Minimum
value: 0
Maximum
value:
4294967295
0
valueid Value ID. Read-only. integer Minimum
value: 0
Maximum
value:
4294967295
0

### config ips sensor

Configure IPS sensor.

#### Syntax

config ips sensor
Description: Configure IPS sensor.
edit <name>
set block-malicious-url [disable|enable]
set comment {var-string}
config entries
Description: IPS sensor filter.
edit <id>
set action [pass|block|...]
set application {user}
set cve <cve-entry1>, <cve-entry2>, ...
set default-action [all|pass|...]
set default-status [all|enable|...]
config exempt-ip
Description: Traffic from selected source or destination IP addresses is
exempt from this signature.
edit <id>
set dst-ip {ipv4-classnet}
set src-ip {ipv4-classnet}
next
end
set last-modified {user}
set location {user}
set log [disable|enable]
set log-attack-context [disable|enable]
set log-packet [disable|enable]
set os {user}
set protocol {user}
set quarantine [none|attacker]
set quarantine-expiry {user}
set quarantine-log [disable|enable]
set rate-count {integer}
set rate-duration {integer}
set rate-mode [periodical|continuous]
set rate-track [none|src-ip|...]
set rule <id1>, <id2>, ...
set severity {user}
set status [disable|enable|...]
set vuln-type <id1>, <id2>, ...
next
end
set extended-log [enable|disable]
set replacemsg-group {string}
set scan-botnet-connections [disable|block|...]
next
end

#### Parameters

config ips sensor
Parameter Description Type Size Default
block-
malicious-url
Enable/disable malicious URL blocking. option - disable
Option Description
disable Disable malicious URL blocking.
enable Enable malicious URL blocking.
comment Comment. var-string Maximum
length: 255
extended-log Enable/disable extended logging. option - disable
Option Description
enable Enable setting.
disable Disable setting.
name Sensor name. string Maximum
length: 35
replacemsg-
group
Replacement message group. string Maximum
length: 35
scan-botnet-
connections
Block or monitor connections to Botnet servers, or
disable Botnet scanning.
option - disable
Parameter Description Type Size Default
Option Description
disable Do not scan connections to botnet servers.
block Block connections to botnet servers.
monitor Log connections to botnet servers.
config entries
Parameter Description Type Size Default
action Action taken with traffic in which signatures are
detected.
option - default
Option Description
pass Pass or allow matching traffic.
block Block or drop matching traffic.
reset Reset sessions for matching traffic.
default Pass or drop matching traffic, depending on the default action of the signature.
application Operating systems to be protected. Use all for every
application and other for unlisted application.
user Not Specified all
cve <cve-
entry>
List of CVE IDs of the signatures to add to the
sensor.
CVE IDs or CVE wildcards.
string Maximum
length: 19
default-action Signature default action filter. option - all
Option Description
all Selects signatures with any default action.
pass Selects signatures with default action 'pass'.
block Selects signatures with default action 'block'.
default-status Signature default status filter. option - all
Option Description
all Selects signatures with any default status.
enable Selects signatures enabled by default.
disable Selects signatures disabled by default.
Parameter Description Type Size Default
id Rule ID in IPS database. integer Minimum
value: 0
Maximum
value:
4294967295
0
last-modified Filter by signature last modified date. Formats:
before <date>, after <date>, between <start-date>
<end-date>.
user Not Specified
location Protect client or server traffic. user Not Specified all
log Enable/disable logging of signatures included in
filter.
option - enable
Option Description
disable Disable logging of selected rules.
enable Enable logging of selected rules.
log-attack-
context
Enable/disable logging of attack context: URL
buffer, header buffer, body buffer, packet buffer.
option - disable
Option Description
disable Disable logging of detailed attack context.
enable Enable logging of detailed attack context.
log-packet Enable/disable packet logging. Enable to save the
packet that triggers the filter. You can download the
packets in pcap format for diagnostic use.
option - disable
Option Description
disable Disable packet logging of selected rules.
enable Enable packet logging of selected rules.
os Operating systems to be protected. Use all for every
operating system and other for unlisted operating
systems.
user Not Specified all
protocol Protocols to be examined. Use all for every protocol
and other for unlisted protocols.
user Not Specified all
quarantine Quarantine method. option - none
Option Description
none Quarantine is disabled.
Parameter Description Type Size Default
Option Description
attacker Block all traffic sent from attacker's IP address. The attacker's IP address is
also added to the banned user list. The target's address is not affected.
quarantine-
expiry
Duration of quarantine. Requires quarantine set to
attacker.
user Not Specified 5m
quarantine-

## log

Enable/disable quarantine logging. option - enable
Option Description
disable Disable quarantine logging.
enable Enable quarantine logging.
rate-count Count of the rate. integer Minimum
value: 0
Maximum
value: 65535
0
rate-duration Duration (sec) of the rate. integer Minimum
value: 1
Maximum
value: 65535
60
rate-mode Rate limit mode. option - continuous
Option Description
periodical Allow configured number of packets every rate-duration.
continuous Block packets once the rate is reached.
rate-track Track the packet protocol field. option - none
Option Description
none none
src-ip Source IP.
dest-ip Destination IP.
dhcp-client-mac DHCP client.
dns-domain DNS domain.
Parameter Description Type Size Default
rule <id> Identifies the predefined or custom IPS signatures
to add to the sensor.
Rule IPS.
integer Minimum
value: 0
Maximum
value:
4294967295
severity Relative severity of the signature, from info to
critical. Log messages generated by the signature
include the severity.
user Not Specified all
status Status of the signatures included in filter. Only those
filters with a status to enable are used.
option - default
Option Description
disable Disable status of selected rules.
enable Enable status of selected rules.
default Default.
vuln-type
<id>
List of signature vulnerability types to filter by.
Vulnerability type ID.
integer Minimum
value: 0
Maximum
value:
4294967295
config exempt-ip
Parameter Description Type Size Default
dst-ip Destination IP address and netmask (applies to
packet matching the signature).
ipv4-
classnet
Not Specified 0.0.0.0
0.0.0.0
id Exempt IP ID. integer Minimum
value: 0
Maximum
value:
4294967295
0
src-ip Source IP address and netmask (applies to packet
matching the signature).
ipv4-
classnet
Not Specified 0.0.0.0
0.0.0.0

### config ips settings

Configure IPS VDOM parameter.

#### Syntax

config ips settings
Description: Configure IPS VDOM parameter.
set ips-packet-quota {integer}
set packet-log-history {integer}
