# config firewall profile-group

> Source: `config firewall profile group.pdf`
> Repeated FortiOS page headers and footers were omitted.
> CLI spelling and parameter terminology follow the FortiOS 7.4.6 reference.

### config firewall profile-group

Configure profile groups.

#### Syntax

```text

config firewall profile-group
Description: Configure profile groups.
edit <name>
set application-list {string}
set av-profile {string}
set casb-profile {string}
set cifs-profile {string}
set diameter-filter-profile {string}
set dlp-profile {string}
set dnsfilter-profile {string}
set emailfilter-profile {string}
set file-filter-profile {string}
set icap-profile {string}
set ips-sensor {string}
set ips-voip-filter {string}
set profile-protocol-options {string}
set sctp-filter-profile {string}
set ssh-filter-profile {string}
set ssl-ssh-profile {string}
set videofilter-profile {string}
set virtual-patch-profile {string}
set voip-profile {string}
set waf-profile {string}
set webfilter-profile {string}
next
end

```

#### Parameters

```text

config firewall profile-group
Parameter Description Type Size Default
application-
list
Name of an existing Application list. string Maximum
length: 35
av-profile Name of an existing Antivirus profile. string Maximum
length: 35
casb-profile Name of an existing CASB profile. string Maximum
length: 35
cifs-profile Name of an existing CIFS profile. string Maximum
length: 35
diameter-
filter-profile
Name of an existing Diameter filter profile. string Maximum
length: 35
dlp-profile Name of an existing DLP profile. string Maximum
length: 35
Parameter Description Type Size Default
dnsfilter-
profile
Name of an existing DNS filter profile. string Maximum
length: 35
emailfilter-
profile
Name of an existing email filter profile. string Maximum
length: 35
file-filter-
profile
Name of an existing file-filter profile. string Maximum
length: 35
icap-profile Name of an existing ICAP profile. string Maximum
length: 35
ips-sensor Name of an existing IPS sensor. string Maximum
length: 35
ips-voip-filter Name of an existing VoIP (ips) profile. string Maximum
length: 35
name Profile group name. string Maximum
length: 35
profile-
protocol-
options
Name of an existing Protocol options profile. string Maximum
length: 35
default
sctp-filter-
profile
Name of an existing SCTP filter profile. string Maximum
length: 35
ssh-filter-
profile
Name of an existing SSH filter profile. string Maximum
length: 35
ssl-ssh-profile Name of an existing SSL SSH profile. string Maximum
length: 35
certificate-
inspection
videofilter-
profile
Name of an existing VideoFilter profile. string Maximum
length: 35
virtual-patch-
profile
Name of an existing virtual-patch profile. string Maximum
length: 35
voip-profile Name of an existing VoIP (voipd) profile. string Maximum
length: 35
waf-profile Name of an existing Web application firewall profile. string Maximum
length: 35
webfilter-
profile
Name of an existing Web filter profile. string Maximum
length: 35

```

### config firewall profile-protocol-options

Configure protocol options.
