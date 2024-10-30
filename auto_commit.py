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
