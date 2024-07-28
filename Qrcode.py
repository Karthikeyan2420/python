import qrcode
img = qrcode.make("hai thamizha")
img.save("hiphop.jpg") 




#pip install opencv-python
import cv2
qr_img= cv2.imread("hiphop.jpg")
qr_det = cv2.QRCodeDetector()
val,pts,st_code= qr_det.detectAndDecode(qr_img)
print("Information:", val)


