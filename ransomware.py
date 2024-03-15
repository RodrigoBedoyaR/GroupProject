import socket;

def whichOS(taget_host, target_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout to handle unresponsive hosts
        s.settimeout(2)
        #Connect to the target host and port
        s.connect(taget_host, target_port)
        #send banner to request
        s.send(b'Hello there \r\n')
        response = s.recv(1024)
        s.close

        if b'Windows' in response:
            return "Windows OS"
        elif b'Linux' in response:
            return "Linux OS"
        elif b'Darwin' in response:
            return "macOS"
        else:
            return "idk bro"
        
    except Exception as e:
        return str(e)

print("Target host:")
target_host = input()
print ("Target Port:")
target_port = input()

print(f'OS detected on {target_host}:{target_port}: {whichOS(target_host, target_port)}')
