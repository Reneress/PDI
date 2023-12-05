import matplotlib.pyplot as plt
import imageio
import numpy as np
from imageio import imread
from scipy import ndimage
from scipy import misc
from PIL import Image, ImageFilter


def main():


    im = imageio.imread('lena_gray_512_salt_pepper.tif')
    im2 = imageio.imread('biel.png')
    im3 = imageio.imread('cameraman.tif')
    
    k = np.ones((3,3),np.float32)/9
   
    imm = ndimage.convolve(im, k)
    imme = ndimage.median_filter(im, size=3)
    
    imm2 = ndimage.convolve(im2, k)
    imme2 = ndimage.median_filter(im2, size=3)
    
    imm3 = ndimage.convolve(im3, k)
    imme3 = ndimage.median_filter(im3, size=3)
    
    #create two colums plot
    fig = plt.figure()
    plt1 = plt.subplot(3,3,1)
    plt2 = plt.subplot(3,3,2)
    plt3 = plt.subplot(3,3,3)
    plt4 = plt.subplot(3,3,4)
    plt5 = plt.subplot(3,3,5)
    plt6 = plt.subplot(3,3,6)
    plt7 = plt.subplot(3,3,7)
    plt8 = plt.subplot(3,3,8)
    plt9 = plt.subplot(3,3,9)
    
    
    plt1.title.set_text('original')
    plt2.title.set_text('mean filter')
    plt3.title.set_text('median filter')
    plt4.title.set_text('original')
    plt5.title.set_text('mean filter')
    plt6.title.set_text('median filter')
    plt7.title.set_text('original')
    plt8.title.set_text('mean filter')
    plt9.title.set_text('median filter')
    
    plt1.imshow(im, cmap='gray')
    plt2.imshow(imm, cmap='gray', vmin=0, vmax=255)
    plt3.imshow(imme, cmap='gray', vmin=0, vmax=255)
    plt4.imshow(im2, cmap='gray')
    plt5.imshow(imm2, cmap='gray', vmin=0, vmax=255)
    plt6.imshow(imme2, cmap='gray', vmin=0, vmax=255)
    plt7.imshow(im3, cmap='gray')
    plt8.imshow(imm3, cmap='gray', vmin=0, vmax=255)
    plt9.imshow(imme3, cmap='gray', vmin=0, vmax=255)
    
    plt.show()
   

    
if __name__ == "__main__":
    main()
