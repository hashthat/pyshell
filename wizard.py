#!/usr/bin/env python3
import os
import subprocess
import tkinter as tk
from tkinter import messagebox
import webbrowser

def install_dependencies():
    """Install Git, Python, Tkinter, and Neofetch."""
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "git", "python3", "python3-pip", "python3-tk", "neofetch"], check=True)
        messagebox.showinfo("Installation Successful", "Git, Python, Tkinter, and Neofetch installed successfully.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to install dependencies. Ensure you have sudo privileges and an internet connection.")

def generate_ssh_key():
    """Generates an SSH key and displays it in the text box."""
    try:
        subprocess.run(["ssh-keygen", "-t", "rsa", "-b", "4096", "-C", "your_email@example.com", "-f", os.path.expanduser("~/.ssh/id_rsa"), "-N", ""], check=True)
        messagebox.showinfo("SSH Key Generated", "SSH key generated successfully!")

        # Display SSH public key
        with open(os.path.expanduser("~/.ssh/id_rsa.pub"), "r") as f:
            ssh_key = f.read()
        ssh_key_text.delete("1.0", tk.END)
        ssh_key_text.insert(tk.END, ssh_key)

    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to generate SSH key. It might already exist.")

def copy_ssh_key():
    """Copies SSH key to clipboard."""
    ssh_key = ssh_key_text.get("1.0", tk.END).strip()
    if ssh_key:
        root.clipboard_clear()
        root.clipboard_append(ssh_key)
        messagebox.showinfo("Copied", "SSH key copied to clipboard! Paste it into GitHub settings.")
    else:
        messagebox.showwarning("No Key", "SSH key not found. Please generate the key first.")

def open_github_ssh_page():
    """Opens the GitHub SSH key settings page in the default web browser."""
    webbrowser.open("https://github.com/settings/ssh/")

# Main GUI window
root = tk.Tk()
root.title("SSH Key Setup Wizard")
root.geometry("500x400")

# Install dependencies button
btn_install_deps = tk.Button(root, text="Install Dependencies (Git, Python, Tkinter, Neofetch)", command=install_dependencies)
btn_install_deps.pack(pady=10)

# Generate SSH Key Button
btn_generate_ssh = tk.Button(root, text="Generate SSH Key", command=generate_ssh_key)
btn_generate_ssh.pack(pady=10)

# SSH Key Display
ssh_key_text = tk.Text(root, height=10, width=50)
ssh_key_text.pack(pady=10)

# Copy SSH Key Button
btn_copy_ssh = tk.Button(root, text="Copy SSH Key", command=copy_ssh_key)
btn_copy_ssh.pack(pady=10)

# Open GitHub SSH settings page button
btn_open_github = tk.Button(root, text="Open GitHub SSH Key Settings", fg="blue", cursor="hand2", command=open_github_ssh_page)
btn_open_github.pack(pady=10)

# Instructions Label
instructions = tk.Label(root, text="After copying, paste the SSH key into your GitHub SSH settings.")
instructions.pack(pady=10)

root.mainloop()
