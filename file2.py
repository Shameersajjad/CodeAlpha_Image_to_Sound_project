import pytesseract
from PIL import Image
from gtts import gTTS
import os

# Path to the Tesseract executable (update this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Function to extract text from an image using PyTesseract


def extract_text_from_image(image_path):
    try:
        # Open the image using PIL (Python Imaging Library)
        image = Image.open(image_path)

        # Use PyTesseract to extract text from the image
        text = pytesseract.image_to_string(image)

        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to convert text to sound using gTTS
def text_to_sound(text, output_path):
    try:
        # Create a gTTS object and save the audio to the output file
        tts = gTTS(text)
        tts.save(output_path)
        print(f"Sound saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Specify the input image path
    input_image_path = "imagetext.jpg.jpg"

    # Specify the output sound file path
    output_sound_path = "sound.mp3"

    # Extract text from the input image
    extracted_text = extract_text_from_image(input_image_path)

    if extracted_text:
        # Convert the extracted text to sound
        text_to_sound(extracted_text, output_sound_path)
    else:
        print("Text extraction failed.")
