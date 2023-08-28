from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy import asarray

def main():

    im = np.array(Image.open('cameraman.tif'))
    im2 = np.array(Image.open('house.tif'))
    im3 = np.array(Image.open('lena_gray_512.tif'))
    
    #recebendo as imagens

    im_neg = im.copy()
    im2_neg = im2.copy()
    im3_neg = im3.copy()
    #copiando as imagens para fazer o negativo as copias
    
    im_neg =255-im_neg
    im2_neg =255-im2_neg
    im3_neg =255-im3_neg
    #gerando o negativo
    
    im_dark = im.copy()
    im_dark = im_dark/2
    im2_dark = im2.copy()
    im2_dark = im2_dark/2
    im3_dark = im3.copy()
    im3_dark = im3_dark/2
    #copiando as imagens para fazer o escurecimento e escurecendo
    
    im_4qB = im.copy()
    im2_4qB = im2.copy()
    im3_4qB = im3.copy()
    #copiando as imagens para fazer os 4 quadrados brancos
    
    im_4qB[0:10,0:10] = 255
    im_4qB[0:10,-10:] = 255
    im_4qB[-10:,0:10] = 255
    im_4qB[-10:,-10:] = 255
    
    im2_4qB[0:10,0:10] = 255
    im2_4qB[0:10,-10:] = 255
    im2_4qB[-10:,0:10] = 255
    im2_4qB[-10:,-10:] = 255
    
    im3_4qB[0:10,0:10] = 255
    im3_4qB[0:10,-10:] = 255
    im3_4qB[-10:,0:10] = 255
    im3_4qB[-10:,-10:] = 255
    #fazendo os 4 quadrados brancos
    
    im_qP = im.copy()
    im2_qP = im2.copy()
    im3_qP = im3.copy()
    #copiando as imagens para fazer o quadrado preto
    
    c1 = im_qP.shape[1]
    c2 = im2_qP.shape[1]
    c3 = im3_qP.shape[1]
    l1 = im_qP.shape[0]
    l2 = im2_qP.shape[0]
    l3 = im3_qP.shape[0]
    #setando as variaveis para o tamanho das imagens
    
    l1 = l1//2
    l2 = l2//2
    l3 = l3//2
    c1 = c1//2
    c2 = c2//2
    c3 = c3//2
    #setando as variaveis para representarem o meio das imagens
    
    im_qP[l1-7:l1+7,c1-7:c1+7] = 0
    im2_qP[l2-7:l2+7,c2-7:c2+7] = 0
    im3_qP[l3-7:l3+7,c3-7:c3+7] = 0
    #fazendo o quadrado preto
    
    fig = plt.figure()
    plt1 = plt.subplot(5,3,1)
    plt2 = plt.subplot(5,3,2)
    plt3 = plt.subplot(5,3,3)
    plt4 = plt.subplot(5,3,4)
    plt5 = plt.subplot(5,3,5)
    plt6 = plt.subplot(5,3,6)
    plt7 = plt.subplot(5,3,7)
    plt8 = plt.subplot(5,3,8)
    plt9 = plt.subplot(5,3,9)
    plt10 = plt.subplot(5,3,10)
    plt11 = plt.subplot(5,3,11)
    plt12 = plt.subplot(5,3,12)
    plt13= plt.subplot(5,3,13)
    plt14 = plt.subplot(5,3,14)
    plt15 = plt.subplot(5,3,15)
    #criando o plot
    
    plt1.title.set_text('original')
    plt2.title.set_text('original')
    plt3.title.set_text('original')
    
    plt4.title.set_text('negativo')
    plt5.title.set_text('negativo')
    plt6.title.set_text('negativo')
    
    
    
    plt7.title.set_text('Escurecido')
    plt8.title.set_text('Escurecido')
    plt9.title.set_text('Escurecido')
    
    plt10.title.set_text('4 Q P')
    plt11.title.set_text('4 Q P')
    plt12.title.set_text('4 Q P')
    
    plt13.title.set_text(' Q P')
    plt14.title.set_text(' Q P')
    plt15.title.set_text(' Q P')
    #setando os titulos
    
    plt1.imshow(im, cmap='gray')
    plt2.imshow(im2, cmap='gray')
    plt3.imshow(im3,cmap= 'gray')
    
    plt4.imshow(im_neg, cmap='gray', vmin=0, vmax=255)
    plt5.imshow(im2_neg, cmap='gray', vmin=0, vmax=255)
    plt6.imshow(im3_neg, cmap='gray', vmin=0, vmax=255)
    
    plt7.imshow(im_dark, cmap='gray', vmin=0, vmax=255)
    plt8.imshow(im2_dark, cmap='gray', vmin=0, vmax=255)
    plt9.imshow(im3_dark, cmap='gray', vmin=0, vmax=255)
    
    plt10.imshow(im_4qB, cmap='gray', vmin=0, vmax=255)
    plt11.imshow(im2_4qB, cmap='gray', vmin=0, vmax=255)
    plt12.imshow(im3_4qB,cmap='gray', vmin=0, vmax=255)
    
    plt13.imshow(im_qP, cmap='gray', vmin=0, vmax=255)
    plt14.imshow(im2_qP, cmap='gray', vmin=0, vmax=255)
    plt15.imshow(im3_qP,cmap='gray', vmin=0, vmax=255)
    #plotando as imagens
    plt.show()
    
if __name__ == "__main__":
    main()



