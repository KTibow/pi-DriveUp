# raspberrypi-onedrive-backup
A simple way to backup your Raspberry Pi to your OneDrive account using Python 3.
To start, install [onedrive-sdk-python](https://github.com/OneDrive/onedrive-sdk-python/) by running `sudo pip3 install git+https://github.com/OneDrive/onedrive-sdk-python.git`. Once installed, you'll need a client ID and secret. I did it in a hacky way because I couldn't find how to do it otherwise:  
  
Go to this link: https://developer.microsoft.com/en-us/graph/quick-start and select Python. **Alert: before doing this, read ahead.** Click on "Get an app ID and secret". If you're prompted to sign in, sign in to your Microsoft account, but as soon as the URL changes, close the tab. **Alert: before doing this, read ahead.** Instead click on this link, which will work for us: 
  
https://apps.dev.microsoft.com/?referrer=https%3a%2f%2fdeveloper.microsoft.com%2fen-us%2fgraph%2fquick-start%3flanguage%3dpython#/quickstart/graphIO?publicClientSupport=false&appName=My%20Python%20App&redirectUrl=http://localhost:8080/&allowImplicitFlow=false&ru=https%3A%2F%2Fdeveloper.microsoft.com%2Fen-us%2Fgraph%2Fquick-start%3FappID%3D_appId_%26appName%3D_appName_%26redirectUrl%3Dhttp%3A%2F%2Flocalhost%3A8080%2F%26platform%3Doption-Python  
  
Basically, if you're curious about what's going on, it was going to have us use code that uses the URL http://localhost:8000/tutorial/callback, but our code uses http://localhost:8080, so we have to tell Microsoft to redirect to that URL or otherwise our code won't work.  
  
Now once you click on that link, wait for it to get your credentials. Click on "Copy to clipboard", and put it in a text editor. You'll need it. Now click on "Got it, take me back to the quick start". Copy your "App ID (or Client ID)" and paste that in the text editor too (on seperate lines I hope!) We don't need the quick start any more, so close it.  
  
For the next part, backing up your Raspberry Pi, your Raspberry Pi should be running Raspbian with a graphical desktop. Download `auth.py` onto your Raspberry Pi, and run it with Python 3. It will guide you. If everything works, you should be ready to start backing up your Raspberry Pi soon!  
  
You're almost ready. Next, download `backup.py`. Change `client_id` to your client ID, and move it to the `/root` directory with `sudo mv /home/pi/Downloads/backup.py /root/backup.py`. If the downloaded file isn't at `/home/pi/Downloads/backup.py`, adjust it accordingly.
