from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


colunas = 612
linhas = 350

image_matrix = np.zeros((linhas, colunas), dtype=np.uint8)

print(image_matrix.shape)

image_matrix[50:300,50:100] = 255
image_matrix[250:300,100:150] = 255
image_matrix[50:300,200:250] = 255
image_matrix[50:100,250:300] = 255

image_matrix[50:100,300:350] = 255
image_matrix[100:200,300:350] = 255
image_matrix[200:250,250:300] = 255
image_matrix[250:300,300:350] = 255
image_matrix[150:200,250:300] = 255

image_matrix[50:100,400:550]=255
image_matrix[100:200,400:450]=255
image_matrix[150:200,450:550]=255
image_matrix[200:300,500:550]=255
image_matrix[250:300,400:500]=255


for i in range(200,250):
    for j in range(300,350):
        if  i+100>=j:
            print(i,j)
            image_matrix[i,j]=255  
            

image_matrix=255-image_matrix
#inverter valores da imagem (negativo)

plt.imshow(image_matrix, cmap='gray')
plt.show()



