#!/usr/bin/env python3
import os
import subprocess
import tkinter as tk
from tkinter import messagebox
import webbrowser

def my_shell():
    """
    The main shell interface function where users can type commands.
    Provides an introduction to PyShell with options to explore features.
    """
    print("Welcome to PyShell! Type 'exit' to quit.")
    print("Use 'ask' to get help with Linux commands, concepts, or Git.")
    print("Type 'setup' to start setting up your Linux environment for software development.")
    print("type 'sshwiz' to launch the SSH Key Setup Wizard.")
    print("By typing 'setup' tkinter will automatically download to be launched!")
    while True:
        # Display prompt for user input
        user_input = input("py_shell> ")

        # Exit condition
        if user_input.lower() in ('exit', 'quit'):
            print("Thank you for using PyShell! Exiting now.")
            break

        # Launch SSH Key Setup Wizard (ssh_wizard)
        if user_input.lower() == "sshwiz":
            launch_ssh_wizard()
            continue

        # Setup function
        if user_input.lower() == "setup":
            setup_environment()
            continue

        # Ask function for guidance
        if user_input.startswith("ask"):
            question = user_input[4:].strip()
            if question:
                ask_bot(question)
            else:
                print("Usage: ask <your question or topic>")
            continue

        # chmod command
        if user_input.startswith("chmod"):
            chmod_command(user_input)
            continue

        # echo command for creating README
        if user_input.startswith("echo"):
            echo_command(user_input)
            continue

        # Split command and arguments
        args = user_input.split()
        if not args:
            continue  # If input is empty, go to next iteration

        command = args[0]
        command_args = args[1:]

        try:
            # Execute built-in shell commands, e.g., 'cd'
            if command == "cd":
                if command_args:
                    os.chdir(command_args[0])
                    print(f"Changed directory to {os.getcwd()}")
                else:
                    print("Usage: cd <directory>")
            else:
                # Run external commands
                result = subprocess.run(args, capture_output=True, text=True)
                print(result.stdout)
                if result.stderr:
                    print(result.stderr)

        except Exception as e:
            print(f"Error: {e}")

def setup_environment():
    """Guides the user through setting up their Linux environment and GitHub integration."""
    print("Welcome to the Linux Environment Setup Wizard!")
    print("Let's start by familiarizing you with basic Linux commands:")
    
    install_tkinter()

    # Step 1: Introduction to Linux Basics
    print("\nBasic Linux Commands:")
    print("- 'ls': list files and directories.")
    print("- 'cd <directory>': change to a specified directory.")
    print("- 'mkdir <directory>': create a new directory.")
    print("- 'touch <file>': create a new empty file.")
    print("- 'pwd' : print working directory.")
    print("- 'whoami' : display's the user or root user in the linux environment")
    print("- 'neofetch' : dislpays the linux environment specs and distro information")
    input("Press Enter to continue...")

    check_installation()

    # Step 2: Installing Necessary Software
    print("\nInstalling Git and Python")
    print("You may need to install Git and Python.")
    print("To install Git: sudo apt update && sudo apt install git")
    print("To install Python: sudo apt install python3 python3-pip")
    print("Use the ssh_wizard and download the dependencies using the button at the top of the GUI")
    input("Press Enter after installation...")



    # Step 3: Setting up SSH Keys for GitHub
    print("\nSetting Up SSH Keys for GitHub")
    print("To push your work to GitHub, set up SSH keys.")
    print("Command: ssh-keygen -t rsa -b 4096 -C \"your_email@example.com\"")
    print("Use the ssh_wizard and create and or generate your new ssh-key in the GUI!")
    input("Press Enter and we will create your SSH key in the git_wizard!!...")

    launch_ssh_wizard()
    # open_github_ssh_page()

    print("Copy your SSH key using 'cat ~/.ssh/id_rsa.pub' and add it to GitHub settings.")
    print("You can also use the GUI and copy the ssh-key from the GUI window and paste your key into the box in your github settings ")
    
    input("Press Enter after adding your SSH key to GitHub...")

    # Step 4: Project Initialization
    print("\nCreating Your Project Directory")
    project_name = input("Enter your project name: ").strip()
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)
    print(f"Changed to project directory: {os.getcwd()}")

    script_name = input("Enter the name of your script (e.g., hello.py): ")
    with open(script_name, 'w') as f:
        f.write("#!/usr/bin/env python3\nprint('Hello, World!')")
    print(f"Created script: {script_name}")

    # Step 5: Initialize Git and Push to GitHub
    print("\nInitializing Git and Pushing to GitHub")
    print("Commands to initialize and push to GitHub:")
    print("git init, git add ., git commit, git remote add origin, git push")
    input("Press Enter after completing Git setup.")

    print("Your Linux environment is ready for development.")

