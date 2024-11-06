#!/usr/bin/env python3
# Import necessary libraries for the script.
import os
import subprocess
import tkinter as tk  # For creating the GUI
from tkinter import messagebox  # To show message boxes for user feedback
import webbrowser  # To open the web browser for GitHub page

def install_dependencies():
    """Install Git, Python, Tkinter, and Neofetch."""
    try:
        # Run system commands to update package list and install necessary packages.
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "git", "python3", "python3-pip", "python3-tk", "neofetch"], check=True)
        # Show a message box if installation is successful.
        messagebox.showinfo("Installation Successful", "Git, Python, Tkinter, and Neofetch installed successfully.")
    except subprocess.CalledProcessError:
        # Show an error message box if the installation fails.
        messagebox.showerror("Error", "Failed to install dependencies. Ensure you have sudo privileges and an internet connection.")

def generate_ssh_key():
    """Generates an SSH key and displays it in the text box."""
    try:
        # Run the command to generate a new SSH key, using the email provided as the comment.
        subprocess.run(["ssh-keygen", "-t", "rsa", "-b", "4096", "-C", "your_email@example.com", "-f", os.path.expanduser("~/.ssh/id_rsa"), "-N", ""], check=True)
        # Show a message box when the key is successfully generated.
        messagebox.showinfo("SSH Key Generated", "SSH key generated successfully!")

        # Read the public SSH key from the file and display it in the text box for the user to copy.
        with open(os.path.expanduser("~/.ssh/id_rsa.pub"), "r") as f:
            ssh_key = f.read()  # Read the content of the public SSH key
        # Clear any previous content in the text box and insert the newly generated SSH key.
        ssh_key_text.delete("1.0", tk.END)
        ssh_key_text.insert(tk.END, ssh_key)

    except subprocess.CalledProcessError:
        # If the SSH key generation fails (perhaps the key already exists), show an error message.
        messagebox.showerror("Error", "Failed to generate SSH key. It might already exist.")

def copy_ssh_key():
    """Copies SSH key to clipboard."""
    # Get the SSH key from the text box (after the user has generated it).
    ssh_key = ssh_key_text.get("1.0", tk.END).strip()  # Get the content from the text box
    if ssh_key:
        # Copy the SSH key to the clipboard if it exists.
        root.clipboard_clear()
        root.clipboard_append(ssh_key)
        # Show a message box confirming the key is copied.
        messagebox.showinfo("Copied", "SSH key copied to clipboard! Paste it into GitHub settings.")
    else:
        # Show a warning if there is no SSH key to copy.
        messagebox.showwarning("No Key", "SSH key not found. Please generate the key first.")

def open_github_ssh_page():
    """Opens the GitHub SSH key settings page in the default web browser."""
    url = "https://github.com/settings/ssh/new"  # URL of the GitHub SSH settings page
    webbrowser.open(url, new=2)  # Open the URL in a new browser tab (if possible)

# Main GUI window setup
root = tk.Tk()  # Create the main Tkinter window
root.title("SSH Key Setup Wizard")  # Set the window title
root.geometry("500x400")  # Set the window size (width x height)

# Button to install dependencies like Git, Python, Tkinter, and Neofetch
btn_install_deps = tk.Button(root, text="Install Dependencies (Git, Python, Tkinter, Neofetch)", command=install_dependencies)
btn_install_deps.pack(pady=10)  # Add button to the window with some vertical padding

# Button to generate the SSH key
btn_generate_ssh = tk.Button(root, text="Generate SSH Key", command=generate_ssh_key)
btn_generate_ssh.pack(pady=10)  # Add button to the window with some vertical padding

# Text box to display the generated SSH key (so the user can copy it)
ssh_key_text = tk.Text(root, height=10, width=50)  # Create a text box with 10 lines and 50 characters wide
ssh_key_text.pack(pady=10)  # Add text box to the window with some vertical padding

# Button to copy the generated SSH key to clipboard
btn_copy_ssh = tk.Button(root, text="Copy SSH Key", command=copy_ssh_key)
btn_copy_ssh.pack(pady=10)  # Add button to the window with some vertical padding

# Button to open GitHub's SSH settings page in the default browser
btn_open_github = tk.Button(root, text="Open GitHub SSH Key Settings", fg="blue", cursor="hand2", command=open_github_ssh_page)
btn_open_github.pack(pady=10)  # Add button to the window with some vertical padding

# Label with instructions to guide the user to paste the key into GitHub settings
instructions = tk.Label(root, text="After copying, paste the SSH key into your GitHub SSH settings.")
instructions.pack(pady=10)  # Add label to the window with some vertical padding

# Start the Tkinter event loop, allowing the GUI to remain responsive.
root.mainloop()
