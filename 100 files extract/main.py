import os
import pytesseract
import pandas as pd

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
  """Extracts text from an image using Tesseract OCR."""
  try:
    # Ensure Tesseract is installed (pip install pytesseract)
    text = pytesseract.image_to_string(image_path)
    return text
  except Exception as e:
    print(f"Error extracting text from {image_path}: {e}")
    return ""

def process_images_in_folder(folder_path):
  """Processes images in a folder and creates a Pandas DataFrame."""
  data = []
  for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
      file_path = os.path.join(folder_path, filename)
      text = extract_text_from_image(file_path)
      data.append({'filename': filename, 'extracted_text': text})

  df = pd.DataFrame(data)
  return df

if __name__ == "__main__":
  folder_path = 'D:\\terrologic task\\image_folder'
  df = process_images_in_folder(folder_path)
  print(df)
  df.to_csv('extracted_text.csv', index=False)
