from PIL import Image
import pytesseract
import pyperclip
extracted_text = pytesseract.image_to_string(Image.open('/tmp/a.png'))
pyperclip.copy(extracted_text)

