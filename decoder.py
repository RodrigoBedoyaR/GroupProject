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

#We need the previous key to decrypt the files. 
with open("TheKey.key", "rb") as key:
    secretKey = key.read()

secretWord = "marimba"
userInput = input("Enter the password to unlock the content:\n")

if secretWord == userInput:
    for file in files:
        with open(file, 'rb') as theFile:
            contentOfFiles = theFile.read
        #Decrypt data
        decryptedContent = Fernet(secretKey).decrypt(contentOfFiles)

        with open(file, "wb") as theFile:
            theFile.write(decryptedContent)
    print("Your files have been decrypted")

else:
    print("wrong password")
    
