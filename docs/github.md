# How to use GitHub to share your contributions

## Step 1: Create a GitHub account
If you already have one go to next step. 
Otherwise, go to https://github.com/ and create a new account.

## Step 2: Fork the project
After you've made login, go to https://github.com/ConoscereLinux/django-conoscerelinux
On the top-left part of the repository, click on `Fork`, this will create a connected 
copy of the principal repository inside your account

## Step 3: clone the fork
Go to your repositories, find the fork you just create and click on the green button 
`Code <>` and use one of the three option to clone the repository (personally I suggest 
using SSH, but you'll need to create an RSA key)

Then use your editor (like VisualStudio Code, Pycharm, Vim, ...) of choose to handle 
the repository in your environment

For more info: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

## Step 4: (optional) create a new branch
Inside your fork you will find a `develop` branch which is at the same commit as the 
`develop` branch in main repository.

To simplify the pull request phase and mantain more control in case of uptades in 
main repository, I suggest you to create a new branch starting from develop, calling 
something like `features/<what you're wonking on>` (for example `features/templates` 
if you're working on templates).

From the shell you can do it with 
```shell
# Create a new local branch called `features/example`
$ git branch 'features/example'
# Enter your new local branch
$ git checkout 'features/example'
# Connect and send your new local branch to your fork
$ git push
```

## Step 5: make some changes
The title is self explainatory

## Step 6: Create Pull Request
After you're satisfied with the changes to back to GitHub.
- Go to the main repo or inside your fork and go to `Pull Requests`
- Select on the left the `develop` branch in main repository (`ConoscereLinux/django-conoscerelinux`)
- Select on the right your branch `features/...`
- Create pull request
- Add some info about what you've changed 
- Wait for an admin to approve yoou're changes

> NOTE: if your branch don't appear click on `compare across forks` this usually happen 
> when you made changes in your fork `develop` branch