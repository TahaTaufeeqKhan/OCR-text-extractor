from PIL import Image
import pytesseract

# Set the path to the Tesseract OCR executable directory
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Tkhan\PycharmProjects\pythonProject1\tesseract.exe'

def extract_text_from_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(img)

    return text

# Replace 'C:\\Users\\Tkhan\\Downloads\\ocr-test.jpg' with the actual path to your image
image_path = r'C:\Users\Tkhan\Downloads\PythonProject\testImg2.jpg'
extracted_text = extract_text_from_image(image_path)

print("Extracted Text:")
print(extracted_text)
