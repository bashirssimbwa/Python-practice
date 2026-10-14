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
   - git status  (See 
   
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
