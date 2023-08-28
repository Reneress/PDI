from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    
    print("hello world")
    im = Image.open('lena_gray_512_salt_pepper.tif')
    f_image_nd = np.array(im)
    g_image_nd = np.zeros(f_image_nd.shape)#criar imagem de zeros do tamanho de f_image_nd
    h_image_nd = np.zeros(f_image_nd.shape)#criar imagem de zeros do tamanho de f_image_nd
    #i_image_nd = np.zeros(f_image_nd.shape)#criar imagem de zeros do tamanho de f_image_nd
    #plt.imshow(f_image_nd, cmap='gray')
    #im.show()

    #Operação em vizinhança
    l = f_image_nd.shape[0]#recupera as linhas da imagem
    c = f_image_nd.shape[1]#recupera as colunas da imagem
    k = 1#tamanho do kernel 1 = 3x3, 2 = 5x5, 3 = 7x7, 4 = 9x9, 5 = 11x11
      
    
    for x in range(k, l-k):
        for y in range(k, c-k):
            s_xy = f_image_nd[x-k:x+k+1, y-k:y+k+1]#recupera a vizinhança
            g_image_nd[x,y] = np.mean(s_xy)#calcula a média da vizinhança e atribui ao pixel central
            h_image_nd[x,y] = np.median(s_xy)#calcula a mediana da vizinhança e atribui ao pixel central
            #i_image_nd[x,y] = np.max(s_xy)#calcula o maximo da vizinhança e atribui ao pixel central
    
    #create two colums plot
    fig = plt.figure()
    plt1 = plt.subplot(1,3,1)
    plt2 = plt.subplot(1,3,2)
    plt3 = plt.subplot(1,3,3)
    #plt4 = plt.subplot(2,2,4)
    plt1.title.set_text('original')
    plt2.title.set_text('mean filter')
    plt3.title.set_text('median filter')
    #plt4.title.set_text('max filter')
    
    plt1.imshow(f_image_nd, cmap='gray')
    plt2.imshow(g_image_nd, cmap='gray', vmin=0, vmax=255)
    plt3.imshow(h_image_nd, cmap='gray', vmin=0, vmax=255)
    #plt4.imshow(i_image_nd, cmap='gray', vmin=0, vmax=255)
    
    plt.show()
   

    
if __name__ == "__main__":
    main()
