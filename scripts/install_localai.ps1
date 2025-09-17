# مسیر نصب
$InstallDir = "$env:USERPROFILE\LocalAI"

if (-Not (Test-Path $InstallDir)) {
    New-Item -ItemType Directory -Path $InstallDir | Out-Null
}

# دانلود باینری LocalAI
$LocalAIUrl = "https://github.com/go-skynet/LocalAI/releases/latest/download/localai-windows-amd64.zip"
$ZipPath = "$InstallDir\localai.zip"
Invoke-WebRequest -Uri $LocalAIUrl -OutFile $ZipPath
Expand-Archive -Path $ZipPath -DestinationPath $InstallDir -Force
Remove-Item $ZipPath

# دانلود مدل کوانت‌شده
$ModelUrl = "https://gpt4all.io/models/ggml-model-gpt4all-falcon-q4_0.bin"
$ModelPath = "$InstallDir\models"
New-Item -ItemType Directory -Path $ModelPath -Force | Out-Null
Invoke-WebRequest -Uri $ModelUrl -OutFile "$ModelPath\model.bin"

Write-Output "✅ LocalAI و مدل نصب شدند. برای اجرا: $InstallDir\localai.exe --models-path $ModelPath"
