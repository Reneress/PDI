from PIL import Image
import numpy as np

im = np.array(Image.open('lena_gray_512.tif'))

print(im.shape)

#acessando um pixel
# im[0,0]

#cessando todos os elementos :
# pegar todos os elementos da coluna 1
# im[:,0]
im[0:20,0:20] = 0
im[0:20,-20:] = 0
im[-20:,0:20] = 0
im[-20:,-20:] = 0
#utilização de -20: para determinar dos 20 pixeis finais até o final da imagem

print(im[200:210,:].shape)
#im[200:210,:] = 0

im_pil = Image.fromarray(im)
im_pil.show()
# im_pil.save('lena_alter.tif')