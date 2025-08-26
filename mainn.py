import os
import sqlite3
import shutil
import sys
from pathlib import Path
import customtkinter as ctk
from tkinter import messagebox
import json
import win32crypt 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def get_chrome_sites():
    login_db_path = os.path.join(os.environ['LOCALAPPDATA'],
                                 r"Google\Chrome\User Data\Default\Login Data")
    if not os.path.exists(login_db_path):
        messagebox.showerror("Error", "Chrome login database not found!")
        return []

    tmp_db = os.path.join(os.environ['TEMP'], "chrome_login_db.db")
    shutil.copy2(login_db_path, tmp_db)

    conn = sqlite3.connect(tmp_db)
    cursor = conn.cursor()
    
    cursor.execute("SELECT origin_url FROM logins")
    sites = [row[0] for row in cursor.fetchall()]

    conn.close()
    os.remove(tmp_db)
    
    sites = sorted(list(set(sites)))
    return sites

class ChromeAccountsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ghosty Chrome Accounts Viewer")
        self.geometry("600x400")
        
        self.label = ctk.CTkLabel(self, text="Saved Chrome Websites:", font=("Arial", 18))
        self.label.pack(pady=10)
        
        self.listbox = ctk.CTkTextbox(self, width=550, height=300)
        self.listbox.pack(padx=10, pady=10)
        
        self.load_button = ctk.CTkButton(self, text="Load Accounts", command=self.load_sites)
        self.load_button.pack(pady=5)

    def load_sites(self):
        self.listbox.delete("0.0", ctk.END)
        sites = get_chrome_sites()
        if sites:
            for site in sites:
                self.listbox.insert(ctk.END, site + "\n")
        else:
            self.listbox.insert(ctk.END, "No saved sites found.")

if __name__ == "__main__":
    app = ChromeAccountsApp()
    app.mainloop()
