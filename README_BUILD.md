# Luci Build & Release Guide

## نصب پیش‌نیازها
- Node.js 18+
- Python 3.9+
- PowerShell (ویندوز)

## ساخت و تست
```bash
npm install
npm run build
npx electron-builder --win
```

## اجرای RAG Pipeline
```bash
pip install -r server/requirements.txt
python server/rag_pipeline.py index --file docs/sample.pdf
python server/rag_pipeline.py query --q "نمونه پرسش"
```

## اجرای LocalAI
```powershell
.\scripts\install_localai.ps1
$env:USERPROFILE\LocalAI\localai.exe --models-path $env:USERPROFILE\LocalAI\models
```

## انتشار خودکار
- یک تگ جدید (مثلاً v1.0.0) پوش کن.
- GitHub Actions اجرا می‌شود و installer ساخته می‌شود.
