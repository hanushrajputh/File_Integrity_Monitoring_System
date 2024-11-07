import hashlib
import json

def check_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    current_hash = sha256_hash.hexdigest()
    
    # Load stored hash
    with open('file_hashes.json', 'r') as f:
        hashes = json.load(f)
    
    return hashes.get(file_path) == current_hash
