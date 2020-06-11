pi-DriveUp is a simple way to backup your Raspberry Pi to your OneDrive account using Python 3.  
![flake8 python lint](https://github.com/KTibow/pi-drive-up/workflows/flake8%20python%20lint/badge.svg)  
![Dependencies are auto-installed](https://img.shields.io/badge/dependencies-auto--installed%20by%20requireit-099)  
<a href="#" class="readmelogo"><img alt="back up to onedrive logo" src="https://github.com/KTibow/pi-DriveUp/raw/master/assets/backuplogoimg.jpg" /></a>
# Installation instructions:
[Requireit automatically installs](https://github.com/KTibow/requireit) `onedrive-sdk-python`, the only dependency.  
If you want to make sure it's installed, manually install it by running this:
```bash
pip3 install git+https://github.com/OneDrive/onedrive-sdk-python.git --user
# or on systems where python means python3
pip install git+https://github.com/OneDrive/onedrive-sdk-python.git --user
```
## Authentication
1. In order to get OneDrive access credentials, we open the [Azure app manager](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade). You may need to sign up for Azure (for free).
2. Once the Azure page loads, click on ![New registration](assets/new_reg.png).
3. Name your app `OneDrive Backup` to make it easier to find later.
4. Use the default setting for supported account types.
5. For the redirect URI, set the type to `Web` and the URI to `http://localhost:8080/`.
6. Click on ![Register](assets/accept_reg.png) at the bottom, and it'll create your app!  
7. Copy the client ID to a place you'll be able to find it later.
8. Click on ![Certificates and Secrets](assets/certs_secrets.png). Click on ![New secret](assets/new_secret.png). 
9. Make sure you choose ![Never](assets/never.png) for ![Expires](assets/expires.png) (otherwise your backup will stop working!). Don't type anything for the description.
10. Click on ![Add](assets/add_secret.png), and it'll create the secret.
11. Press the copy button, and put it into your notepad.  
  
That's all the steps needed for getting your credentials!  
    
## Setup
&nbsp;&nbsp;&nbsp;&nbsp;For the next part, backing up your Raspberry Pi, your Raspberry Pi should be running [Raspbian](https://www.raspberrypi.org/downloads/).  
  
1. Download <a id="raw-url" href="https://github.com/ktibow/pi-driveup/releases/latest/download/auth.py" download>auth.py</a> onto your Raspberry Pi.
2. Run it with Python 3. It will guide you through setting up the backup program. 

Note: You need to be a member of `sudoers` for `auth.py` to work. Also, *just to clarify*, this is meant to run on a Raspberry Pi.
  
## Running
In order to run this script, **you must have a fair bit of spare memory** on your SD card.
It compresses your whole disk into a `.zip` and stores it locally until it uploads.
Also note that **this won't always upload**; OneDrive can be flakey sometimes.  
&nbsp;&nbsp;&nbsp;&nbsp;To manually backup your Pi, do this at the command line:
```bash
sudo -s
cd /root
python3 /root/backup.py
exit
```
## Scheduling
&nbsp;&nbsp;&nbsp;&nbsp;To run it every 3AM, I'd recommend you add it to your crontab. Don't worry, it automatically deletes local backups. You can run this to quickly add it:
```bash
(sudo crontab -l ; echo "0 3 * * * cd /root; python3 /root/backup.py") | sudo crontab -
```
**Warning:** When you run that, it'll initially say `no crontab for root` if you haven't edited the root crontab yet. Don't worry, it's there. Run it twice, and you'll have two backups, which could lead to problems. List your current root crontab with `sudo crontab -l`.
  
&nbsp;&nbsp;&nbsp;&nbsp;I hope this helped you back up your Pi. Feel free to look around my code and do anything you want with it (at least under the license 😋). Happy backuping!  
