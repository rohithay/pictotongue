# Newspaper Translator App

This is a complete implementation of a newspaper translator app that allows users to:
1. Take a photo of a newspaper article
2. Extract text using OCR
3. Translate the text to a native language
4. Display the translated content

## Project Structure

```
newspaper_translator/
│
├── app/
│   ├── __init__.py
│   ├── main.py            # Main application file
│   ├── ocr_engine.py      # OCR functionality
│   ├── translator.py      # Translation functionality
│   └── ui/
│       ├── __init__.py
│       ├── main_screen.py # Main UI screen
│       └── styles.py      # UI styles
│
├── requirements.txt       # Dependencies
└── README.md             # Project documentation
```

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
python -m app.main
```

## Dependencies (requirements.txt)

```
Pillow==9.5.0
pytesseract==0.3.10
googletrans==4.0.0rc1
kivy==2.1.0
kivymd==1.1.1
```

Additionally, you'll need to install Tesseract OCR on your system:
- Windows: Download the installer from https://github.com/UB-Mannheim/tesseract/wiki
- macOS: `brew install tesseract`
- Linux: `sudo apt install tesseract-ocr`
