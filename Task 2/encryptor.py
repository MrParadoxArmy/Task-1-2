from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from integrity import get_file_hash
import os, time, json

def encrypt_file(file_path):
    key = os.urandom(32)  # AES-256 key
    iv = os.urandom(16)   # 128-bit IV
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as f:
        data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    enc_file = file_path + ".enc"
    with open(enc_file, 'wb') as f:
        f.write(iv + encrypted)

    file_hash = get_file_hash(file_path)
    meta = {
        "original": os.path.basename(file_path),
        "encrypted": os.path.basename(enc_file),
        "timestamp": time.ctime(),
        "hash": file_hash,
        "key": key.hex()
    }
    with open(enc_file + ".meta.json", 'w') as f:
        json.dump(meta, f, indent=4)

    print(f"Encrypted: {enc_file}")
