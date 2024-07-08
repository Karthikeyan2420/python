""" import qrcode
img = qrcode.make("st.joseph institute of technology")
img.save("img1.jpg") """


import cv2
qr_img = cv2.imread("img1.jpg")
qr_det = cv2.QRCodeDetector()
val, pts, st_code = qr_det.detectAndDecode(qr_img)
print("Information:", val) 