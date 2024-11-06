#!/usr/bin/env python3
import os
import subprocess

def my_shell():
    """
    The main shell interface function where users can type commands.
    Provides an introduction to PyShell with options to explore features.
    """
    print("Welcome to PyShell! Type 'exit' to quit.")
    print("Use 'ask' to get help with Linux commands, concepts, or Git.")
    print("Type 'setup' to start setting up your Linux environment for software development.")

    while True:
        # Display prompt for user input
        user_input = input("py_shell> ")

        # Exit condition
        if user_input.lower() in ('exit', 'quit'):
            print("Thank you for using PyShell! Exiting now.")
            break

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

    # Step 1: Introduction to Linux Basics
    print("\nBasic Linux Commands:")
    print("- 'ls': list files and directories.")
    print("- 'cd <directory>': change to a specified directory.")
    print("- 'mkdir <directory>': create a new directory.")
    print("- 'touch <file>': create a new empty file.")
    input("Press Enter to continue...")

    # Step 2: Installing Necessary Software
    print("\nInstalling Git and Python")
    print("You may need to install Git and Python.")
    print("To install Git: sudo apt update && sudo apt install git")
    print("To install Python: sudo apt install python3 python3-pip")
    input("Press Enter after installation...")

    # Step 3: Setting up SSH Keys for GitHub
    print("\nSetting Up SSH Keys for GitHub")
    print("To push your work to GitHub, set up SSH keys.")
    print("Command: ssh-keygen -t rsa -b 4096 -C \"your_email@example.com\"")
    input("Press Enter after generating your SSH key...")

    print("Copy your SSH key using 'cat ~/.ssh/id_rsa.pub' and add it to GitHub settings.")
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

def ask_bot(question):
    """Provides tips based on user questions."""
    question = question.lower()
    
    # Common command responses
    if "linux" in question or "command" in question:
        print("Basic Linux commands include: 'ls', 'cd', 'mkdir', 'rm', 'pwd', 'cp', 'mv', 'man'")
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

