from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from integrity import verify_integrity
import json

def decrypt_file(enc_file):
    with open(enc_file + ".meta.json", 'r') as f:
        meta = json.load(f)

    key = bytes.fromhex(meta["key"])
    with open(enc_file, 'rb') as f:
        iv = f.read(16)
        encrypted = f.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted) + unpadder.finalize()

    dec_file = enc_file.replace(".enc", ".dec")
    with open(dec_file, 'wb') as f:
        f.write(data)

    if verify_integrity(dec_file, meta["hash"]):
        print(f"Decryption successful. File integrity verified: {dec_file}")
    else:
        print("WARNING: File integrity check FAILED!")
