import cv2
import pytesseract

img = cv2.imread('./hello.png')
dst = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
text = pytesseract.image_to_string(dst, lang='kor+eng')
print(text)
