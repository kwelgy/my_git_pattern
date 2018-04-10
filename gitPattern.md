# my_git_pattern

## Usual Pattern

#### local central repo:
 * `git init --bare` "initialize bare directory"

#### local repo:
 * `git init`
 * `git add .` (or -u)
 * `git commit -m "Initial commit"`
 * `git remote add origin <path-to-central>`
 * `git push origin master`

#### working repo:
 * `git clone <central repo>`
 * `git checkout -b <branch>`
 * (anytime after) `git push -u origin <branch>`
 * code(contextual)
 * `git add <files>`
 * `git commit -m <message>`

#### merging branch:
 * `git checkout master`
 * `git merge <branch>`
 * `git branch -d <branch>`
 * `git push origin master`

#### delete local uncommited changes
 * `git reset --hard <sha>`
 * <https://stackoverflow.com/questions/4114095/how-to-revert-git-repository-to-a-previous-commit>

#### show remote
 * `git remote show origin`
 * `git remote -v`

#### change remote origin`
 * `git remote set-url <name(origin)> <url>`

#### change git commit message
 * `git commit --amend`

#### .gitignore
 * ignore folder <<ex: git/>>
 * ignore filetype <<ex: .git>>

#### import subtree
 * `git remote add <name_remote> <path-or-url-to-XXX-repo>`
 * `git fetch <name_remote>`
 * `git merge -s ours --no-commit <name_remote/master>`
 * `git read-tree --prefix=ZZZ/ -u <name_remote/master>`
 * `git commit -m "Imported XXX as a subtree."`

#### remove from git but local
 * `git rm --cached <file1.txt>`
 * `git commit -m <"remove file1.txt">`
 * can use `git rm` to delete local and from r

#### track remote branch
 * `git branch -a`
 * `git branch -t <branch_name> <remote_branch>`
 * `git checkout <branch_name>`
 * OR
 * `git checkout -t <remote_branch>`

#### See graphical log
 * `gitk`

# Merge repos and preserve history <https://saintgimp.org/2013/01/22/merging-two-git-repositories-into-one-repository-without-losing-file-history/>
###### Assume the current directory is where we want the new repository to be created
###### Create the new repository
git init

#### Before we do a merge, we have to have an initial commit, so we’ll make a dummy commit
dir > deleteme.txt
git add .

#### Add a remote for and fetch the old repo
git remote add -f old_a <OldA repo URL>

#### Merge the files from old_a/master into new/master
git merge old_a/master

#### Clean up our dummy file because we don’t need it any more
git rm .\deleteme.txt
git commit -m “Clean up initial file”

#### Move the old_a repo files and folders into a subdirectory so they don’t collide with the other repo coming later
mkdir old_a
dir –exclude old_a | %{git mv $_.Name old_a}

#### Commit the move
git commit -m “Move old_a files into subdir”

#### Do the same thing for old_b
git remote add -f old_b <OldB repo URL>
git merge old_b/master
mkdir old_b
dir –exclude old_a,old_b | %{git mv $_.Name old_b}
git commit -m “Move old_b files into subdir”
