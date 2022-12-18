### les alias des compmandes git ( personalisation )
git config --global alias.st status

> git st = git status

git config --global alias.co commit

> git co = git commit

### création d'un alias log formaté
git config alias.lg 'log --pretty="format:%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%ad) %Cblue(%cn)"'
exemple :
90c26b4 - (HEAD -> master, origin/master)  suppression pycache (Sat Dec 17 17:20:28 2022 +0100) (kim)
5dad16b - version initiale (Sat Dec 17 17:17:08 2022 +0100) (kim)

### liste des fichiers impactés par le commit n°id

git diff-tree --no-commit-id --name-only -r id

git config alias.show-file 'diff-tree --no-commit-id --name-only -r' 

git show-file id

## les branches et tag

## création d'une branche

git checkout -b branch_git