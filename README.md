### Step 1: Create a README.md File
1. In your project folder, create a new file named `README.md`.
2. Open the file in a text editor and paste the instructions you’ve written:

   ```markdown
   # How to Run the Automation Script

   I'll walk you through the steps to run this code. This will assume you have a Git repository set up and some basic tools installed on your computer.

   ### Prerequisites
   1. **Git**: Make sure you have Git installed. You can download it from [git-scm.com](https://git-scm.com/).
   2. **Python**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

   ### Step 1: Set Up a Git Repository
   1. Open a terminal or command prompt.
   2. Navigate to the folder where you want to create the project.
   3. Run the following commands to initialize a Git repository:
      ```bash
      git init
      ```

   ### Step 2: Create the Python Script
   1. Open a text editor (like Notepad, VS Code, or any text editor).
   2. Copy the revised code below and paste it into the text editor:
      ```python
      import os
      from random import randint

      for i in range(1, 365):
          for j in range(randint(1, 10)):
              d = str(i) + ' days ago'
              # Write unique content to file to ensure changes are made
              with open('file.txt', 'a') as file:
                  file.write(f"Commit made {d}\n")
              
              # Stage and commit with a unique message
              os.system('git add .')
              os.system(f'git commit --date="{d}" -m "Commit on {d}"')

      # Push all changes to the remote repository
      os.system('git push -u origin main')
      ```

   3. Save this file with a `.py` extension (e.g., `auto_commit.py`) in the same folder as your Git repository.

   ### Step 3: Set Up GitHub (or Another Git Host)
   1. Create a repository on GitHub (or any other Git platform).
   2. Copy the repository's URL (it will look like `https://github.com/username/repo.git`).
   3. In your terminal, link your local Git repository to this remote repository by running:
      ```bash
      git remote add origin <repository_url>
      ```
      Replace `<repository_url>` with the URL you copied.

   ### Step 4: Run the Script
   1. In your terminal, navigate to the folder where `auto_commit.py` is saved.
   2. Run the script by typing:
      ```bash
      python auto_commit.py
      ```
      This will generate random commits in the past year and push them to your GitHub repository.

   ### Notes
   - The script may take a few minutes to run because it makes multiple commits.
   - Check your GitHub repository to confirm the commits have been pushed.
