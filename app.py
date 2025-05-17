"""
PictoTongue - A web application for image-to-text translation

This script serves as the main entry point for the PictoTongue application,
providing a web interface for users to upload images, extract text, and translate
to various languages.
"""

import os
import base64
import time
import json
import re
import uuid
from datetime import datetime
from io import BytesIO
from typing import Dict, List, Optional, Tuple, Union

import cv2
import numpy as np
import pytesseract
from PIL import Image
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from deep_translator import GoogleTranslator
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# Configuration
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
MAX_IMAGE_SIZE = int(os.getenv("MAX_IMAGE_SIZE", 10 * 1024 * 1024))  # 10MB

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Language map
LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'zh-cn': 'Chinese (Simplified)',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ar': 'Arabic',
    'hi': 'Hindi',
    'bn': 'Bengali',
    'pa': 'Punjabi',
    'te': 'Telugu',
    'mr': 'Marathi',
    'ta': 'Tamil',
    'ur': 'Urdu',
    'gu': 'Gujarati',
    'kn': 'Kannada',
    'ml': 'Malayalam',
    'th': 'Thai',
    'vi': 'Vietnamese',
    'id': 'Indonesian',
    'ms': 'Malay',
    'tr': 'Turkish',
    'nl': 'Dutch',
    'sv': 'Swedish',
    'fi': 'Finnish',
    'da': 'Danish',
    'no': 'Norwegian',
    'pl': 'Polish',
    'hu': 'Hungarian',
    'cs': 'Czech',
    'el': 'Greek',
    'he': 'Hebrew',
    'fa': 'Persian'
}

# Initialize translator
translator = GoogleTranslator()

def allowed_file(filename: str) -> bool:
    """
    Check if the uploaded file has an allowed extension
    
    Args:
        filename (str): The name of the uploaded file
        
    Returns:
        bool: True if the file extension is allowed, False otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_image(image_path: str, lang: str = 'eng') -> str:
    """
    Extract text from an image using OCR
    
    Args:
        image_path (str): Path to the image file
        lang (str): Language code for OCR (default: 'eng')
        
    Returns:
        str: Extracted text from the image
    """
    try:
        # Map language codes to Tesseract language codes
        lang_map = {
            'en': 'eng',
            'es': 'spa',
            'fr': 'fra',
            'de': 'deu',
            'it': 'ita',
            'pt': 'por',
            'ru': 'rus',
            'zh-cn': 'chi_sim',
            'ja': 'jpn',
            'ko': 'kor',
            'ar': 'ara',
            'hi': 'hin',
            'bn': 'ben',
            'te': 'tel',
            'mr': 'mar',
            'ta': 'tam',
            'pa': 'pan',
            'gu': 'guj',
            'kn': 'kan',
            'ml': 'mal',
            'th': 'tha',
            'vi': 'vie'
        }
        
        tesseract_lang = lang_map.get(lang, 'eng')
        
        # Read the image
        img = cv2.imread(image_path)
        
        # Preprocess the image to improve OCR accuracy
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        
        # Apply OCR
        text = pytesseract.image_to_string(gray, lang=tesseract_lang)
        
        return text.strip()
    except Exception as e:
        print(f"Error during OCR: {e}")
        return "Error during text extraction. Please try again with a clearer image."

def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    """
    Translate text from one language to another using deep-translator.
    
    Args:
        text (str): Text to translate
        source_lang (str): Source language code
        target_lang (str): Target language code
        
    Returns:
        str: Translated text
    """
    try:
        if source_lang == target_lang:
            return text
            
        # Translate the text
        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated_text
    except Exception as e:
        print(f"Error during translation: {e}")
        return "Error during translation. Please try again later."
    
def save_base64_image(base64_data: str) -> Tuple[bool, str]:
    """
    Save a base64 encoded image to the uploads folder
    
    Args:
        base64_data (str): Base64 encoded image data
        
    Returns:
        Tuple[bool, str]: Success status and file path or error message
    """
    try:
        # Extract the base64 data part
        if 'base64,' in base64_data:
            base64_data = base64_data.split('base64,')[1]
        
        # Decode the base64 data
        image_data = base64.b64decode(base64_data)
        
        # Generate a unique filename
        filename = f"{uuid.uuid4().hex}.png"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        
        # Save the image
        with open(filepath, "wb") as f:
            f.write(image_data)
            
        return True, filepath
    except Exception as e:
        print(f"Error saving image: {e}")
        return False, str(e)

@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html', languages=LANGUAGES)

@app.route('/static/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory('static', path)

@app.route('/api/languages', methods=['GET'])
def get_languages():
    """API endpoint to get supported languages"""
    return jsonify(LANGUAGES)

@app.route('/api/translate', methods=['POST'])
def translate_image():
    """API endpoint to process image and translate text"""
    # Start processing timer
    start_time = time.time()
    
    # Parse request data
    data = request.json
    
    if not data or 'imageData' not in data:
        return jsonify({'error': 'No image data provided'}), 400
        
    image_data = data.get('imageData')
    from_lang = data.get('fromLang', 'en')
    to_lang = data.get('toLang', 'es')
    
    # Save the base64 image
    success, filepath = save_base64_image(image_data)
    
    if not success:
        return jsonify({'error': f'Failed to save image: {filepath}'}), 500
    
    try:
        # Extract text from the image
        original_text = extract_text_from_image(filepath, from_lang)
        
        # Translate the text
        translated_text = translate_text(original_text, from_lang, to_lang)
        
        # Calculate processing time
        processing_time = f"{time.time() - start_time:.2f} seconds"
        
        # Remove the temporary file
        os.remove(filepath)
        
        # Return the results
        return jsonify({
            'originalText': original_text,
            'translatedText': translated_text,
            'fromLang': from_lang,
            'toLang': to_lang,
            'processingTime': processing_time
        })
    except Exception as e:
        # Remove the temporary file if it exists
        if os.path.exists(filepath):
            os.remove(filepath)
            
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    debug = os.getenv("DEBUG", "False").lower() in ('true', '1', 't')
    
    print(f"Starting PictoTongue server on port {port}...")
    print(f"Open http://localhost:{port} in your browser")
    
    app.run(host='0.0.0.0', port=port, debug=debug)