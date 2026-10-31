# Python-practice
Python Fundamentals 
1. Variables
2. Conditional Execution
3. Functions
    - Error Handling(Try/Except)
- 4. Files
- 5. Lists
  6. Dictionaries 

### Github  cheatsheet   22/09/2026
- Incase we want to pull latest changes but we are on a diffrent branch
  - git fetch origin
  - git merge origin/main
- How to create a branch from main branch
   - git checkout main
   - git pull origin main
   - git checkout -b feature/your-branch-name
### Github  cheatsheet 14/10/2026
- In case you want to revert to a good working commit after a bad commit.
   - git log --oneline -8 (8 last working commits)
   
| Command | Purpose |
| :--- | :--- |
| `git log --oneline -10` | See recent commits and their hashes |
| `git status` | See staged, unstaged and untracked files |
| `git reset --hard <hash>` | Move branch + working tree to a previous commit |
| `git push origin main --force` | Overwrite remote history (use carefully) |
| `git rm -r --cached <folder>` | Stop tracking a folder but keep it on disk |
| `git add .gitignore` | Start tracking the ignore rules |
| `git commit -m "message"` | Create a new commit |
| `git push origin main` | Publish the commit to GitHub |


### Github Cheatsheet 31/10/2026
**- Creating a focussed Branch**
      - git switch main
      - git pull --ff-only
      - git switch -c research/56-data-architecture-recommendation
    
- **Committing to a Focussed Branch**
 - **Always specify your work , avoid using git add .**
      - git add docs/research
      - git commit -m "docs(research): add behavioral event contract for recommendation platform"
      - git push -u origin research/56-data-architecture-recommendation
 
- **Incase u had already run git add . and u want to revert to the last working state**
  -  git restore --staged
- **Incase u had unstaged Changes but still want to revert to the last working state**
  - **Step 1:** Stash; temporarily shelves your modified files and leaves you with a clean working directory
      - git stash
   - **step 2:** Pull the latest changes from github
        - git pull --rebase origin main
   - **Step 3:** Bring back your unstaged work
           - git stash pop
   - **Step 4:** Push your changes Github
      - git push origin  main

- **Incase the files in the Local folder are behind the ones in Github , and the ones in github are the most relevant**
 - **Method 1:**(clear the local files , consider the github files)
    - git reset --hard HEAD
    - git clean -fd
    - git pull origin main 
- **Method 2:** (Incase u want to merge the remote and local changes)
    - **Step 1:** stash your current VS code edits to a safe place
      - git stash -u
    - **step 2:** Pull the 3 commits you made on github:
      -  git pull origin main 
    - **step 3:** Bring your VS code edits back on top
      - git stash pop

  - **Method 3:**(Just pull the latest changes from remote)
    - git pull 