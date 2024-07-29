from pytesseract import pytesseract
import cv2
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = "WhatsApp Image 2024-07-28 at 2.51.05 PM.jpeg"
image = cv2.imread(img)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
custom_config = r'--oem 3 --psm 6'
text_data = pytesseract.image_to_string(threshold_image, config=custom_config)

print(text_data)