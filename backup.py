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
import urllib.request
import asyncio
from zipfile import ZipFile
import hashlib
def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()
client_id = 'your_client_id'
print("Testing latest version...")
bckscript = str(urllib.request.urlopen("https://github.com/ktibow/pi-driveup/releases/latest/download/backup.py").read()).replace("your_"+"client_id", client_id)
bckfile = open("latestbackup.py", "w")
bckfile.write(bckscript)
bckfile.close()
current = hash_file(__file__)
latest = hash_file("latestbackup.py")
if current != latest:
	print("Update available! Re-running...")
	os.system("sudo mv "+os.getcwd()+"/latestbackup.py /root/backup.py; sudo python3 /root/backup.py")
	exit()
scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
http_provider = onedrivesdk.HttpProvider()
base_url = 'https://api.onedrive.com/v1.0/'
auth_provider = onedrivesdk.AuthProvider(http_provider,
                                         client_id,
                                         scopes)
auth_provider.load_session()
auth_provider.refresh_token()
client = onedrivesdk.OneDriveClient(base_url, auth_provider, http_provider)


def status(part, total):
    print("about" + str(round((part + 1) / (total + 1) * 10000) / 100.0) + "% complete, " + str(part) + "/" + str(total))


def download(client, drivename, localname):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.item(drive='me', path=drivename).download_async(localname))


backup = ZipFile('thisbackup.zip', 'w')
print("Backing up home directory...")
for folderName, subfolders, filenames in os.walk("/home/"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "Singleton" not in filePath and "Cache" not in filePath:
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /bin...")
for folderName, subfolders, filenames in os.walk("/bin"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /boot...")
for folderName, subfolders, filenames in os.walk("/boot"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /etc...")
for folderName, subfolders, filenames in os.walk("/etc"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /lib...")
for folderName, subfolders, filenames in os.walk("/lib"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /lost+found...")
for folderName, subfolders, filenames in os.walk("/lost+found"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /media...")
for folderName, subfolders, filenames in os.walk("/media"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /mnt...")
for folderName, subfolders, filenames in os.walk("/mnt"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /opt...")
for folderName, subfolders, filenames in os.walk("/opt"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /sbin...")
for folderName, subfolders, filenames in os.walk("/sbin"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /srv...")
for folderName, subfolders, filenames in os.walk("/srv"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /usr...")
for folderName, subfolders, filenames in os.walk("/usr"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
print("Backing up /var...")
for folderName, subfolders, filenames in os.walk("/var"):
    for filename in filenames:
        # create complete filepath of file in directory
        filePath = os.path.join(folderName, filename)
        # Add file to zip
        try:
            if "cache" not in filePath.lower():
                backup.write(filePath)
        except FileNotFoundError:
            pass
backup.close()
print("Deleting old backups...")
try:
    client.item(drive='me', path="backup.zip").delete()
except Exception as e:
    print("Error deleting " + str(e))
print("Uploading...")
success = False
iterations = 0
while (not success) and (iterations < 3):
    success = True
    try:
        client.item(drive='me', path="backup.zip").upload_async('./thisbackup.zip', upload_status=status)
    except KeyboardInterrupt:
        success = False
        if iterations == 0:
            print("Nope, still gotta upload this.")
        elif iterations == 1:
            print("This, it's important.")
        elif iterations == 2:
            print("Fine, fine, I'm done.")
    except Exception:
        success = False
    iterations += 1
print("Freeing up space by deleting local zip backup...")
os.remove("thisbackup.zip")
print("Saving session...")
auth_provider.save_session()
