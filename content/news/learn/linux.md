Title: Linux 
Date: 16-Sep-2018 12:20:58
Category: Learning Curve
Modified: 16-Sep-2019 12:20:58

This is where I am logging everything I know about Linux. There are so
many distros out there. Whatever here works on debian based system like
Ubuntu or Linux Mint, and might need a slight tinkering for other 
distros.

#### command - ls

- `ls -l` - long listing the file
- `ls -lrt` - list file based on the modified date. recent at the last.

### Installing using deb file
Most of the modern distros support double clicking deb file to install.
Some times, you may need to do the below.

- `chmod +x installer-file.deb` - Give execute permission
- `dpkg -i installer-file.deb` - You may need to use `sudo`

