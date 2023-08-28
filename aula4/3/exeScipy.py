import matplotlib.pyplot as plt
import imageio
import numpy as np
from scipy import ndimage, misc
from scipy.ndimage import interpolation

def reduzir(im, scale):
    
    scale = 1/ scale
    imr = interpolation.zoom(im,zoom = (scale, scale, 1))
    
    return imr


def aumentar(im, scale):
    
    imr = interpolation.zoom(im,zoom = (scale, scale, 1))
    
    return imr

def translacao(im, x, y):
    deslocamento = [x,y]
    tmatrix = np.eye(3)
    tmatrix[0,2] = deslocamento[0]
    tmatrix[1,2] = deslocamento[1]
    
    imT = ndimage.affine_transform(im, tmatrix)
    
    return imT
def main():
    
    im = imageio.imread('lena_gray_512_salt_pepper.tif')
    im2 = imageio.imread('house.tif')
    im3 = imageio.imread('cameraman.tif')
    
    imR = reduzir(im, 1.5)
    imR2 = reduzir(im2, 1.5)
    imR3 = reduzir(im3,1.5)
    
    imA = aumentar(im,2.5)
    imA2 = aumentar(im2,2.5)
    imA3 = aumentar(im3,2.5)
            
    imRot90 = ndimage.rotate(im,90)
    im2Rot90 = ndimage.rotate(im2,90)
    im3Rot90 = ndimage.rotate(im3,90)
    
    imRot45 = ndimage.rotate(im,45)
    im2Rot45 = ndimage.rotate(im2,45)
    im3Rot45 = ndimage.rotate(im3,45)
    
    imRot100= ndimage.rotate(im,100)
    im2Rot100 = ndimage.rotate(im2,100)
    im3Rot100 = ndimage.rotate(im3,100)
    
    imTras = translacao(im, 50, 50)
    im2Tras = translacao(im2, 50, 50)
    im3Tras = translacao(im3, 50,50)
    
    imTras3545 = translacao(im,35,45)
    im2Tras3545 = translacao(im2,35,45)
    im3Tras3545 = translacao(im3,35,45)
    
    #create two colums plot
    fig = plt.figure()
    plt1 = plt.subplot(3,8,1)
    plt2 = plt.subplot(3,8,2)
    plt3 = plt.subplot(3,8,3)
    plt4 = plt.subplot(3,8,4)
    plt5 = plt.subplot(3,8,5)
    plt6 = plt.subplot(3,8,6)
    plt7 = plt.subplot(3,8,7)
    plt8 = plt.subplot(3,8,8)
    plt9 = plt.subplot(3,8,9)
    plt10 = plt.subplot(3,8,10)
    plt11 = plt.subplot(3,8,11)
    plt12 = plt.subplot(3,8,12)
    plt13 = plt.subplot(3,8,13)
    plt14 = plt.subplot(3,8,14)
    plt15 = plt.subplot(3,8,15)
    plt16 = plt.subplot(3,8,16)
    plt17 = plt.subplot(3,8,17)
    plt18 = plt.subplot(3,8,18)
    plt19 = plt.subplot(3,8,19)
    plt20 = plt.subplot(3,8,20)
    plt21 = plt.subplot(3,8,21)
    plt22 = plt.subplot(3,8,22)
    plt23 = plt.subplot(3,8,23)
    plt24 = plt.subplot(3,8,24)
    
    
    
    
   
  
    
    plt1.title.set_text('original')
    plt2.title.set_text('pequena')
    plt3.title.set_text('grande')
    plt4.title.set_text('rotacao 45')
    plt5.title.set_text('rotacao 90')
    plt6.title.set_text('rotacao 100')
    plt7.title.set_text('translacao')
    plt8.title.set_text('translacao 35-45')
    
    plt9.title.set_text('original')
    plt10.title.set_text('pequena')
    plt11.title.set_text('grande')
    plt12.title.set_text('rotacao 45')
    plt13.title.set_text('rotacao 90')
    plt14.title.set_text('rotacao 100')
    plt15.title.set_text('translacao')
    plt16.title.set_text('translacao 35-45')
    
    plt17.title.set_text('original')
    plt18.title.set_text('pequena')
    plt19.title.set_text('grande')
    plt20.title.set_text('rotacao 45')
    plt21.title.set_text('rotacao 90')
    plt22.title.set_text('rotacao 100')
    plt23.title.set_text('translacao')
    plt24.title.set_text('translacao 35-45')
    
    
    plt1.imshow(im, cmap='gray')
    plt2.imshow(imR, cmap='gray', vmin=0, vmax=255)
    plt3.imshow(imA, cmap='gray', vmin=0, vmax=255)
    plt4.imshow(imRot45, cmap='gray', vmin=0, vmax=255)
    plt5.imshow(imRot90, cmap='gray', vmin=0, vmax=255)
    plt6.imshow(imRot100, cmap='gray', vmin=0, vmax=255)
    plt7.imshow(imTras, cmap='gray', vmin=0, vmax=255)
    plt8.imshow(imTras3545, cmap='gray', vmin=0, vmax=255)
    
    plt9.imshow(im2, cmap='gray')
    plt10.imshow(imR2, cmap='gray', vmin=0, vmax=255)
    plt11.imshow(imA2, cmap='gray', vmin=0, vmax=255)
    plt12.imshow(im2Rot45, cmap='gray', vmin=0, vmax=255)
    plt13.imshow(im2Rot90, cmap='gray', vmin=0, vmax=255)
    plt14.imshow(im2Rot100, cmap='gray', vmin=0, vmax=255)
    plt15.imshow(im2Tras, cmap='gray', vmin=0, vmax=255)
    plt16.imshow(im2Tras3545, cmap='gray', vmin=0, vmax=255)
    
    plt17.imshow(im3, cmap='gray')
    plt18.imshow(imR3, cmap='gray', vmin=0, vmax=255)
    plt19.imshow(imA3, cmap='gray', vmin=0, vmax=255)
    plt20.imshow(im3Rot45, cmap='gray', vmin=0, vmax=255)
    plt21.imshow(im3Rot90, cmap='gray', vmin=0, vmax=255)
    plt22.imshow(im3Rot100, cmap='gray', vmin=0, vmax=255)
    plt23.imshow(im3Tras, cmap='gray', vmin=0, vmax=255)
    plt24.imshow(im3Tras3545, cmap='gray', vmin=0, vmax=255)
    
    
    plt.show()


    
if __name__ == "__main__":
    main()

   