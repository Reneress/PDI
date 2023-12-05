import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from PIL import Image
from mpl_toolkits import mplot3d

#elementos estruturantes
A = cv.getStructuringElement(cv.MORPH_CROSS,(40,40))
# A = cruz 3x3
B= cv.getStructuringElement(cv.MORPH_RECT,(3,3))
# B = retangulo 3x3
C = cv.getStructuringElement(cv.MORPH_RECT,(1,7))
#C = retangulo 7x1
D = cv.getStructuringElement(cv.MORPH_ELLIPSE,(20,20))
#D = elipse 7x7
    
def erosao(img, elem, V):
    
    if(len(img.shape) == 3):
         img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    elem = cv.getStructuringElement(cv.MORPH_CROSS,(V,V))
    imd = cv.erode(img, elem, iterations = 1)
    
    return imd
    
def dilatacao(img, elem,V):
    if(len(img.shape) == 3):
         img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
         
    elem = cv.getStructuringElement(cv.MORPH_CROSS,(V,V))
    imd = cv.dilate(img, elem, iterations = 1)
    
    return imd
    
    
def abertura(img,elem,V):
    im = erosao(img, elem,V)
    imf = dilatacao(im, elem,V)
    return imf

def fechamento(img,elem,V):   
        im = dilatacao(img, elem,V)
        imf = erosao(im, elem,V)
        
        return imf
def borda (img, elem,V):
    im = erosao(img, elem,V)
    b = img - im
    
    return b
    
def plotar (img, elem):
    
    plt.subplot(161),plt.imshow(img, cmap = 'gray')
    plt.title('Original')
    plt.subplot(162),plt.imshow(elem, cmap = 'gray')
    plt.title('Estrutura')
    plt.subplot(163),plt.imshow(erosao(img,elem), cmap = 'gray')
    plt.title('Erosão')
    plt.subplot(164),plt.imshow(dilatacao(img,elem), cmap = 'gray')
    plt.title('Dilatação')
    plt.subplot(165),plt.imshow(abertura(img,elem), cmap = 'gray')
    plt.title('Abertura')
    plt.subplot(166),plt.imshow(fechamento(img,elem), cmap = 'gray')
    plt.title('Fechamento')
    
    plt.show()
    
def main():

    
    while(True):
    
        print("Digite o nome da imagem: A, B, C, D, E, F, G, H,  0 = sair")
        input_img = input()
        
        if(input_img == '0'):
            break
        elif(input_img == 'A'):
            img = cv.imread('fingerprint.tif',0)
            cv.imshow('fingerprint',img)
        elif(input_img == 'B'):
            img = cv.imread('imagem1.tif',0)
        elif(input_img == 'C'):
            img = cv.imread('imagem2.tif',0)
        elif(input_img == 'D'):
            img = cv.imread('morfologia1.tif',0)
        elif(input_img == 'E'):
            img = cv.imread('morfologia2.tif',0)
        elif(input_img == 'F'):
            img = cv.imread('noise_rectangle.tif',0)
        elif(input_img == 'G'):
            img = cv.imread('text_gaps.tif',0)
        elif(input_img == 'H'):
            img = cv.imread('rosto_perfil.tif',0)
        else:
            break
        
        
        ima = img.copy()
        
        while(True):
            print("Digite a operação, 1 = erosão, 2 = dilatação, 3 = abertura, 4 = fechamento, 5 = borda, 6 = sair")
            elem = input()
            print("Digite o valor do elemento")
            V = int(input())
            
            if(elem == '6'):
                break
            elif(elem == '1'):
                ima = erosao(ima,A,V)
                cv.imshow('original',img)
                cv.imshow('erosao',ima)
                cv.waitKey(0)
                cv.destroyAllWindows()
            elif(elem == '2'):
                ima = dilatacao(ima,A,V)
                cv.imshow('original',img)
                cv.imshow('dilatacao',ima)
                cv.waitKey(0)
                cv.destroyAllWindows()
            elif(elem == '3'):
                ima = abertura(ima,A,V)
                cv.imshow('original',img)
                cv.imshow('abertura',ima)
                cv.waitKey(0)
                cv.destroyAllWindows()
            elif(elem == '4'):
                ima = fechamento(ima,A,V)
                cv.imshow('original',img)
                cv.imshow('fechamento',ima)
                cv.waitKey(0)
                cv.destroyAllWindows()
            elif(elem == '5'):
                b = borda(img,A,V)
                cv.imshow('original',img)
                cv.imshow('borda',b)
                cv.waitKey(0)
                cv.destroyAllWindows()
            else:
                break
            
     
         
if __name__ == "__main__":
    main()