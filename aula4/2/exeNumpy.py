from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    
    im = Image.open('lena_gray_512_salt_pepper.tif')
    im2 = Image.open('house.tif')
    im3 = Image.open('cameraman.tif')
    
    f_m2_nd = np.array(im2)
    f_m3_nd = np.array(im3)
    
    g_m2_nd = np.zeros(f_m2_nd.shape)#criar imagem de zeros do tamanho de f_m_nd
    g_m3_nd = np.zeros(f_m3_nd.shape)#criar imagem de zeros do tamanho de f_m_nd
    
    h_m2_nd = np.zeros(f_m2_nd.shape)#criar imagem de zeros do tamanho de f_m_nd
    h_m3_nd = np.zeros(f_m3_nd.shape)#criar imagem de zeros do tamanho de f_m_nd
    
    f_m_nd = np.array(im)
    g_m_nd = np.zeros(f_m_nd.shape)#criar imagem de zeros do tamanho de f_m_nd
    h_m_nd = np.zeros(f_m_nd.shape)#criar imagem de zeros do tamanho de f_m_nd
    #i_image_nd = np.zeros(f_m_nd.shape)#criar imagem de zeros do tamanho de f_m_nd
    #plt.imshow(f_m_nd, cmap='gray')
    #im.show()

    #Operação em vizinhança
    l = f_m_nd.shape[0]#recupera as linhas da imagem
    c = f_m_nd.shape[1]#recupera as colunas da imagem
    k = 1#tamanho do kernel 1 = 3x3, 2 = 5x5, 3 = 7x7, 4 = 9x9, 5 = 11x11
    
    l2 = f_m2_nd.shape[0]#recupera as linhas da imagem
    c2 = f_m2_nd.shape[1]#recupera as colunas da imagem
    
    l3 = f_m3_nd.shape[0]#recupera as linhas da imagem
    c3 = f_m3_nd.shape[1]#recupera as colunas da imagem
    
    for x in range(k, l2-k):
        for y in range(k, c2-k):
            s_xy = f_m2_nd[x-k:x+k+1, y-k:y+k+1]#recupera a vizinhança
            g_m2_nd[x,y] = np.mean(s_xy)#calcula a média da vizinhança e atribui ao pixel central
            h_m2_nd[x,y] = np.median(s_xy)#calcula a mediana da vizinhança e atribui ao pixel central
            #i_image_nd[x,y] = np.max(s_xy)#calcula o maximo da vizinhança e atribui ao pixel central
    
    for x in range(k, l3-k):
        for y in range(k, c3-k):
            s_xy = f_m3_nd[x-k:x+k+1, y-k:y+k+1]
            g_m3_nd[x,y] = np.mean(s_xy)
            h_m3_nd[x,y] = np.median(s_xy)
            
    
    for x in range(k, l-k):
        for y in range(k, c-k):
            s_xy = f_m_nd[x-k:x+k+1, y-k:y+k+1]#recupera a vizinhança
            g_m_nd[x,y] = np.mean(s_xy)#calcula a média da vizinhança e atribui ao pixel central
            h_m_nd[x,y] = np.median(s_xy)#calcula a mediana da vizinhança e atribui ao pixel central
            #i_image_nd[x,y] = np.max(s_xy)#calcula o maximo da vizinhança e atribui ao pixel central
    
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
    
    plt1.imshow(f_m_nd, cmap='gray')
    plt2.imshow(g_m_nd, cmap='gray', vmin=0, vmax=255)
    plt3.imshow(h_m_nd, cmap='gray', vmin=0, vmax=255)
    plt4.imshow(f_m2_nd, cmap='gray')
    plt5.imshow(g_m2_nd, cmap='gray', vmin=0, vmax=255)
    plt6.imshow(h_m2_nd, cmap='gray', vmin=0, vmax=255)
    plt7.imshow(f_m3_nd, cmap='gray')
    plt8.imshow(g_m3_nd, cmap='gray', vmin=0, vmax=255)
    plt9.imshow(h_m3_nd, cmap='gray', vmin=0, vmax=255)
    
    plt.show()
   

    
if __name__ == "__main__":
    main()
