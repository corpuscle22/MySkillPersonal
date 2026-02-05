param (
    [string]$RemoteName = "origin",
    [string]$Branch = "main"
)

Write-Host "Syncing skills to GitHub..." -ForegroundColor Cyan

# Check if git is initialized
if (!(Test-Path ".git")) {
    Write-Error "Not a git repository. Please run 'git init' first."
    exit 1
}

# Add all changes in the skills directory
git add .agent/skills/

# Check if there are changes to commit
$status = git status --porcelain .agent/skills/
if ([string]::IsNullOrWhiteSpace($status)) {
    Write-Host "No changes detected in .agent/skills." -ForegroundColor Yellow
    exit 0
}

# Commit changes
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "Auto-sync skills: $timestamp"

# Push to remote
Write-Host "Pushing to $RemoteName $Branch..."
git push $RemoteName $Branch

if ($LASTEXITCODE -eq 0) {
    Write-Host "Successfully synced skills to GitHub!" -ForegroundColor Green
} else {
    Write-Error "Failed to push to GitHub. Please check your remote configuration."
}
