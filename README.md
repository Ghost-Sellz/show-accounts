# Ghosty Chrome Accounts Viewer

A Python application with a **CustomTkinter GUI** that displays websites saved in **Google Chrome's login database**.  
This tool helps you see all the sites where login credentials are stored inside Chrome.

---

## ✨ Features
- Reads Chrome's `Login Data` SQLite database.
- Extracts and displays saved website URLs.
- Dark-mode GUI built with **CustomTkinter**.
- Error handling if the Chrome database is missing.
- Lightweight, simple, and clean interface.

---

## 📦 Requirements
Ensure you have **Python 3.8+** installed.  
Install dependencies with:

```bash
pip install customtkinter pypiwin32
```

---

## 🛠️ How It Works
- Copies Chrome's Login Data SQLite file to a temporary folder.
- Runs a SQL query to fetch origin_url values.
- Displays unique websites in the GUI.
- Cleans up by deleting the temporary database copy.

---

## ▶️ Usage
``` bash
git clone https://github.com/Ghost-Sellz/show-accounts
cd show-account
```
- run the script
  ``` bash
  python mainn.py
  ```

---

# 🤝 Contributing
Contributions are welcome!
To contribute:

1. Fork this repository.
   
3. Create a new branch:
``` bash
git checkout -b feature-name
```
3. Commit your changes:
``` bash
git commit -m "Add new feature"
```
4. Push the branch:
``` bash
git push origin feature-name
```
5. Open a Pull Request.


