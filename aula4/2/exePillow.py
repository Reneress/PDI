from PIL import Image, ImageFilter
import matplotlib.pyplot as plt


def main():
    
    im = Image.open('lena_gray_512_salt_pepper.tif')
    im2 = Image.open('house.tif')
    im3 = Image.open('cameraman.tif')
     
    imm = im.filter(ImageFilter.BoxBlur(radius=3))
    imme = im.filter(ImageFilter.MedianFilter(size=3))
    
    imm2 = im2.filter(ImageFilter.BoxBlur(radius=3))
    imme2 = im2.filter(ImageFilter.MedianFilter(size=3))
    
    imm3 = im3.filter(ImageFilter.BoxBlur(radius=3))
    imme3 = im3.filter(ImageFilter.MedianFilter(size=3))
    
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
