# raspberrypi-onedrive-backup
A simple way to backup your Raspberry Pi to your OneDrive account using Python 3.  
![image logo for raspberry pi backup to onedrive](backuplogoimg.jpg)
# Installation instructions:
## Installing dependencies
&nbsp;&nbsp;&nbsp;&nbsp;The only dependency is onedrive-sdk-python ([OneDrive/onedrive-sdk-python](https://github.com/OneDrive/onedrive-sdk-python/))! Install it by running this:
```bash
sudo pip3 install git+https://github.com/OneDrive/onedrive-sdk-python.git
```
## Authentication
&nbsp;&nbsp;&nbsp;&nbsp;In order to get OneDrive credentials, we open the [Azure app manager](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade), because the OneDrive API is part of the Microsoft Graph API, which is part of Azure. You may need to sign up for Azure. Once the Azure page loads, click on ![New registration](new_reg.png).  
  
&nbsp;&nbsp;&nbsp;&nbsp;Name your app `OneDrive Backup` to make it easier to find later. Use the default setting for supported account types. For the redirect URI, set the type to `Web` and the URI to `http://localhost:8080/`. Click on `Register` at the bottom, and it'll create your app!  
&nbsp;&nbsp;&nbsp;&nbsp;Yay! Your app is created. Copy the client ID to a place you'll be able to find it later. Now, click on "Certificates and Secrets". Click on "New client secret". Set "Expires" to never (otherwise your backup will stop working!) and don't type anything for the description. Click on "Add", and it'll create the secret. Press the copy button, and put it into your notepad. We're all done!
## Setup
&nbsp;&nbsp;&nbsp;&nbsp;For the next part, backing up your Raspberry Pi, your Raspberry Pi should be running Raspbian. (It's easier to set up with a graphical desktop.) Download [`auth.py`](auth.py?raw=true) onto your Raspberry Pi. If you downloaded this repo as a zip, make sure you extract it to /home/pi, and run it with Python 3. It will guide you. If everything works, you should be ready to start backing up your Raspberry Pi soon!  
&nbsp;&nbsp;&nbsp;&nbsp;You're almost ready. Next, download [`backup.py`](backup.py?raw=true). Change `client_id` to your client ID, and move it to the `/root` directory. That should be it!  
## Running
&nbsp;&nbsp;&nbsp;&nbsp;To manually backup your Pi, do this at the command line:
```bash
sudo python3 /replace/this/with/your/path/to/backup.py
```
## Scheduling
&nbsp;&nbsp;&nbsp;&nbsp;To run it every 3AM (don't worry, it compresses backups, deletes backups more than 1 week old, and removes temporary backup files), you can run this to quickly add it to your crontab: `(sudo crontab -l ; echo "0 3 * * * cd /root; python3 /root/backup.py")| sudo crontab -`. Or to manually run it, do `sudo -s`, type `cd /root`, and then run `python3 /root/backup.py`. (When done, don't forget to exit the sudo shell with "exit" to go back to your shell.) Enjoy your new backup program!  
  
&nbsp;&nbsp;&nbsp;&nbsp;I hope this helped you back up your Pi. Feel free to look around my code and make any pull requests if you need to. Happy backuping!  
