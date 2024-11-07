import os
import hashlib
import config

def generate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def initialize():
    hashes = {}
    for directory in config.MONITORED_DIRECTORIES:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                hashes[file_path] = generate_hash(file_path)
    # Store hashes in a JSON file or database
    with open('file_hashes.json', 'w') as f:
        json.dump(hashes, f)

if __name__ == "__main__":
    initialize()
