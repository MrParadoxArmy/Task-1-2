import hashlib

def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def verify_integrity(file_path, expected_hash):
    return get_file_hash(file_path) == expected_hash
