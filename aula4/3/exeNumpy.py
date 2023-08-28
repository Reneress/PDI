from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def rotate(image, angle):
    an = angle * np.pi / 180

    # Calculando a matriz de transformação de rotação
    cos_angle = np.cos(an)
    sin_angle = np.sin(an)
    rotation_matrix = np.array([[cos_angle, -sin_angle], [sin_angle, cos_angle]])

    # Calculando as coordenadas dos pixels rotacionados
    x, y = np.meshgrid(range(image.shape[1]), range(image.shape[0]))
    coordinates = np.vstack([x.ravel(), y.ravel()])
    rotated_coordinates = np.dot(rotation_matrix, coordinates).astype(int)

    # Criando um array para armazenar a imagem rotacionada
    imRotate = np.zeros_like(image)

    # Copiando os pixels da imagem original para a imagem rotacionada
    for i in range(coordinates.shape[1]):
        x, y = coordinates[:, i]
        new_x, new_y = rotated_coordinates[:, i]
        if 0 <= new_x < imRotate.shape[1] and 0 <= new_y < imRotate.shape[0]:
            imRotate[new_y, new_x] = image[y, x]
            
    return imRotate

def tamanho(imagem, fator):
        
    # Calculando o novo tamanho da imagem
    new_shape = tuple(int(dim * fator) for dim in imagem.shape)

    # Criando um array para armazenar a imagem reduzida
    image_alterada = np.zeros(new_shape)

    # Selecionando uma submatriz da imagem
    x_ratio = imagem.shape[0] / new_shape[0]
    y_ratio = imagem.shape[1] / new_shape[1]
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            image_alterada[i, j] = imagem[int(i * x_ratio), int(j * y_ratio)]

    return image_alterada

def translacao(image, x, y):
    
    # Definindo o deslocamento da translação
    x_trava = x
    y_trava = y

    # Criando um array para armazenar a imagem transladada
    imTras = np.zeros_like(image)

    # Copiando os pixels da imagem original para a imagem transladada
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            new_i = i + y_trava
            new_j = j + x_trava
            if 0 <= new_i < image.shape[0] and 0 <= new_j < image.shape[1]:
                imTras[new_i, new_j] = image[i, j]
    
    return imTras

def main():
    
    im = np.array(Image.open('lena_gray_512.tif'))
    im2 = np.array(Image.open('house.tif'))
    im3 = np.array(Image.open('cameraman.tif'))
    
    imR = tamanho(im, 0.85)
    imR2 = tamanho(im2, 0.85)
    imR3 = tamanho(im3, 0.85)
    
    imA = tamanho(im, 1.25)
    imA2 = tamanho(im2, 1.25)
    imA3 = tamanho(im3, 1.25)
            
    imRot90 = np.rot90(im, 1)
    im2Rot90 = np.rot90(im2, 1)
    im3Rot90 = np.rot90(im3, 1)
    
    imRot45 = rotate(im, 45)
    im2Rot45 = rotate(im2, 45)
    im3Rot45 = rotate(im3, 45)
    
    imRot100= rotate(im, 100)
    im2Rot100 = rotate(im2, 100)
    im3Rot100 = rotate(im3, 100)
    
    imTras = translacao(im, 50, 50)
    im2Tras = translacao(im2, 50, 50)
    im3Tras = translacao(im3, 50, 50)
    
    imTras3545 = translacao(im, 35, 45)
    im2Tras3545 = translacao(im2, 35, 45)
    im3Tras3545 = translacao(im3, 35, 45)
    
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
