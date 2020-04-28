import onedrivesdk
import os
from onedrivesdk.helpers import GetAuthCodeServer
from time import sleep

redirect_uri = 'http://localhost:8080/'
print("What's your client secret? Make sure you didn't copy anything else.")
client_secret = input("Paste it in and press enter: ")
scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

client = onedrivesdk.get_default_client(
    client_id=input("What's your client ID? Make sure you didn't copy anything else. Paste it in and press enter: "), scopes=scopes)

auth_url = client.auth_provider.get_auth_url(redirect_uri)

print("A blank webpage will pop up in 10 seconds. If it says that it couldn't connect, then re-run this script.")
print("It will automatically close itself.")
sleep(10)
print("If a window doesn't pop up in the next few seconds, or if")
print("this machine doesn't have an accesible web browser, copy and paste ")
print(auth_url)
print(" into your browser.")
# this will block until we have the code
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

client.auth_provider.authenticate(code, redirect_uri, client_secret)

client.auth_provider.save_session()
os.system("sudo mv /home/pi/session.pickle /root/session.pickle")
print("Auth code set up. You only need to run this once, unless you start getting exceptions.")
