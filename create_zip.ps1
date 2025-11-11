# PowerShell script to create a zip of Blogify project
# Excludes node_modules, venv, __pycache__, and other build artifacts

$sourcePath = "D:\Apps\Blogify"
$zipPath = "D:\Apps\Blogify_Backup_$(Get-Date -Format 'yyyy-MM-dd_HHmmss').zip"

Write-Host "Creating zip archive of Blogify project..." -ForegroundColor Green
Write-Host "Source: $sourcePath" -ForegroundColor Cyan
Write-Host "Destination: $zipPath" -ForegroundColor Cyan

# Exclusion patterns
$excludePatterns = @(
    "node_modules",
    "venv",
    "__pycache__",
    ".git",
    "*.pyc",
    ".env",
    "package-lock.json",
    ".DS_Store",
    "Thumbs.db",
    "*.log",
    ".vscode",
    ".idea",
    "build",
    "dist",
    ".pytest_cache",
    "*.egg-info"
)

# Create temporary directory for filtered files
$tempDir = "$env:TEMP\Blogify_Temp_$(Get-Date -Format 'yyyyMMddHHmmss')"
New-Item -ItemType Directory -Path $tempDir -Force | Out-Null

Write-Host "`nCopying files (excluding build artifacts)..." -ForegroundColor Yellow

# Copy files with exclusions
$files = Get-ChildItem -Path $sourcePath -Recurse -File | Where-Object {
    $file = $_
    $shouldExclude = $false
    
    foreach ($pattern in $excludePatterns) {
        if ($file.FullName -like "*\$pattern\*" -or $file.Name -like $pattern) {
            $shouldExclude = $true
            break
        }
    }
    
    -not $shouldExclude
}

$totalFiles = $files.Count
$current = 0

foreach ($file in $files) {
    $current++
    $relativePath = $file.FullName.Substring($sourcePath.Length + 1)
    $destPath = Join-Path $tempDir $relativePath
    $destFolder = Split-Path $destPath -Parent
    
    if (-not (Test-Path $destFolder)) {
        New-Item -ItemType Directory -Path $destFolder -Force | Out-Null
    }
    
    Copy-Item $file.FullName -Destination $destPath -Force
    
    if ($current % 50 -eq 0) {
        Write-Progress -Activity "Copying files" -Status "$current of $totalFiles" -PercentComplete (($current / $totalFiles) * 100)
    }
}

Write-Progress -Activity "Copying files" -Completed

Write-Host "`nCreating zip archive..." -ForegroundColor Yellow

# Create zip file
Compress-Archive -Path "$tempDir\*" -DestinationPath $zipPath -Force

# Cleanup temp directory
Remove-Item -Path $tempDir -Recurse -Force

$zipSize = (Get-Item $zipPath).Length / 1MB

Write-Host "`n✅ Zip created successfully!" -ForegroundColor Green
Write-Host "Location: $zipPath" -ForegroundColor Cyan
Write-Host "Size: $([math]::Round($zipSize, 2)) MB" -ForegroundColor Cyan
Write-Host "`nExcluded:" -ForegroundColor Yellow
$excludePatterns | ForEach-Object { Write-Host "  - $_" -ForegroundColor Gray }

# Open folder containing the zip
Start-Process explorer.exe -ArgumentList "/select,`"$zipPath`""
