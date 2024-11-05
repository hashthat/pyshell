#                                                                
#                                  88                     88 88  
#                                  88                     88 88  
#                                  88                     88 88  
#8b,dPPYba,  8b       d8 ,adPPYba, 88,dPPYba,   ,adPPYba, 88 88  
#88P'    "8a `8b     d8' I8[    "" 88P'    "8a a8P_____88 88 88  
#88       d8  `8b   d8'   `"Y8ba,  88       88 8PP""""""" 88 88  
#88b,   ,a8"   `8b,d8'   aa    ]8I 88       88 "8b,   ,aa 88 88  
#88`YbbdP"'      Y88'    `"YbbdP"' 88       88  `"Ybbd8"' 88 88  
#88              d8'                                             
#88             d8'

---

# PyShell

PyShell is a custom shell environment built in Python, designed to assist users in setting up a Linux development environment, learning Linux commands, and managing Git repositories. It includes commands for basic shell operations, a setup wizard for GitHub integration, and an "ask" function to provide helpful tips on Linux, Git, and programming concepts.

## Features

- **Basic Shell Functionality**: Run typical Linux commands, including `cd`, `ls`, `chmod`, and `echo`.
- **Setup Wizard**: Walks users through setting up essential tools for development, including Git, Python, SSH keys, and GitHub integration.
- **Git Wizard**: Provides guidance on basic Git commands like `git init`, `git add`, `git commit`, and `git push`.
- **Interactive Assistance**: Use the `ask` command to get helpful information about common Linux commands, SSH keys, Git, and programming concepts such as recursion.

## Getting Started

### Requirements

- Python 3.x
- Linux environment (e.g., Ubuntu)
- Optional: Git, if intending to use version control features

### Usage

1. **Launching PyShell**: Run the script from the terminal:
    ```bash
    python3 pyshell.py
    ```

2. **Basic Commands**: Use standard commands like `cd`, `chmod`, and `echo` to navigate and manage files within the PyShell environment.

3. **Setup Wizard**: 
   - Type `setup` to start the environment setup wizard. This guide will walk you through:
     - **Linux basics**: Commands like `ls`, `mkdir`, and `vim`.
     - **Software Installation**: Instructions for installing Git and Python.
     - **SSH Key Setup**: Steps to generate and add an SSH key to GitHub.
     - **Project Setup**: Instructions for initializing a new project, creating a Python script, and setting up Git.

4. **Ask for Help**: 
   - Type `ask <topic>` to get guidance on topics like Linux commands, SSH, Git, or recursion. Example:
     ```bash
     ask git
     ```

5. **Git Commands**:
   - For specific Git actions, use the `git_wizard` to learn essential commands like `git init`, `git add`, and `git commit`.

### Example

Here's a simple interaction in PyShell:
```plaintext
py_shell> setup
  # Walks through setting up Git, SSH, and a project
py_shell> ask linux
  # Provides a list of common Linux commands
py_shell> ask git
  # Offers guidance on Git commands and usage
py_shell> echo "My Project" > README.md
  # Creates a README file for your project
py_shell> chmod +x hello.py
  # Makes hello.py executable
```

## Troubleshooting

If you encounter any issues:
- Ensure Git and Python are installed properly by running `git --version` and `python3 --version`.
- If SSH key generation fails, confirm that `~/.ssh/id_rsa` doesn't already exist or specify a different file name.

## License

This project is open-source and available for modification to suit individual project requirements.
