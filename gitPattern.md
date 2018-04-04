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