def check_installation():
    """Checks if Python and Git are installed."""
    try:
        python_version = subprocess.run(["python3", "--version"], capture_output=True, text=True)
        git_version = subprocess.run(["git", "--version"], capture_output=True, text=True)

        if python_version.returncode == 0:
            print(f"Python is installed: {python_version.stdout.strip()}")
        else:
            print("Python is not installed. Please install Python.")

        if git_version.returncode == 0:
            print(f"Git is installed: {git_version.stdout.strip()}")
        else:
            print("Git is not installed. Please install Git.")

    except Exception as e:
        print(f"Error checking installations: {e}")


def chmod_wizard(filename):
    """Sets file permission using 'chmod u+x' and explains different permission settings."""
    try:
        # Grant execute permissions to the user for the file
        subprocess.run(["chmod", "u+x", filename], check=True)
        print(f"Execute permission granted to user for '{filename}'.")

        # Explain permissions in octal notation
        print("\nUnderstanding Linux File Permissions:")
        print("Permission format: Owner (User) | Group | Others")
        print("Each permission has three numbers, e.g., 755.")
        print(" - 7: Read, write, execute (4 + 2 + 1)")
        print(" - 5: Read, execute (4 + 1)")
        print(" - 4: Read only")
        print(" - 0: No permissions")
        print("For example, 755 gives: User full access (7), Group read and execute (5), Others read and execute (5).")

    except subprocess.CalledProcessError:
        print(f"Failed to change permissions for '{filename}'. Ensure the file exists.")

def ask_bot(question):
    """Provides tips based on user questions with explanations for specific Linux commands."""
    question = question.lower()
    if "linux" in question or "command" in question:
        print("Basic Linux commands include: 'ls', 'cd', 'mkdir', 'rm', 'pwd', 'cp', 'mv', 'man'")
    elif "ssh" in question:
        print("To create an SSH key, use 'ssh-keygen -t rsa -b 4096 -C \"your_email@example.com\"'.")
    elif "git" in question:
        git_wizard()
    elif "command":
        print("Ask about Linux commands, Git, or programming concepts.")

    # Common command responses with explanations
    elif "ls" in question:
        print("Command 'ls': Lists files and directories in the current directory.")
    elif "cd" in question:
        print("Command 'cd <directory>': Changes to the specified directory.")
    elif "pwd" in question:
        print("Command 'pwd': Prints the current working directory.")
    elif "whoami" in question:
        print("Command 'whoami': Displays the current logged-in user.")
    elif "neofetch" in question:
        print("Command 'neofetch': Shows Linux environment specs and distro information.")
    elif "chmod" in question:
        chmod_wizard()
    elif "ssh" in question:
        print("To create an SSH key, use 'ssh-keygen -t rsa -b 4096 -C \"your_email@example.com\"'.")
    elif "git" in question:
        git_wizard()
    elif "recursion" in question:
        print("Recursion is a function calling itself. Head recursion: the call is the first action.")
    elif "grep" in question:
        print("Grep is used to search patterns in files. Example: grep 'pattern' filename.txt")
    else:
        print("Ask about Linux commands, Git, or programming concepts.")



def chmod_command(user_input):
    """Changes file permissions based on user input."""
    args = user_input.split()
    if len(args) != 3:
        print("Usage: chmod <permissions> <filename>")
        return

    permissions, filename = args[1], args[2]
    try:
        subprocess.run(["chmod", permissions, filename], check=True)
        print(f"Changed permissions of '{filename}' to '{permissions}'.")
    except subprocess.CalledProcessError:
        print(f"Failed to change permissions for '{filename}'.")

def install_tkinter():
    """Installs Tkinter if it is not already available."""
    try:
        #check if Tkinter is installed by attmepting to import it
        import tkinter
        print("Tkinter is already installed.")
    except ImportError:
        print("Tkinter not found. Installing Tkinter...")
        try:
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "python3-tk"], check=True)
            print("Tkinter installed successfully.")
        except subprocess.CalledProcessError:
            print("Error: Could not install Tkinter. Please install it manually.")


def echo_command(user_input):
    """Creates a README file based on user input."""
    args = user_input.split(maxsplit=1)
    if len(args) < 2:
        print("Usage: echo <text> > README.md")
        return

    text = args[1]
    with open("README.md", "w") as readme:
        readme.write(text)
    print("Created README.md with content:")
    print(text)

    
def launch_ssh_wizard():
    """Launches the SSH Key Setup Wizard."""
    try:
        subprocess.run(["python3", "wizard.py"], check=True)
    except Exception as e:
        print(f"Failed to launch SSH Key Setup Wizard: {e}")

def git_wizard():
    """Provides a guide for basic Git commands."""
    print("Basic Git commands:")
    print("- 'git init': Initialize a new Git repository.")
    print("- 'git add <file>': Add changes to the staging area.")
    print("- 'git commit -m \"message\"': Commit with a message.")
    print("- 'git push': Push changes to the repository.")
    print("- 'git pull': Pull the latest changes.")
    print("- 'git clone <url>': Clone a repository.")

if __name__ == "__main__":
    my_shell()
