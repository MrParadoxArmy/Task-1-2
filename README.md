# 🔐 Secure File Storage System with AES-256 & Password Strength Analyzer with Wordlist Generator

## 📌 Overview

This repository contains two security-focused tools:

### ✅ Task 1: **AES File Storage System**
A secure local file storage system using AES-256 encryption with integrity checks.

### ✅ Task 2: **Password Analyzer & Wordlist Generator**
A password strength evaluation tool with the ability to generate custom wordlists from personal inputs.

---

## 🧰 Technologies Used
- **Python 3**
- `cryptography` – AES encryption
- `hashlib` – File hashing (SHA-256)
- `argparse` – Command-line interface
- `zxcvbn` – Password strength scoring
- `nltk` – Wordlist processing (optional)
- `PyQt5` (optional GUI)

---

# 🗂️ Project Structure

├── task1_aes_file_storage/
│ ├── secure_file_storage.py
│ ├── encryptor.py
│ ├── decryptor.py
│ ├── integrity.py
│ └── README.md
│
├── task2_password_analyzer/
│ ├── password_analyzer.py
│ ├── wordlist_generator.py
│ ├── sample_inputs.txt
│ └── README.md


---

# 🔒 Task 1: AES File Storage System

### ✅ Features
- Encrypt files using **AES-256 (CBC mode)**
- Store encrypted files with `.enc` extension
- Save metadata: filename, hash (SHA-256), key, timestamp
- Decrypt files and verify integrity
- Fully CLI-based (optionally GUI)

### 🔧 How to Use
```bash
pip install cryptography
python secure_file_storage.py --encrypt myfile.txt
python secure_file_storage.py --decrypt myfile.txt.enc
