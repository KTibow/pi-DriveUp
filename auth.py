onedrivesdk = 0
from pip._internal import main as A # This is requireit: https://github.com/KTibow/requireit
class VersionError(Exception):0
class InstallError(Exception):0
E="Couldn't auto-install ";F='install'
def requireit(B):
	for C in B:
		J=C if isinstance(C,str)else C[0]
		try:from importlib import import_module as L
		except ImportError:raise VersionError('Please upgrade Python')
		try: globals()[J]=L(J)
		except ModuleNotFoundError:
			try:A([F,C]) if isinstance(C,str)else A([F,C[1]]);globals()[J]=L(J)
			except Exception:raise InstallError(E+J)
requireit([["onedrivesdk", "git+https://github.com/OneDrive/onedrive-sdk-python.git"]])
if onedrivesdk == 0:
	print("Package error... If there's an exception later, replace this and everything above with \"import onedrivesdk\". Make sure you've installed it with \"pip install git+https://github.com/OneDrive/onedrive-sdk-python.git\" too.")
import os, urllib.request
from onedrivesdk.helpers import GetAuthCodeServer
from time import sleep

redirect_uri = 'http://localhost:8080/'
print("What's your client secret? Make sure you didn't copy anything else.")
client_secret = input("Paste it in and press enter: ")
scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
client_id=input("What's your client ID? Make sure you didn't copy anything else. Paste it in and press enter: ")
client = onedrivesdk.get_default_client(
    client_id=client_id, scopes=scopes)

auth_url = client.auth_provider.get_auth_url(redirect_uri)

print("A blank webpage will pop up in 7 seconds. If it says that it couldn't connect, then re-run this script.")
print("It will automatically close itself.")
sleep(7)
print("If a window doesn't pop up in the next few seconds, or if")
print("this machine doesn't have an accesible web browser, copy and paste ")
print(auth_url)
print(" into your browser.")
# this will block until we have the code
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

client.auth_provider.authenticate(code, redirect_uri, client_secret)

client.auth_provider.save_session()
os.system("sudo mv "+os.getcwd()+"/session.pickle /root/session.pickle")
print("Auth code set up. You only need to run this once, unless you start getting errors.")
print("Downloading backup.py and moving it...")
bckscript = str(urllib.request.urlopen("https://github.com/ktibow/pi-driveup/releases/latest/download/backup.py").read()).replace("your_client_id", client_id)
bckfile = open("backup.py", "w")
bckfile.write(bckscript)
bckfile.close()
os.system("sudo mv "+os.getcwd()+"/backup.py /root/backup.py")
print("Done! Opening the docs.")
import webbrowser
webbrowser.open_new("https://ktibow.github.io/pi-DriveUp/#running")
