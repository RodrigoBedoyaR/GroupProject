import sys
import platform
import os

def OS_name():
    OS = sys.platform
    if OS == "darwin":
        return "macOS"
    elif OS == "linux":
        return "Linux"
    elif OS == "win32" or "msys" or "cygwin":
        return "Windows"
    else:
        return "Unknown OS"
    

print (f'OS is: {OS_name()} \nVersion: {platform.platform()}')