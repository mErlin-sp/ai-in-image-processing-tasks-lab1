import imutils as imutils
import numpy as np
import cv2

print(cv2.__version__)

# завантажуємо файл як кольорове зображення і як сіре зображення
img = cv2.imread('daenerys-targaryen.jpg')
img_gray = cv2.imread('daenerys-targaryen.jpg', 0)

cv2.imshow('Raw image', img)
# закриваються всі вікна після натискання довільної клавіші
cv2.waitKey(0)
cv2.destroyAllWindows()

# збереження зображення в файл
cv2.imwrite('daenerys-targaryen-1.jpg', img)

# вивід розміру зображення
(h, w, d) = img.shape  #
print(" width ={}, height ={}, depth ={}".format(w, h, d))

# доступ до RGB пікселя з координатами x=50 , y=100
(B, G, R) = img[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# extract a square ROI ( Region of Interest ) from the
# input image starting at x=1500 ,y=470 at ending at x=1100 ,y=6
roi = img[6:470, 1100:1500]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# resize the image to 960x540px , ignoring aspect ratio
img = cv2.resize(img, (960, 540))
cv2.imshow("Fixed Resizing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# resize the image to 960x540px, saving aspect ratio
h, w = img.shape[0:2]  # висота і ширина оригінального зображення
h_new = 540  # висота нового зображення
ratio = w / h  # відношення ширини до висоти
w_new = int(h_new * ratio)  # ширина нового зображення
resized = cv2.resize(img, (w_new, h_new))  # зміна розміру оригінального зображення
print(resized.shape)
cv2.imshow('Fixed Resizing', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# поворот зображення на 45 градусів
rotated = imutils.rotate(img, -45)
cv2.imshow(" Imutils Rotation ", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it ,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(img, (11, 11), 0)
cv2.imshow(" Blurred ", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# draw rectangle
cv2.rectangle(img, (550, 3), (750, 235), (0, 0, 255), 2)
cv2.imshow(" Rectangle ", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# draw line
zero_img = np.zeros((1000, 1000, 3), np.uint8)
points = np.array([[600, 200], [910, 641], [300, 300], [0, 0]])
cv2.polylines(zero_img, np.int32([points]), 1, (255, 255, 255))
cv2.imshow('1', zero_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# draw circle
zero_img = np.zeros((200, 200, 3), np.uint8)
output = img.copy()
cv2.circle(zero_img, (100, 100), 50, (0, 0, 255), 2)
cv2.imshow(" Circle ", zero_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# draw text
font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX
font2 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(img, 'Daenerys Targaryen', (550, 300), font, 1, (0, 0, 255), 2, cv2.LINE_4)
cv2.imshow(" Text ", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
