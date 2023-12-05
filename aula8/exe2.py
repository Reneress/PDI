import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from math import exp

def inverse_fourier_transform(fshift):
    f_ishift = np.fft.ifftshift(fshift)
    im1_back = np.fft.ifft2(f_ishift)
    im1_back = np.abs(im1_back)
    return im1_back   

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def idealFilterLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((y,x),center) < D0:
                base[y,x] = 1
    return base

def idealFilterHP(D0,imgShape):
    base = np.ones(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((y,x),center) < D0:
                base[y,x] = 0
    return base

def butterworthLP(D0,imgShape,n):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1/(1+(distance((y,x),center)/D0)**(2*n))
    return base

def butterworthHP(D0,imgShape,n):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1-1/(1+(distance((y,x),center)/D0)**(2*n))
    return base

def gaussianLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base

def gaussianHP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1 - exp(((-distance((y,x),center)**2)/(2*(D0**2))))
            
    return base

def plotarPassaAlta(im1):
    
    f = np.fft.fft2(im1)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    #fase = np.angle(fshift)
    
    PassaaltaIdeal= idealFilterHP(20,fshift.shape)
    # PassaaltaButterworth= butterworthHP(50,fshift.shape,2)
    # PassaltaGaussiano= gaussianHP(50,fshift.shape)
    
    ImAltaIdeal = fshift*PassaaltaIdeal
    # ImAltaGaussiano = fshift*PassaltaGaussiano
    # ImAltaButterworth = fshift*PassaaltaButterworth
    
    ImAltaIdeal = inverse_fourier_transform(np.fft.ifftshift(ImAltaIdeal))
    # ImAltaButterworth = inverse_fourier_transform(np.fft.ifftshift(ImAltaButterworth))
    # ImAltaGaussiano = inverse_fourier_transform(np.fft.ifftshift(ImAltaGaussiano))
    
    
    plt.subplot(221),plt.imshow(im1, cmap = 'gray')
    plt.title("Original"), plt.xticks([]), plt.yticks([])

    
    plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
    
    # plt.subplot(333),plt.imshow(fase, cmap = 'gray')
    # plt.title('Fase'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(223),plt.imshow(PassaaltaIdeal, cmap = 'gray')
    plt.title('Passa Alta Ideal'), plt.xticks([]), plt.yticks([])
    
    # plt.subplot(335),plt.imshow(PassaaltaButterworth, cmap = 'gray')
    # plt.title('Passa Alta Butterworth'), plt.xticks([]), plt.yticks([])
    
    # plt.subplot(336),plt.imshow(PassaltaGaussiano, cmap = 'gray')
    # plt.title('Passa Alta Gaussiano'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(224),plt.imshow(ImAltaIdeal, cmap = 'gray')
    plt.title('Imagem Passa Alta Ideal'), plt.xticks([]), plt.yticks([])
    
    # plt.subplot(338),plt.imshow(ImAltaButterworth, cmap = 'gray')
    # plt.title('Imagem Passa Alta Butterworth'), plt.xticks([]), plt.yticks([])
    
    # plt.subplot(339),plt.imshow(ImAltaGaussiano, cmap = 'gray')
    # plt.title('Imagem Passa Alta Gaussiano'), plt.xticks([]), plt.yticks([])
    
    plt.show()
    
def plotarpassabaixa(im1):
    
    f = np.fft.fft2(im1)
    
    fshift = np.fft.fftshift(f)
    
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    
    #fase = np.angle(fshift)
    
    PassabaixaIdeal= idealFilterLP(20,fshift.shape)
    # PassabaixaButterworth= butterworthLP(50,fshift.shape,2)
    # PassabaixaGaussiano= gaussianLP(50,fshift.shape)
    
    ImBaixaIdeal = fshift*PassabaixaIdeal
    # ImBaixaButterworth = fshift*PassabaixaButterworth
    # ImBaixaGaussiano = fshift*PassabaixaGaussiano
    
    ImBaixaIdeal = inverse_fourier_transform(np.fft.ifftshift(ImBaixaIdeal))
    # ImBaixaButterworth = inverse_fourier_transform(np.fft.ifftshift(ImBaixaButterworth))
    # ImBaixaGaussiano = inverse_fourier_transform(np.fft.ifftshift(ImBaixaGaussiano))

    

    plt.subplot(221),plt.imshow(im1, cmap = 'gray')
    plt.title("Original"), plt.xticks([]), plt.yticks([])

    
    plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
    
    # plt.subplot(233),plt.imshow(fase, cmap = 'gray')
    # plt.title('Fase'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(223),plt.imshow(PassabaixaIdeal, cmap = 'gray')
    plt.title('Passa Baixa Ideal'), plt.xticks([]), plt.yticks([])
    
    # plt.subplot(335),plt.imshow(PassabaixaButterworth, cmap = 'gray')
    # plt.title('Passa Baixa Butterworth'), plt.xticks([]), plt.yticks([])
    
    # plt.subplot(336),plt.imshow(PassabaixaGaussiano, cmap = 'gray')
    # plt.title('Passa Baixa Gaussiano'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(224),plt.imshow(np.real(ImBaixaIdeal), cmap = 'gray')
    plt.title('Imagem Passa Baixa Ideal'), plt.xticks([]), plt.yticks([])
    
    # plt.subplot(338),plt.imshow(np.real(ImBaixaButterworth), cmap = 'gray')
    # plt.title('Imagem Passa Baixa Butterworth'), plt.xticks([]), plt.yticks([])
    
    # plt.subplot(339),plt.imshow(np.real(ImBaixaGaussiano), cmap = 'gray')
    # plt.title('Imagem Passa Baixa Gaussiano'), plt.xticks([]), plt.yticks([])
    
    
    
    plt.show()
    

def idealFilterLHP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((y,x),center) < D0:
                base[y,x] = 0
            else:
                base[y,x] = 1
    return base


def plotarPassaFaixa(im1):
    f = np.fft.fft2(im1)
    
    fshift = np.fft.fftshift(f)
    
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    
    passabaixaIdeal= idealFilterLP(20,fshift.shape)
    passaaltaideal = idealFilterHP(20,fshift.shape)
    passafaixaIdeal = idealFilterLHP(20,fshift.shape)
    
    impassabaixaIdeal = fshift*passabaixaIdeal
    impassaaltaideal = fshift*passaaltaideal
    impassafaixaIdeal = fshift*passafaixaIdeal
    
    impassabaixaIdeal = inverse_fourier_transform(np.fft.ifftshift(impassabaixaIdeal))
    impassaaltaideal = inverse_fourier_transform(np.fft.ifftshift(impassaaltaideal))
    impassafaixaIdeal = inverse_fourier_transform(np.fft.ifftshift(impassafaixaIdeal))
    
    plt.subplot(321),plt.imshow(im1, cmap = 'gray')
    plt.title("Original"), plt.xticks([]), plt.yticks([])
    
    plt.subplot(322),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(323),plt.imshow(impassabaixaIdeal, cmap = 'gray')
    plt.title('Passa Baixa Ideal'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(324),plt.imshow(impassaaltaideal, cmap = 'gray')
    plt.title('Passa Alta Ideal'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(325),plt.imshow(np.real(impassafaixaIdeal), cmap = 'gray')      
    plt.title('Imagem Passa Faixa Ideal'), plt.xticks([]), plt.yticks([])
    
    plt.show()
    
def main():
    while(True):
        print("Selecione a imagem: 1 , 2, 3 ou 4")
        im = input()
    
        if im == '1':
            im1 =cv.imread("car.tif", cv.IMREAD_GRAYSCALE)
        elif im == '2':
            im1 = cv.imread('len_periodic_noise.png', cv.IMREAD_GRAYSCALE)
        elif im == '3':
            im1 = cv.imread('periodic_noise.png', cv.IMREAD_GRAYSCALE)
        elif im == '4':
            im1 = cv.imread('newspaper_shot_woman.tif', cv.IMREAD_GRAYSCALE)
        elif im == '5':
            break
        else:
           break
       
        while(True):
            print("Selecione a opção: 1: passa baixa, 2= passa alta, 3= passa faixa ou 4= sair")
            m = int(input())
            
            if(m ==1 ):
                plotarpassabaixa(im1)
            elif(m==2):
                plotarPassaAlta(im1)
            elif(m==3):
                plotarPassaFaixa(im1)
            else:
                break
        
if __name__ == "__main__":
    main()