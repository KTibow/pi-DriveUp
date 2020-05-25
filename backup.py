try:
    onedrivesdk = 0
    print("Loading...")
    # Requireit
    from pip._internal import main as A;import sys # This is requireit: https://github.com/KTibow/requireit
    class VersionError(Exception):0
    class InstallError(Exception):0
    E="Couldn't auto-install ";F='install'
    def requireit(B):
        for C in B:
            J=C if isinstance(C,str)else C[0]
            try:from importlib import import_module as L
            except ImportError:raise VersionError('Please upgrade Python')
            try: globals()[J]=L(J)
            except ModuleNotFoundError if sys.version_info.minor > 5 else ImportError:
                try:A([F,C]) if isinstance(C,str)else A([F,C[1]]);globals()[J]=L(J)
                except Exception:raise InstallError(E+J)
    requireit([["onedrivesdk", "git+https://github.com/OneDrive/onedrive-sdk-python.git"]])
    if onedrivesdk == 0:
        print("Package error... If there's an exception later, replace this and everything above with \"import onedrivesdk\". Make sure you've installed it with \"pip install git+https://github.com/OneDrive/onedrive-sdk-python.git\" too.")
    # Imports
    import os, asyncio, hashlib, webbrowser
    import urllib.request
    from zipfile import ZipFile
    # Functions
    def hash_file(filename):
       h = hashlib.sha1()
       with open(filename, 'rb') as file:
           chunk = 0
           while chunk != b'':
               chunk = file.read(1024)
               h.update(chunk)
       return h.hexdigest()
    def status(part, total):
        print("about " + str(round((part + 1) / (total + 1) * 10000) / 100.0) + "% complete, " + str(part) + "/" + str(total))
    def download(client, drivename, localname):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(client.item(drive='me', path=drivename).download_async(localname))
except Exception as e:
    print("Couldn't load because of "+str(e)+".")
    webbrowser.open_new("https://ktibow.github.io/pi-DriveUp/loaderror.html")
    exit()
try:
    # Get latest version
    print("Testing latest version...")
    client_id = 'your_client_id'
    bckscript = urllib.request.urlopen("https://github.com/ktibow/pi-driveup/releases/latest/download/backup.py").read().decode().replace("your_"+"client_id", client_id)
    bckfile = open("latestbackup.py", "w")
    bckfile.write(bckscript)
    bckfile.close()
    current = hash_file(__file__)
    latest = hash_file("latestbackup.py")
    if current != latest:
        print("Update available! Re-running...")
        os.system("sudo mv "+os.getcwd()+"/latestbackup.py /root/backup.py; sudo python3 /root/backup.py")
        exit()
except Exception as e:
    print("Couldn't get the latest version of backup.py because of "+str(e)+".")
    webbrowser.open_new("https://ktibow.github.io/pi-DriveUp/latestversionerror.html")
    exit()
# Auth
scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
http_provider = onedrivesdk.HttpProvider()
base_url = 'https://api.onedrive.com/v1.0/'
auth_provider = onedrivesdk.AuthProvider(http_provider,
                                         client_id,
                                         scopes)
auth_provider.load_session()
auth_provider.refresh_token()
client = onedrivesdk.OneDriveClient(base_url, auth_provider, http_provider)
# Compression
backup = ZipFile('thisbackup.zip', 'w')
for dir in ["/home", "/bin", "/boot", "/etc", "/lib", "/lost+found", "/media", "/mnt", "/opt", "/sbin", "/srv", "/usr", "/var"]:
    print("Backing up "+dir+" directory...")
    for folderName, subfolders, filenames in os.walk(dir):
        for filename in filenames:
            # create complete filepath of file in directory
            filePath = os.path.join(folderName, filename)
            # Add file to zip
            try:
                if "singleton" not in filePath.lower() and "cache" not in filePath.lower():
                    backup.write(filePath)
            except FileNotFoundError:
                pass
backup.close()
# Free up **cloud** space
print("Deleting old backups...")
try:
    client.item(drive='me', path="backup.zip").delete()
except Exception as e:
    print("Error deleting " + str(e))
# Upload backup
print("Uploading...")
success = False
iterations = 0
while (not success) and (iterations < 3):
    success = True
    try:
        # Upload file async
        client.item(drive='me', path="backup.zip").upload_async('./thisbackup.zip', upload_status=status)
    except Exception:
        success = False
        if iterations == 0:
            print("Nope, still gotta upload this.")
        elif iterations == 1:
            print("This, it's important.")
        elif iterations == 2:
            print("Fine, fine, I'm done.")
    iterations += 1
print("Freeing up space by deleting local zip backup...")
# Remove local copies to not take up a lot of space
os.remove("thisbackup.zip")
print("Saving session...")
# Save session so if we refreshed it, our session stays valid
auth_provider.save_session()
