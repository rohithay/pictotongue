# pictotongue
PictoTongue is a powerful image-to-text conversion tool that breaks down language barriers by allowing you to extract and translate text from any image. Whether you're analyzing screenshots, processing scanned documents, or making foreign news articles accessible, PictoTongue handles it with precision and ease.

## Features

- Optical Character Recognition - Extract text from images, screenshots, and scanned documents
- Multilingual Support - Process text in 50+ languages
- Smart Translation - Convert extracted text to your preferred language
- Batch Processing - Handle multiple images simultaneously
- Format Preservation - Maintain text layout and structure when possible
- Web Integration - Simple API for developers to integrate into their projects
- Privacy-Focused - Process images locally with optional cloud backups
  
<img width="1219" alt="Screenshot 2025-05-17 at 6 59 53 PM" src="https://github.com/user-attachments/assets/e6c12573-9481-4ce8-bfd6-7f3ee209b8ce" />


## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
cd scripts
python translator.py --lang <language-code>
```
