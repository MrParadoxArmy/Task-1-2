# 🔐 Password Strength Analyzer & Custom Wordlist Generator

A Python tool to **analyze password strength** using `zxcvbn` and **generate targeted custom wordlists** based on personal inputs like name, birthdate, and pet name. Ideal for cybersecurity research and password auditing.

---

## 🚀 Features

- 🔍 Analyze password strength using **zxcvbn** (entropy-based model)
- 🛠 Generate **custom wordlists** using:
  - Personal info (name, DOB, pet name)
  - Leetspeak variants
  - Appended common years (1990–2025)
- 📤 Export wordlist to `.txt` format
- 💻 Command-line interface
- 🖼 Optional GUI using Tkinter

---

## 🧰 Tools & Dependencies

- Python 3.6+
- [zxcvbn](https://github.com/dropbox/zxcvbn) – password strength estimator
- `nltk` (optional for future enhancements like stemming)
- `tkinter` – GUI (comes with Python)

Install dependencies:

```bash
pip install zxcvbn nltk
