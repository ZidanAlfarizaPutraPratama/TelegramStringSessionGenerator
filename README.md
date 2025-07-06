# 🔐 Telegram String Session Generator

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Telethon Version](https://img.shields.io/pypi/v/telethon?color=blue&label=Telethon&logo=python)](https://pypi.org/project/telethon/)
[![Pyrogram Version](https://img.shields.io/pypi/v/pyrogram?color=orange&label=Pyrogram&logo=python)](https://pypi.org/project/pyrogram/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@zidanAlfarizaPutraPratama-0088cc?logo=telegram)](https://t.me/paradoxtrines)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/ZidanAlfarizaPutraPratama/TelegramStringSessionGenerator?color=informational)](https://github.com/ZidanAlfarizaPutraPratama/TelegramStringSessionGenerator)

Generate **Telethon** and **Pyrogram v2.x** string sessions quickly and easily from your terminal.

![Telegram Session Generator](./Assets/image.png)

> By: [@Zidan Alfariza Putra Pratama](https://github.com/ZidanAlfarizaPutraPratama)

---

## ✨ Features

- ✅ Support for **Telethon** and **Pyrogram v2+**
- ✅ Saves string session to `.txt` file automatically
- ✅ Copies the string to clipboard (if supported)
- ✅ Clear terminal UI with `colorama`
- ✅ Handles common errors like `FLOOD_WAIT`

---

## 🚀 Installation

1. **Clone the repo or download** the `generate_session.py` file.

2. (Optional but recommended) **Create and activate a virtual environment**:

```bash
python -m venv python
# Windows
source python/Scripts/activate
# macOS/Linux
source python/bin/activate
````

3. **Install the required dependencies**:

```bash
pip install telethon pyrogram tgcrypto colorama pyperclip
```

---

## 🧪 Usage

Run the script using Python:

```bash
python generate_session.py
```

Then follow the instructions:

* Choose session type: `1` (Telethon) or `2` (Pyrogram)
* Enter your `API_ID` and `API_HASH` (get from [my.telegram.org](https://my.telegram.org))
* Enter your phone number and verification code

---

## 📁 Output

* 📝 String session saved as:

  * `telethon_custom_string.txt` (for Telethon)
  * `pyrogram_custom_string.txt` (for Pyrogram)
* 📋 String session is also copied to your clipboard (if `pyperclip` works)

---

## ⚠️ Notes

* **FLOOD\_WAIT Error**: If you attempt login too frequently, Telegram may block login temporarily. The script will tell you how long you must wait.
* If blocked, try using a different account or IP (e.g. VPN).

---

## 🧑‍💻 Author

Created by [@Zidan Alfariza Putra Pratama](https://t.me/ziddev)

---

## 🛡️ Disclaimer

This tool is for educational and development purposes only. Do not use it to violate [Telegram's Terms of Service](https://telegram.org/tos).
