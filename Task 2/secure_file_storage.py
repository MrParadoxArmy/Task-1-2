from encryptor import encrypt_file
from decryptor import decrypt_file
from integrity import get_file_hash, verify_integrity
import argparse

parser = argparse.ArgumentParser(description="AES-256 Secure File Storage")
parser.add_argument("--encrypt", help="Path to file to encrypt")
parser.add_argument("--decrypt", help="Path to file to decrypt")
args = parser.parse_args()

if args.encrypt:
    encrypt_file(args.encrypt)
elif args.decrypt:
    decrypt_file(args.decrypt)
else:
    print("Use --encrypt <file> or --decrypt <file>")
