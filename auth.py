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
print("Auth code set up. You only need to run this once, unless you start getting errors.")
