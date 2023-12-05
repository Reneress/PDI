import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load test images
origImg =  cv2.imread('pcbCropped.png', cv2.IMREAD_GRAYSCALE) / 255.0
defectImg = cv2.imread('pcbCroppedTranslatedDefected.png', cv2.IMREAD_GRAYSCALE) / 255.0

# Perform shift
rows, cols = origImg.shape
xShift = 10
yShift = 10
registImg = np.zeros(defectImg.shape)
registImg[yShift:rows, xShift:cols] = defectImg[0:rows-yShift, 0:cols-xShift]

# Show difference images
diffImg1 = abs(origImg - defectImg)
plt.subplot(1, 3, 1), plt.imshow(diffImg1, cmap='gray'), plt.title('Unaligned Difference Image')
diffImg2 = abs(origImg - registImg)
plt.subplot(1, 3, 2), plt.imshow(diffImg2, cmap='gray'), plt.title('Aligned Difference Image')
bwImg = diffImg2 > 0.15
height, width = bwImg.shape
border = round(0.05 * width)
borderMask = np.zeros((height, width))
borderMask[border:height-border, border:width-border] = 1
bwImg = bwImg * borderMask
plt.subplot(1, 3, 3), plt.imshow(bwImg, cmap='gray'), plt.title('Thresholded + Aligned Difference Image')
plt.show()

# Save images
cv2.imwrite('Defect_Detection_diff.png', diffImg1 * 255)
cv2.imwrite('Defect_Detection_diffRegisted.png', diffImg2 * 255)
cv2.imwrite('Defect_Detection_bw.png', bwImg * 255)
