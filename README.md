# Picto Tongue
PictoTongue is a powerful image-to-text conversion tool that breaks down language barriers by allowing you to extract and translate text from any image. Whether you're analyzing screenshots, processing scanned documents, or making foreign news articles accessible, PictoTongue handles it with precision and ease.

This is a complete implementation of a translator that allows users to:
1. Take a photo of a newspaper article
2. Extract text using OCR
3. Translate the text to a native language
4. Display the translated content

## 🌟 Features

- Optical Character Recognition - Extract text from images, screenshots, and scanned documents
- Multilingual Support - Process text in 50+ languages
- Smart Translation - Convert extracted text to your preferred language
- Batch Processing - Handle multiple images simultaneously
- Format Preservation - Maintain text layout and structure when possible
- Web Integration - Simple API for developers to integrate into their projects
- Privacy-Focused - Process images locally with optional cloud backups

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
