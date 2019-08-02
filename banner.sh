#!/bin/bash

# 20180316
# Memory calculation reference
# https://unix.stackexchange.com/questions/152299/how-to-get-memory-usedram-used-using-linux-command

hostname=`hostname -f`
echo "
System Status:
Date/Time: `TZ='Asia/Kuala_Lumpur' date`
Total User: `w | head -1 | awk '{ print $6}'`

- Server Name           = `hostname -A`
- Local IP Address      = `hostname --ip-address`
- Load Average          = `cat /proc/loadavg`
- System Uptime         = `uptime | awk '{ print $3 " " $4}'`
- System Data           = `uname -orpi`
- CPU Usage             = `grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'` %
- Memory Usage (Actual) = `free -m| awk 'FNR == 3 {print $3/($3+$4)*100}'` %
- Memory Free (Cache)   = `free -m | head -n 3 | tail -n 1 | awk '{print $3}'` Mb
- Swap in use           = `free -m | tail -n 1 | awk {'print $3'}`
- Disk Space Used       = `df -h / | awk '{ a = $3 } END { print a }'`
- Disk Space Avaible    = `df -h / | awk '{ a = $4 } END { print a }'`
- Alias			= `grep -i alias $HOME/.bash_profile`

Notes:
Command to block IP: $~ iptables -A INPUT -s 42.123.81.144 -j DROP
Command to save iptables: $~ service iptables save
"

