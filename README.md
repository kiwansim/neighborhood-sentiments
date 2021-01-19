# Neighborhood Sentiments Project

# Getting Started

## Flask set up on Windows
[Documentation](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

1. Install pip 
Run `py -m pip --version` to access pip
If you need to update pip to the latest version, run `py -m pip install --upgrade pip`

2. Install virtual environment
```
py -m pip install --user virtualenv
py -m venv env  
```
This creates a virtual Python installation in the env folder

3. Activate environment
```
.\env\Scripts\activate
```
Check that you are in the virtual env by checking where your Python is located. Run `where python` and it should yield something like `.../env/bin/python.exe`

4. Install flask
```
py -m pip install Flask==1.1.1
```

5. Install requirements
```
py -m pip install -r requirements.txt
```

6. Run the app
```
$ python app.py
```
Your app will show up here: http://localhost:5000/
Make sure to kill the server when you're done (ctrl + c in terminal)

## Git help

### Frequently used
- `git status`
gives the status of any modified files, untracked files, changes to be committed.
always run this before pulling/pushing!
- `git add .` or `git add [insert file path here, no brackets]`
the . adds all modified or untracked files to the “stage.”
staged files are the ones that show up as green when you type git status.
- `git commit -m "insert commit message here in quotes"`
this “saves” all of your staged files under one commit! consider committing as a checkpoint that you can go back to any time you need to revert to an older version of your directory.
- `git push`
pushes your local commits to the remote branch of the same name
- `git pull origin [branch name here, no brackets]`
pulls latest changes from remote branch. note that you may run into merge conflicts if your local files and remote files conflict.

### Branch related commands
- `git branch`
checks what branch you are currently on your local machine. Only branches you have worked on locally will be listed
- `git checkout -b [branch name here]`
creates new branch on your local machine based on the current branch you write this command on
- `git fetch`
gets all remote branches in Github and fetches it so your local machine can access those branches.
ex) useful when team member pushes a new branch you want to take a look at, edit, etc.

### Merge conflict
1. Go to your VS code and click on the tab on the left hand side called “Source Control”
2. Manually accept/reject incoming changes from files that were flagged with a yellow “M” as in “Modified”
3. Don’t forget to save those modified files!
4. In your terminal, type `git add .`
5. Go back to your VS code. Now at the top of the left hand tab with file names, you should be able to click the small check box above the merge message.
6. If that works, your merge is successful! Type `git status` in your terminal to check that the status is “nothing to commit, working tree clean.” OR type `git log` to see the merged commit message.

 ## Contributors
- Ki Wan Sim
- Yuchan Yang
- Andrew Suh
