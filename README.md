# MOTD
Linux summary system information display right after your login into the system. Objective of this script is to show the existing summary of system informations such as hostname, ip address, load average, etc.

To setup the script is very straightforward where we just need to copy the shell script and store it in the /usr/loca/bin.

### Step as follows:


1. Copy the script to /usr/local/bin/
```sh
$ sudo cp banner /usr/local/bin/
```

2. Modify the /etc/profile so all users will get the same system information once they login and add /usr/local/bin/banner to the end of the file.

3. Re-login to the system again.

