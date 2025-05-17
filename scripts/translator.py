import os
import sys
import argparse
from PIL import Image
import pytesseract
from googletrans import Translator
import time
import logging


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("picto_tongue.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class PictoTongue:
    def __init__(self, input_folder, output_folder, target_language="es"):
        """
        Initialize the PictoTongue.

        Args:
            input_folder (str): Path to the folder containing images
            output_folder (str): Path to the folder where translations will be saved
            target_language (str): Target language code (default: Spanish 'es')
        """
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.target_language = target_language
        self.translator = Translator()

        # Verify input folder exists
        if not os.path.exists(input_folder):
            logger.error(f"Input folder does not exist: {input_folder}")
            sys.exit(1)

        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            logger.info(f"Created output folder: {output_folder}")

    def process_images(self):
        """Process all images in the input folder."""
        # Get all image files from the input folder
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
        image_files = [
            f for f in os.listdir(self.input_folder)
            if os.path.isfile(os.path.join(self.input_folder, f))
            and any(
                f.lower().endswith(ext)
                for ext in image_extensions
            )
        ]

        if not image_files:
            logger.warning(f"No image files found in {self.input_folder}")
            return

        logger.info(f"Found {len(image_files)} image(s) to process")

        # Process each image
        for image_file in image_files:
            logger.info(f"Processing image: {image_file}")

            try:
                # Extract text
                image_path = os.path.join(self.input_folder, image_file)
                extracted_text = self.extract_text(image_path)

                if not extracted_text.strip():
                    logger.warning(f"No text extracted from {image_file}")
                    continue

                # Translate text
                translated_text = self.translate_text(extracted_text)

                # Save results
                self.save_results(image_file, extracted_text, translated_text)

                logger.info(f"Successfully processed {image_file}")

            except Exception as e:
                logger.error(f"Error processing {image_file}: {str(e)}")

    def extract_text(self, image_path):
        """
        Extract text from an image using OCR.

        Args:
            image_path (str): Path to the image file

        Returns:
            str: Extracted text
        """
        logger.info(f"Extracting text from {image_path}")

        try:
            # Open image
            image = Image.open(image_path)

            # Convert image to grayscale for better OCR results
            if image.mode != 'L':
                image = image.convert('L')

            # Extract text using Tesseract
            text = pytesseract.image_to_string(image)

            logger.info(f"Extracted {len(text.split())} words")
            return text.strip()

        except Exception as e:
            logger.error(f"OCR error: {str(e)}")
            raise

    def translate_text(self, text):
        """
        Translate text to the target language.

        Args:
            text (str): Text to translate

        Returns:
            str: Translated text
        """
        logger.info(f"Translating text to {self.target_language}")

        try:
            # Add delay to avoid rate limiting
            time.sleep(1)

            # Translate text
            translation = self.translator.translate(text, dest=self.target_language)

            logger.info("Translation completed")
            return translation.text

        except Exception as e:
            logger.error(f"Translation error: {str(e)}")
            raise

    def save_results(self, image_filename, original_text, translated_text):
        """
        Save original and translated text to output files.

        Args:
            image_filename (str): Name of the processed image file
            original_text (str): Extracted text
            translated_text (str): Translated text
        """
        # Create a subfolder in the output directory named after the language code for translated text
        lang_folder = os.path.join(self.output_folder, self.target_language)
        if not os.path.exists(lang_folder):
            os.makedirs(lang_folder)
            logger.info(f"Created language-specific folder: {lang_folder}")

        # Create base filename without extension
        base_filename = os.path.splitext(image_filename)[0]

        # Save original text directly in the output folder
        original_path = os.path.join(self.output_folder, f"{base_filename}_original.txt")
        with open(original_path, 'w', encoding='utf-8') as f:
            f.write(original_text)

        # Save translated text in the language-specific folder
        translated_path = os.path.join(lang_folder, f"{base_filename}_translated.txt")
        with open(translated_path, 'w', encoding='utf-8') as f:
            f.write(translated_text)

        logger.info(f"Saved original text to {original_path}")
        logger.info(f"Saved translated text to {translated_path}")


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Translate images to a target language')

    # Set input and output directories relative to the root directory
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Go one level up to the root directory
    input_dir = os.path.join(root_dir, 'input')  # Path to input folder in the root directory
    output_dir = os.path.join(root_dir, 'output')  # Path to output folder in the root directory

    parser.add_argument('--input', default=input_dir, help='Input folder containing images')
    parser.add_argument('--output', default=output_dir, help='Output folder for translated texts')
    parser.add_argument('--lang', default='es', help='Target language code (default: Spanish "es")')
    args = parser.parse_args()

    logger.info("Starting PictoTongue process")
    logger.info(f"Input folder: {args.input}")
    logger.info(f"Output folder: {args.output}")
    logger.info(f"Target language: {args.lang}")

    # Create and run translator
    translator = PictoTongue(args.input, args.output, args.lang)
    translator.process_images()

    logger.info("Process completed")


if __name__ == "__main__":
    main()
