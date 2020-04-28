import onedrivesdk
import os
import asyncio
from zipfile import ZipFile

scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
http_provider = onedrivesdk.HttpProvider()
client_id = 'your_client_id'
base_url = 'https://api.onedrive.com/v1.0/'
auth_provider = onedrivesdk.AuthProvider(http_provider,
                                         client_id,
                                         scopes)
auth_provider.load_session()
auth_provider.refresh_token()
client = onedrivesdk.OneDriveClient(base_url, auth_provider, http_provider)


def status(part, total):
    print(str(round((part+1)/(total+1)*10000)/10.0)+"% complete, "+str(part)+"/"+str(total))


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
    print("Error deleting "+str(e))
print("Uploading...")
success = False
iterations = 0
while (not success) and (iterations < 3):
    success = True
    try:
        client.item(drive='me', path="backup.zip").upload_async('./thisbackup.zip', upload_status=status)
    except KeyboardInterrupt:
        print("Okay, okay, bye.")
        success = True
    except Exception:
        success = False
    iterations += 1
print("Freeing up space by deleting local zip backup...")
os.remove("backup.zip")
print("Saving session...")
auth_provider.save_session()
