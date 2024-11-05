#!/usr/bin/env python3
import os
import subprocess

def my_shell():
    
    print("Welcome to PyShell! Type 'exit' to quit.")
    print("Use 'ask' to get help with Linux commands, concepts, or Git.")
    print("Type 'setup' to start setting up your Linux environment for software development.")

    while True:
        # Display prompt
        user_input = input("py_shell> ")

        # Exit condition
        if user_input.lower() in ('exit', 'quit'):
            print("Thank you for using PyShell! Exiting now.")
            break

        # Check for setup function
        if user_input.lower() == "setup":
            setup_environment()
            continue

        # Check for ask function
        if user_input.startswith("ask"):
            question = user_input[4:].strip()
            if question:
                ask_bot(question)
            else:
                print("Usage: ask <your question or topic>")
            continue

        # Check for chmod command
        if user_input.startswith("chmod"):
            chmod_command(user_input)
            continue

        # Check for echo command
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

    # Step 1: Introduction to Linux Basics
    print("\nStep 1: Linux Basics")
    print("Before we begin, let's familiarize you with some basic Linux commands:")
    print("- 'ls': list files and directories.")
    print("- 'cd <directory>': change to a specified directory.")
    print("- 'mkdir <directory>': create a new directory.")
    print("- 'touch <file>': create a new empty file.")
    print("- 'vim <file>': open the file in the Nano text editor.")
    input("Press Enter to continue...")

    # Step 2: Installing Necessary Software
    print("\nStep 2: Installing Necessary Software")
    print("You will need to install Git and Python.")
    print("To install Git, run the following command:")
    print("sudo apt update && sudo apt install git")
    input("Press Enter after you have installed Git...")

    print("To install Python, run the following command:")
    print("sudo apt install python3 python3-pip")
    input("Press Enter after you have installed Python...")

    # Step 3: Setting up SSH Keys
    print("\nStep 3: Setting Up SSH Keys for GitHub")
    print("To push your work to GitHub, you need to set up SSH keys.")
    print("Run the following command to generate a new SSH key:")
    print("ssh-keygen -t rsa -b 4096 -C \"your_email@example.com\"")
    print("Follow the prompts and press Enter to save the key.")
    input("Press Enter after generating your SSH key...")

    print("Next, copy your SSH key to your clipboard using:")
    print("cat ~/.ssh/id_rsa.pub")
    print("Then, go to your GitHub settings and add the SSH key.")
    input("Press Enter after adding your SSH key to GitHub...")

    # Step 4: Project Initialization
    print("\nStep 4: Create Your First Project Directory")
    while True:
        project_name = input("Enter your project name: ").strip()
        if project_name:
            break
        else:
            print("Project name cannot be empty. Please enter a valid project name.")

    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)
    print(f"Changed to project directory: {os.getcwd()}")

    print("Now, let's create your first Python script.")
    script_name = input("Enter the name of your script (e.g., hello.py): ")
    with open(script_name, 'w') as f:
        f.write("#!/usr/bin/env python3\nprint('Hello, World!')")
    print(f"Created script: {script_name}")
    print(f"Make it executable with: chmod +x {script_name}")

    # Step 5: Initialize Git and Push to GitHub
    print("\nStep 5: Initialize Git and Push Your Project to GitHub")
    print("Run the following commands to set up Git:")
    print("git init")
    print("git add .")
    commit_message = input("Enter a commit message for your first commit: ")
    print(f"git commit -m \"{commit_message}\"")
    print("Now link your local repository to GitHub:")
    repo_url = input("Enter your GitHub repository URL (e.g., git@github.com:username/repo.git): ")
    print(f"git remote add origin {repo_url}")
    print("Finally, push your changes to GitHub:")
    print("git push -u origin main")

    print("\nCongratulations! You have set up your Linux environment and pushed your first project to GitHub.")
    print("Feel free to explore more and build your projects!")


def chmod_command(user_input):
    """Changes file permissions based on user input."""
    args = user_input.split()
    if len(args) != 3:
        print("Usage: chmod <permissions> <filename>")
        return

    permissions, filename = args[1], args[2]

    try:
        # Change the permissions of the file
        subprocess.run(["chmod", permissions, filename], check=True)
        print(f"Changed permissions of '{filename}' to '{permissions}'.")
        print("You can now run this file as an executable.")
    except subprocess.CalledProcessError:
        print(f"Failed to change permissions for '{filename}'. Ensure the file exists.")

def echo_command(user_input):
    """Creates a README file based on user input."""
    args = user_input.split(maxsplit=1)
    if len(args) < 2:
        print("Usage: echo <text> > README.md")
        return

    text = args[1]
    with open("README.md", "w") as readme:
        readme.write(text)
    print("Created README.md with the following content:")
    print(text)

def ask_bot(question):
    """Provides tips and advice based on user questions."""
    question = question.lower()
    
    # Linux Commands
    if "linux" in question or "command" in question:
        print("To navigate in Linux, try commands like:")
        print("- 'ls': list files and directories.")
        print("- 'cd <directory>': change to the specified directory.")
        print("- 'mkdir <directory>': create a new directory.")
        print("- 'rm <file>': remove a file.")
        print("- 'pwd': print the current working directory.")
        print("- 'cp <source> <destination>': copy files.")
        print("- 'mv <source> <destination>': move or rename files.")
        print("- 'man <command>': view the manual for a command.")

    # SSH Key Creation
    elif "ssh" in question:
        print("To create an SSH key:")
        print("1. Run 'ssh-keygen -t rsa -b 4096 -C \"your_email@example.com\"'.")
        print("2. Follow the prompts to save the key.")
        print("3. Use 'cat ~/.ssh/id_rsa.pub' to display and copy your public key.")
        print("4. Go to your GitHub settings at https://github.com/settings/keys.")
        print("5. Paste the SSH key you copied from your id_rsa.pub file into a new SSH key on GitHub and save.")
        print("6. This allows you to use SSH instead of a token for smoother GitHub workflow.")

    # Git Commands
    elif "git" in question:
        git_wizard()

    # Recursion
    elif "recursion" in question:
        print("Recursion is a function that calls itself, typically with modified parameters, until it reaches a base case.")
        print("There are two types of recursion:")
        print("- Head Recursion: The recursive call is the first action in the function.")
        print("Example:")
        print("def head_recursive(n):")
        print("\tif n > 0:")
        print("\t\thead_recursive(n - 1)")
        print("\t\tprint(n)")

        print("- Tail Recursion: The recursive call is the last action in the function.")
        print("Example:")
        print("def tail_recursive(n, acc=0):")
        print("\tif n == 0:")
        print("\t\treturn acc")
        print("\treturn tail_recursive(n - 1, acc + n)")

    # Grep and Shell Scripts
    elif "grep" in question:
        print("The 'grep' command searches for patterns in files. It is commonly used in shell scripts.")
        print("Example usage: grep 'pattern' filename.txt")
    
    else:
        print("I'm not sure how to help with that. Try asking about Linux commands, Git, or programming concepts.")

def git_wizard():
    """Provides a guide for basic Git commands."""
    print("Here are some essential Git commands:")
    print("- 'git init': Initialize a new Git repository.")
    print("- 'git add <file>': Add changes to the staging area.")
    print("- 'git commit -m \"message\"': Commit your changes with a message.")
    print("- 'git push': Push your changes to the remote repository.")
    print("- 'git pull': Pull the latest changes from the remote repository.")
    print("- 'git clone <url>': Clone a repository from a given URL.")

if __name__ == "__main__":
    my_shell()
