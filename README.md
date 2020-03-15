# raspberrypi-onedrive-backup
A simple way to backup your Raspberry Pi to your OneDrive account using Python 3.
To start, install [onedrive-sdk-python](https://github.com/OneDrive/onedrive-sdk-python/) by running `sudo pip3 install git+https://github.com/OneDrive/onedrive-sdk-python.git`. Once installed, you'll need a client ID and secret. Here's how to get it.  
  
Click [here](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade) to open the Azure app manager. You may need to sign up for Azure. Once the Azure page loads, click on "New registration".
  
Name your app "OneDrive Backup". Don't worry, these names aren't a unique identifier. The default setting for supported account types is fine. For the redirect URI, set the type to Web and the URI to `http://localhost:8080/`. Click on "Register" at the bottom, and it'll create your app.  
  
Yay! Your app is created. Copy the client ID to a notepad. Now, click on "Certificates and Secrets". Click on "New client secret". Set "Expires" to never (otherwise your backup will stop working) and don't type anything for the description. Click on "Add", and it'll create the secret. Press the copy button, and put it into your notepad. Close Azure, because we've got everything we need!  
  
For the next part, backing up your Raspberry Pi, your Raspberry Pi should be running Raspbian with a graphical desktop. Download `auth.py` onto your Raspberry Pi. If you downloaded this as a zip, make sure you extract it to /home/pi, and run it with Python 3. It will guide you. If everything works, you should be ready to start backing up your Raspberry Pi soon!  
  
You're almost ready. Next, download `backup.py`. Change `client_id` to your client ID, and move it to the `/root` directory with `sudo mv /home/pi/Downloads/backup.py /root/backup.py`. If the downloaded file isn't at `/home/pi/Downloads/backup.py`, adjust it accordingly. That should be it! To run it every 3AM (don't worry, it compresses backups, deletes backups more than 1 week old, and removes temporary backup files), you can run this to quickly add it to your crontab: `(sudo crontab -l ; echo "0 3 * * * cd /root; python3 /root/backup.py")| sudo crontab -`. Or to manually run it, do `sudo -s`, type `cd /root`, and then run `python3 /root/backup.py`. (When done, don't forget to exit the sudo shell with "exit" to go back to your shell.)
  
I hope this helped you back up your Pi. Feel free to look around my code and make any pull requests if you need to. Happy backuping!  
