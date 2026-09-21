# config system accprofile

> Source: `config system accprofile.pdf`
> FortiOS 7.4.6 CLI reference extraction. Repeated PDF page headers and footers were omitted.
> Page-boundary carry-over from adjacent CLI sections is retained when it appears in the uploaded PDF.

Parameter Description Type Size Default
init-string Init string in hexadecimal format (even length). string Maximum
length: 127
model MODEM model name. string Maximum
length: 35
modeswitch-
string
USB modeswitch arguments. For example: '-v 1410 -
p 9030 -V 1410 -P 9032 -u 3'.
string Maximum
length: 127
product-id USB product ID in hexadecimal format (0000-ffff). user Not Specified
vendor MODEM vendor name. string Maximum
length: 35
vendor-id USB vendor ID in hexadecimal format (0000-ffff). user Not Specified

### config system accprofile

Configure access profiles for system administrators.

#### Syntax

config system accprofile
Description: Configure access profiles for system administrators.
edit <name>
set admintimeout {integer}
set admintimeout-override [enable|disable]
set authgrp [none|read|...]
set cli-config [enable|disable]
set cli-diagnose [enable|disable]
set cli-exec [enable|disable]
set cli-get [enable|disable]
set cli-show [enable|disable]
set comments {var-string}
set ftviewgrp [none|read|...]
set fwgrp [none|read|...]
config fwgrp-permission
Description: Custom firewall permission.
set address [none|read|...]
set others [none|read|...]
set policy [none|read|...]
set schedule [none|read|...]
set service [none|read|...]
end
set loggrp [none|read|...]
config loggrp-permission
Description: Custom Log & Report permission.
set config [none|read|...]
set data-access [none|read|...]
set report-access [none|read|...]
set threat-weight [none|read|...]
end
set netgrp [none|read|...]
config netgrp-permission
Description: Custom network permission.
set cfg [none|read|...]
set packet-capture [none|read|...]
set route-cfg [none|read|...]
end
set scope [vdom|global]
set secfabgrp [none|read|...]
set sysgrp [none|read|...]
config sysgrp-permission
Description: Custom system permission.
set admin [none|read|...]
set cfg [none|read|...]
set mnt [none|read|...]
set upd [none|read|...]
end
set system-execute-ssh [enable|disable]
set system-execute-telnet [enable|disable]
set utmgrp [none|read|...]
config utmgrp-permission
Description: Custom Security Profile permissions.
set antivirus [none|read|...]
set application-control [none|read|...]
set casb [none|read|...]
set dlp [none|read|...]
set dnsfilter [none|read|...]
set emailfilter [none|read|...]
set endpoint-control [none|read|...]
set file-filter [none|read|...]
set icap [none|read|...]
set ips [none|read|...]
set videofilter [none|read|...]
set virtual-patch [none|read|...]
set voip [none|read|...]
set waf [none|read|...]
set webfilter [none|read|...]
end
set vpngrp [none|read|...]
set wanoptgrp [none|read|...]
set wifi [none|read|...]
next
end

#### Parameters

config system accprofile
Parameter Description Type Size Default
admintimeout Administrator timeout for this access profile. integer Minimum
value: 1
Maximum
value: 480
10
admintimeout-
override
Enable/disable overriding the global administrator idle
timeout.
option - disable
Parameter Description Type Size Default
Option Description
enable Enable overriding the global administrator idle timeout.
disable Disable overriding the global administrator idle timeout.
authgrp Administrator access to Users and Devices. option - none
Option Description
none No access.
read Read access.
read-write Read/write access.
cli-config Enable/disable permission to run config commands. option - disable
Option Description
enable Enable permission to run config commands.
disable Disable permission to run config commands.
cli-diagnose Enable/disable permission to run diagnostic
commands.
option - disable
Option Description
enable Enable permission to run diagnostic commands.
disable Disable permission to run diagnostic commands.
cli-exec Enable/disable permission to run execute commands. option - disable
Option Description
enable Enable permission to run execute commands.
disable Disable permission to run execute commands.
cli-get Enable/disable permission to run get commands. option - disable
Option Description
enable Enable permission to run get commands.
disable Disable permission to run get commands.
cli-show Enable/disable permission to run show commands. option - disable
Option Description
enable Enable permission to run show commands.
