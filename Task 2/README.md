
# 🔐 Secure File Storage System with AES-256

## 📌 Objective
A local file encryption and decryption system built using **AES-256** encryption for secure storage. The system ensures file confidentiality and integrity using hashing for tamper detection.

---

## 🧰 Tools & Technologies
- **Python 3**
- [`cryptography`](https://cryptography.io/) – For AES-256 encryption/decryption
- [`hashlib`](https://docs.python.org/3/library/hashlib.html) – For SHA-256 integrity checks
- **CLI-based interface**
- *(Optional GUI: PyQt5)*

---

## 🧭 Features
- 🔐 **AES-256 Encryption** in CBC mode with a random key and IV
- 📁 Encrypt and store files with `.enc` extension
- 📝 Save metadata (original name, timestamp, hash, key) in a `.meta.json` file
- 🔓 Secure decryption using stored key and IV
- ✅ Integrity check using SHA-256 to detect file tampering
- ❌ No cloud, all encryption/decryption is local and offline

---

## 📂 Project Structure
```
secure_file_storage/
├── secure_file_storage.py         # Main script
├── encrypted_files/               # Encrypted outputs
│   ├── myfile.txt.enc
│   ├── myfile.txt.enc.meta.json
├── decrypted_files/               # Decrypted outputs
│   ├── myfile.txt.dec
```

---

## 🚀 How to Run

### 1️⃣ Install Dependencies
```bash
pip install cryptography
```

### 2️⃣ Run the Script
```bash
python secure_file_storage.py
```

---

## 🔐 How It Works

### 🔸 Encryption
1. Generates a random AES-256 key and IV.
2. Encrypts the selected file in CBC mode.
3. Outputs:
   - `.enc` encrypted file.
   - `.meta.json` file with:
     - Original filename
     - Timestamp
     - AES key (hex)
     - SHA-256 file hash

### 🔸 Decryption
1. Reads the key and IV from metadata.
2. Decrypts the `.enc` file.
3. Verifies SHA-256 hash integrity.

---

## ✅ Example Workflow
```bash
# Encrypt a file
python secure_file_storage.py --encrypt mydocument.pdf

# Decrypt a file
python secure_file_storage.py --decrypt mydocument.pdf.enc
```

---

## 🔒 Security Notes
- The AES key is stored in the metadata file in hex format for demo purposes.
  - 🔑 In production, keys should be securely stored or password-derived (PBKDF2).
- IV is prepended to encrypted file for decryption.
- All operations are performed **locally**; no data leaves your machine.

---

## 📜 License
This project is open-source under the MIT License.

---

## ✍️ Author
**Superior Sanjib Vlogs**  
Feel free to fork or contribute!
