# MOTD
Linux summary system information display right after your login into the system. Objective of this script is to show the existing summary of system informations such as hostname, ip address, load average, etc.

To setup the script is very straightforward where we just need to copy the shell script and store it in the /usr/loca/bin.

# Pre-requisite;
+ Need to install lshw;
```sh
$ sudo yum install lshw
```

### Step as follows:


1. Clone the script and copy the script to /usr/local/bin/
```sh
$ cd /opt; git clone git@github.com:armadadigital/motd.git;
$ sudo ln -s /opt/motd/banner /usr/local/bin/banner
```

2. Modify the /etc/profile or .bash_profile ( if you dont have admin priviledges ) so all users will get the same system information once they login and add /usr/local/bin/banner to the end of the file.

3. Re-login to the system again.

