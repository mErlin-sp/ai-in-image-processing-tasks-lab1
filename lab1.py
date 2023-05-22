import imutils as imutils
import numpy as np
import cv2

print('Lab1. OpenCV version: ' + cv2.__version__)

# upload the file as a colour image and as a grey image
img = cv2.imread('daenerys.jpg')
img_gray = cv2.imread('daenerys.jpg', 0)

cv2.imshow(' Raw image ', img)
# closes all windows after pressing an arbitrary key
cv2.waitKey(0)
cv2.destroyAllWindows()

# saving the image to a file
cv2.imwrite('daenerys-1.jpg', img)

# output the image size
(h, w, d) = img.shape  #
print(' width ={}, height ={}, depth ={}'.format(w, h, d))

# access to RGB pixel with coordinates x=50, y=100
(B, G, R) = img[100, 50]
print('R={}, G={}, B={}'.format(R, G, B))

# extract a square ROI ( Region of Interest ) from the
# input image starting at x=350 ,y=250 at ending at x=650 ,y=0
roi = img[0:250, 350:650]
cv2.imshow(' ROI ', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# resize the image to 800x450px , ignoring aspect ratio
img = cv2.resize(img, (800, 450))
cv2.imshow(' Fixed Resizing ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# resize the image to 800x450px, saving aspect ratio
h, w = img.shape[0:2]  # height and width of the original image
h_new = 450  # height of the new image
ratio = w / h  # width to height ratio
w_new = int(h_new * ratio)  # width of the new image
resized = cv2.resize(img, (w_new, h_new))  # resize the original image
print(resized.shape)
cv2.imshow(' Fixed Resizing ', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# rotate the image by 45 degrees
rotated = imutils.rotate(img, -45)
cv2.imshow(' Imutils Rotation ', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it ,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(img, (11, 11), 0)
cv2.imshow(' Blurred ', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# draw rectangle
cv2.rectangle(img, (350, 0), (650, 250), (0, 0, 255), 2)
cv2.imshow(' Rectangle ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# draw line
points = np.array(
    [[262, 448], [273, 386], [306, 352], [307, 318], [345, 294], [379, 269], [386, 237], [381, 216], [394, 195],
     [387, 161], [386, 124], [392, 82], [402, 46], [417, 13], [435, -1], [600, 0], [604, 14], [613, 33], [622, 45],
     [626, 77], [634, 103], [630, 118], [626, 137], [630, 173], [628, 199], [631, 211], [644, 233], [645, 246],
     [662, 263], [686, 269], [718, 281], [732, 292], [734, 306], [729, 319], [732, 334], [747, 369], [753, 400],
     [758, 428], [758, 449]])
cv2.polylines(img, np.int32([points]), 2, (255, 0, 0))
cv2.imshow(' Lines ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# draw circle
cv2.circle(img, (494, 114), 128, (0, 255, 0), 2)
cv2.imshow(' Circle ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# draw text
font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX
font2 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(img, 'Daenerys', (400, 300), font, 1, (102, 0, 204), 2, cv2.LINE_4)
cv2.imshow(' Text ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
