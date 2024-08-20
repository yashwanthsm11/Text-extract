import pytesseract
import pandas as pd

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        text = pytesseract.image_to_string(image_path)
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

# Example usage
image_path = 'D:\\terrologic task\\image_folder\\dfd diagram.png'
extracted_text = extract_text_from_image(image_path)
print(extracted_text)
