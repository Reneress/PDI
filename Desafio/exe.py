import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read video
cap = cv2.VideoCapture('surveillance.mpg')
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('Background_Subtraction.avi', fourcc, 30.0, (640,480))

# Perform background accumulation and subtraction
alpha = 0.95
theta = 0.1
ret, frame = cap.read()
background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
background = background.astype(float)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        currImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        currImg = currImg.astype(float)
        background = alpha * background + (1 - alpha) * currImg
        diffImg = abs(currImg - background)
        ret, threshImg = cv2.threshold(diffImg, theta, 255, cv2.THRESH_BINARY)

        plt.subplot(2, 2, 1), plt.imshow(currImg, cmap='gray'), plt.title('New frame')
        plt.subplot(2, 2, 2), plt.imshow(background, cmap='gray'), plt.title('Background frame')
        plt.subplot(2, 2, 3), plt.imshow(diffImg, cmap='gray'), plt.title('Difference image')
        plt.subplot(2, 2, 4), plt.imshow(threshImg, cmap='gray'), plt.title('Thresholded difference image')
        plt.show()

        out.write(frame)
    else:
        break

cap.release()
out.release()

# Save images
cv2.imwrite('Background_Subtraction_curr.png', currImg)
cv2.imwrite('Background_Subtraction_background.png', background)
cv2.imwrite('Background_Subtraction_thresh.png', threshImg)
