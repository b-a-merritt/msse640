# Assignments for Git Hub Project 

# Assignments 
- [Assignment #1 (Due Week 2)](./Assignment1.md)
- [Assignment #2 (Due Week 3)](./Assignment2.md)
- [Assignment #3 (Due Week 4)](./Assignment3.md)
- [Assignment #4 (Due Week 5)](./Assignment4.md)
- [Assignment #5 (Due Week 6)](./Assignment5.md)
- [Assignment #6 (Due Week 7)](./Assignment6.md)



# General instructions
- If this is your first time working on the project, follow the instructions for working with Git and answer the essay questions. 
- If you worked on this project in a previous class, you will participate in additional exercises about the theme of AI.  You may recycle your answers from the previous class (the foundation activities).  


# References

## Basic Info

- Repo URL 
[Repo URL:  This one](https://github.com/granierregis/MSSE640-2025summer.git)

- How to find out the remote repo
```
$ git remote -v
origin  https://granierregis@github.com/granierregis/MSSE640-2025summer.git (fetch)
origin  https://granierregis@github.com/granierregis/MSSE640-2025summer.git (push)
```

## Local and global config
- If using multiple GitHub accounts, I recommend ensuring that all of your config info is local
```
$ git config --list --local
git config --list --global
```

### You should always use the local config option if you want to access multiple Git Hub accounts from the same computer

- Basic global config setup (Before first commit)
```
git config --global user.email "<email>"
git config --global user.name "<First Last>"

```
- Basic local config setup (Before first commit)

```
git config --local user.email "<email>"
git config --local user.name "<First Last>"

```

### If have trouble using multiple accounts from the same computer
- Including the correct username for the repo in the remote. 
- Credential helper will often cache one username and it will use that by default when you attempt 
to use another repo where that username is not correct. 

#### Example
```
git remote add origin https://granierregis@github.com/granierregis/MSSE640-2025summer.git
```

## Mark Down Cheat Sheets

- Markdown Guide (Web)
[Markdown Guide](https://github.com/granierregis/msse642-2025summer.git)(https://www.markdownguide.org/cheat-sheet/)

- Markdown Cheatsheet (Downloadable PDF)
[Markdown Guide](./files/markdown-cheatsheet-download.pdf)


