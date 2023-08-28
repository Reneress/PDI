from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    
    print("hello world")
    im = Image.open('lena_gray_512.tif')
    #im.show()
    
    im_ndarray = np.array(im)
    #plt.imshow(im_ndarray, cmap='gray')
    #plt.show()
    
    #Operação pixel a pixel, escureçendo
    im_dark = im_ndarray.copy()
    im_dark = im_dark/4

    #Operação em vizinhança
    im2 = Image.open('lena_gray_512_salt_pepper.tif')
    im2_ndarray = np.array(im2)
    #plt.imshow(im2_ndarray, cmap='gray')
      
    #create two colums plot
    fig = plt.figure()
    plt1 = plt.subplot(1,2,1)
    plt2 = plt.subplot(1,2,2)
    plt1.title.set_text('original')
    plt2.title.set_text('modified')
    
    plt1.imshow(im_ndarray, cmap='gray')
    plt2.imshow(im_dark, cmap='gray', vmin=0, vmax=255)
    plt.show()
   

    
if __name__ == "__main__":
    main()
