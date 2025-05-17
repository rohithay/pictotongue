# Newspaper Translator - Usage Guide

This tool automatically extracts text from newspaper images and translates it to your target language. The script processes all images in an input folder and outputs both the original and translated text to an output folder.

## Prerequisites

Before using the script, you need to install the following:

1. **Python 3.7+**: Download from [python.org](https://www.python.org/downloads/)

2. **Tesseract OCR**: 
   - **Windows**: Download installer from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt install tesseract-ocr`

3. **Required Python Libraries**:
   ```bash
   pip install pillow pytesseract googletrans==4.0.0rc1
   ```

## Setup

1. Create two folders:
   - `input` - Place newspaper images here
   - `output` - Translated files will be saved here

2. Download the script (`newspaper_translator.py`) to the same directory as the input and output folders.

## Usage

### Basic Usage

Run the script with default settings:

```bash
python newspaper_translator.py
```

This will:
- Process all images in the `input` folder
- Translate extracted text to Spanish (default)
- Save results in the `output` folder

### Advanced Usage

Customize the behavior with command-line arguments:

```bash
python newspaper_translator.py --input custom_input --output custom_output --lang fr
```

Available arguments:
- `--input`: Specify input folder (default: "input")
- `--output`: Specify output folder (default: "output")
- `--lang`: Specify target language code (default: "es" for Spanish)

### Language Codes

Common language codes:
- `es`: Spanish
- `fr`: French
- `de`: German
- `it`: Italian
- `pt`: Portuguese
- `ru`: Russian
- `ja`: Japanese
- `ko`: Korean
- `zh-cn`: Chinese (Simplified)
- `hi`: Hindi
- `ar`: Arabic

## Output

For each image processed, the script generates two files in the output folder:
- `[image_name]_original.txt`: The extracted text from the image
- `[image_name]_translated.txt`: The translated text

## Tips for Better Results

1. **Image Quality**:
   - Use clear, well-lit images
   - Ensure text is in focus and not blurry
   - Avoid wrinkled or damaged newspaper pages

2. **Cropping**:
   - Crop images to include only the text you want to extract
   - Remove unnecessary graphics or images

3. **Language Support**:
   - For non-Latin scripts (e.g., Arabic, Chinese), install the appropriate Tesseract language packages

## Troubleshooting

1. **No text extracted**:
   - Check image quality
   - Ensure Tesseract is properly installed
   - Try installing additional language packs for Tesseract

2. **Translation errors**:
   - Check internet connection
   - If receiving rate limit errors, increase the sleep time in the script

3. **File not found errors**:
   - Ensure input and output folders exist
   - Check file permissions

## Logs

A log file (`newspaper_translator.log`) is created in the same directory as the script. This log contains detailed information about each processing step and any errors encountered.

## Example

1. Place newspaper images in the `input` folder:
   - `news1.jpg`
   - `article2.png`

2. Run the script:
   ```bash
   python translator.py --lang fr
   ```

3. Check the `output` folder for results:
   - `news1_original.txt` - Contains the extracted English text
   - `news1_translated.txt` - Contains the French translation
   - `article2_original.txt` - Contains the extracted English text
   - `article2_translated.txt` - Contains the French translation
