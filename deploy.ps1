param(
    [string]$Message = "Update site"
)

# Se placer à la racine du dépôt (là où se trouve ce script)
Set-Location $PSScriptRoot

# 1) Commit du code source sur main (sans public)
git switch main

# Ajoute tout…
git add .

# …puis retire public de l’index
git restore --staged public

# S’il y a quelque chose à commit
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "$Message"
    git push origin main
} else {
    Write-Host "Rien à commit sur main"
}

# 2) Commit du worktree gh-pages (répertoire public)
Push-Location "public"

git add .

git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "Build: $Message"
    git push origin gh-pages
} else {
    Write-Host "Rien à commit sur gh-pages"
}

Pop-Location