import cv2
import numpy as np
import matplotlib.pyplot as plt

def plotar(im1,n):
    
    f = np.fft.fft2(im1)
    
    fshift = np.fft.fftshift(f)
    
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    
    mag = 20*np.log(np.abs(f))
    
    fase = np.angle(f)
    
    
    

    plt.subplot(221),plt.imshow(im1, cmap = 'gray')
    plt.title(n), plt.xticks([]), plt.yticks([])
    
    plt.subplot(222),plt.imshow(mag, cmap = 'gray')
    plt.title('Magnitude Spectrum não centralizado'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(223),plt.imshow(fase, cmap = 'gray')
    plt.title('Fase não centralizado'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(224),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    
    
    
    
    plt.show()
                
                
                
def main():

    # Crie uma imagem preta
    imagem = np.zeros((512, 512, 3), dtype = "uint8")

    # Desenhe um quadrado branco
    cv2.rectangle(imagem, (128, 128), (384, 384), (255, 255, 255), -1)
    
    im = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    plotar(im,"Quadrado")
    
    while(True):
        print("Selecione a opção: 1: rotação, 2= translação, 3=zoom ou 5 = sair")
        m = int(input())
        (altura, largura) = im.shape[:2]
        if(m ==1 ):
            centro = (largura / 2, altura / 2)
            matriz = cv2.getRotationMatrix2D(centro, 40, 1.0)
            plotar(cv2.warpAffine(im, matriz, (largura, altura)),"Rotação 40 graus")
        elif(m==2):
            desloc_x = largura / 6
            desloc_y = altura / 6
            matriz = np.float32([[1, 0, desloc_x], [0, 1, desloc_y]])
            plotar(cv2.warpAffine(im, matriz, (largura, altura)),"Translação")
        elif(m==3):
            zoom = 1.5
            imzoom= cv2.resize(im, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_LINEAR)
            plotar(imzoom,"Zoom")
        elif(m==5):
            break
        else:
            break
            
if __name__ == "__main__":
    main()