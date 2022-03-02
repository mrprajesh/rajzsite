Title: Git and Github 
Date: 16-Sep-2018 12:20:58
Category: Learning Curve
Modified: 16.09.2019 13:32:02 

Git is a cool versioning manager and Github is awesome. You could
manage large open/close software projects. 

# To install

```
sudo apt-get install git
```

## Git - commands to know

- `git clone <URL>` - Clone the **repo**sitory `<URL>` may be github url.
- `git add <File/FOLDER>` - Monitors the `file/FOLDER` for changes
- `git commit -m "<MESSAGE>"` - give a meaningful name to your commit.
- `git commit -m "<MESSAGE>" -a ` - commits all tracked changes.
- `git push origin master` - Push the last commit to the remote server

These are handy quick cmds.

- `git log` - Check the commits history
- `git status` - Files monitored by git
- `git pull` - Pull and updates local repo from server

## One time setup 
As all the commits are logged with the username and email. It is a must
to setup this. used `global` as I wanted the same setup for all my repos.

```
git config --global user.name "YOUR FULL NAME"
git config --global user.email "YOUR-EMAIl-ID@gmail.com"
```
