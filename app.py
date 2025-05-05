from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import sys
from newspaper_translator import NewspaperTranslator

app = Flask(__name__, 
            static_folder='frontend',
            template_folder='frontend')

# Ensure input and output directories exist
os.makedirs('input', exist_ok=True)
os.makedirs('output', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image = request.files['image']
    language = request.form.get('language', 'es')
    
    # Save the uploaded image to the input folder
    image_path = os.path.join('input', image.filename)
    image.save(image_path)
    
    # Create translator instance
    translator = NewspaperTranslator('input', 'output', language)
    
    try:
        # Process the image
        translator.process_images()
        
        # Get the output files
        base_filename = os.path.splitext(image.filename)[0]
        original_path = os.path.join('output', f"{base_filename}_original.txt")
        translated_path = os.path.join('output', f"{base_filename}_translated.txt")
        
        # Read the output files
        original_text = ""
        translated_text = ""
        
        if os.path.exists(original_path):
            with open(original_path, 'r', encoding='utf-8') as f:
                original_text = f.read()
        
        if os.path.exists(translated_path):
            with open(translated_path, 'r', encoding='utf-8') as f:
                translated_text = f.read()
        
        return jsonify({
            'originalText': original_text,
            'translatedText': translated_text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Serve static files from frontend folder
@app.route('/frontend/<path:path>')
def serve_static(path):
    return send_from_directory('frontend', path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
