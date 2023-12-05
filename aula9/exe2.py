import cv2 as cv
import numpy as np

kernel_laplaciano = np.array([[1, 1, 1],	[1, -4, 1],	[1, 1, 1]],dtype="int")

kernel_laplacian_large = np.array([[1, 1, 1, 1, 1],	[1, 1, 1, 1, 1],	[1, 1, -24, 1, 1],	[1, 1, 1, 1, 1],	[1, 1, 1, 1, 1]],dtype="int")

def detectarpontos(im):
    
    iml = cv.Laplacian(im,cv.CV_8U,ksize=5)
    imlA = np.abs(iml)
    
    T = 0.9*np.max(imlA)
    
    print(T)
    
    pontos = np.where(imlA>0,0,255).astype('uint8')
    
    print(np.where(pontos>0))
    

    
    cv.imshow('Original', im)
    cv.imshow('Laplaciano ', iml)
    cv.imshow('Pontos detectados', pontos)
   
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    
def canny(im,t1,t2):
    imc = cv.Canny(im,threshold1=t1, threshold2=t2, apertureSize = 3)
    return imc

def limiarizacao(im):
        # global thresholding
    im_blur = cv.GaussianBlur(im, (5,5), 0)
    ret,th = cv.threshold(im_blur,127,255,cv.THRESH_BINARY) 
    
    cv.imshow('Original', im)
    cv.imshow('Global threshold', th) 
    cv.waitKey(0) 
    cv.destroyAllWindows()

def main():
    # Crie uma imagem em branco (255 é branco em escala de cinza)
    # imagem = np.ones((500, 500), np.uint8) * 255

    # # Defina a cor dos pontos como preto
    # cor_ponto = 1

    # # Crie pontos pretos na imagem
    # for _ in range(1000):
    #     # Gere coordenadas aleatórias para os pontos
    #     x = np.random.randint(1, imagem.shape[1])
    #     y = np.random.randint(1, imagem.shape[1])
        
    #     # Desenhe o ponto na imagem
    #     cv.circle(imagem, (x, y), 2, cor_ponto, -1)
   
    # # Exiba a image
    
    
    # detectarpontos(imagem)
    
    # img = cv.imread('fingerprint.tif')
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # limiarizacao(img)
    
    im = cv.imread('biel.png')
    im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    im_blur = cv.GaussianBlur(im_gray, (3,3), 1)
    
    cv.imshow('Original', im)
    
    imc = canny(im_gray,50,150)
    cv.imshow('Canny Edge Detection', imc)
   
    imc2 = canny(im_blur,50,150)
    cv.imshow('Canny Edge Detection with Blur', imc2)
    
    cv.waitKey(0)
    
    cv.destroyAllWindows()
    
    while(True):
        t1 = int(input("Digite o valor de t1: "))
        t2 = int(input("Digite o valor de t2: "))
        
        if(t1 == 0 or t2 == 0):
            break
        else:
            imc3 = canny(im_blur,t1,t2)
            cv.imshow('Canny Edge Detection with Blur and T1, T2', imc3)
            cv.waitKey(0)
            cv.destroyAllWindows()
    
if __name__ == "__main__":
    main()