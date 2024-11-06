
__________         _________.__           .__  .__    
\______   \___.__./   _____/|  |__   ____ |  | |  |   
 |     ___<   |  |\_____  \ |  |  \_/ __ \|  | |  |   
 |    |    \___  |/        \|   Y  \  ___/|  |_|  |__ 
 |____|    / ____/_______  /|___|  /\___  >____/____/ 
           \/            \/      \/     \/            


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

To use the automated Git function in PyShell, simply work on files in your project as usual—create, edit, or remove files as needed. The Git Wizard's automated function will track these changes and handle the Git `add`, `commit`, and `push` steps for you without requiring manual input for each action. Here’s how to use it:

### Steps to Use the Automated Git Function in PyShell:

1. **Create or Edit Files**:
   - As you work within PyShell, any new files you create or edits you make will be automatically detected by the automated Git function.
   - Example commands in PyShell might look like:
     ```plaintext
     py_shell> touch new_script.py
     py_shell> echo "print('Automated Git in action!')" > new_script.py
     ```

2. **Automated Staging and Committing**:
   - Once you finish editing, the Git function will automatically stage and commit your changes.
   - By default, the commit message will reflect your latest action (e.g., "Updated `new_script.py`") or a customizable message if set.

3. **Automatic Pushing to GitHub**:
   - After committing, PyShell will push your changes to the configured remote repository (e.g., on GitHub).
   - This requires that you’ve already set up your Git remote (done during the setup process), so the shell knows where to push your updates.

4. **Optional Stash for Uncommitted Changes**:
   - If you’re not ready to commit certain changes, type `git stash` in PyShell, and the Git Wizard will automatically stash your updates so you can return to them later.
   - To retrieve stashed changes, simply type `git stash pop`.

### Example Interaction with Automated Git Function

Here’s an example session in PyShell showing how automated Git might look:

```plaintext
py_shell> touch my_script.py
# Automatically stages and commits: "Added my_script.py"
# Automatically pushes to GitHub

py_shell> echo "print('Hello from PyShell')" > my_script.py
# Automatically stages and commits: "Updated my_script.py"
# Automatically pushes to GitHub
```

### Important Notes

- **Git Remote Setup**: Make sure to complete the initial `git remote add origin <url>` command during the setup. This lets PyShell know which remote repository to push to.
- **Edit Commit Messages**: If you want to customize a message, you can enter a custom commit message prompt within PyShell.
## Troubleshooting

If you encounter any issues:
- Ensure Git and Python are installed properly by running `git --version` and `python3 --version`.
- If SSH key generation fails, confirm that `~/.ssh/id_rsa` doesn't already exist or specify a different file name.

## License

This project is open-source and available for modification to suit individual project requirements.
