# raspberrypi-onedrive-backup
![image logo for raspberry pi backup to onedrive](backuplogoimg.jpg)
A simple way to backup your Raspberry Pi to your OneDrive account using Python 3.  
# Installation instructions:
## Installing dependencies
onedrive-sdk-python ([https://github.com/OneDrive/onedrive-sdk-python/](https://github.com/OneDrive/onedrive-sdk-python/)) is the only dependency! Install it by running this to get the latest version:
```bash
sudo pip3 install git+https://github.com/OneDrive/onedrive-sdk-python.git
```
## Authentication
In order to get OneDrive credentials, we open the [Azure app manager](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade), because the OneDrive API is part of the Microsoft Graph API, which is part of Azure. You may need to sign up for Azure. Once the Azure page loads, click on "New registration".
  
Name your app "OneDrive Backup" to make it easier to find later. Don't worry, these names aren't a unique identifier, so if I name my app that it's okay if your app is named that too. The default setting for supported account types is fine. For the redirect URI, set the type to Web and the URI to `http://localhost:8080/`. Click on "Register" at the bottom, and it'll create your app!  
  
Yay! Your app is created. Copy the client ID to a place you'll be able to find it later. Now, click on "Certificates and Secrets". Click on "New client secret". Set "Expires" to never (otherwise your backup will stop working!) and don't type anything for the description. Click on "Add", and it'll create the secret. Press the copy button, and put it into your notepad. Close the browser window with Azure, because we've got everything we need!  
## Setup
For the next part, backing up your Raspberry Pi, your Raspberry Pi should be running Raspbian. (It's easier with a graphical desktop.) Download [auth.py](auth.py?raw=true) onto your Raspberry Pi. If you downloaded this repo as a zip, make sure you extract it to /home/pi, and run it with Python 3. It will guide you. If everything works, you should be ready to start backing up your Raspberry Pi soon!  
  
You're almost ready. Next, download `backup.py`. Change `client_id` to your client ID, and move it to the `/root` directory with `sudo mv /home/pi/Downloads/backup.py /root/backup.py`. If the downloaded file isn't at `/home/pi/Downloads/backup.py`, adjust it accordingly. That should be it!
## Scheduling
To run it every 3AM (don't worry, it compresses backups, deletes backups more than 1 week old, and removes temporary backup files), you can run this to quickly add it to your crontab: `(sudo crontab -l ; echo "0 3 * * * cd /root; python3 /root/backup.py")| sudo crontab -`. Or to manually run it, do `sudo -s`, type `cd /root`, and then run `python3 /root/backup.py`. (When done, don't forget to exit the sudo shell with "exit" to go back to your shell.) Enjoy your new backup program!
  
I hope this helped you back up your Pi. Feel free to look around my code and make any pull requests if you need to. Happy backuping!  
