import matplotlib.pyplot as plt
import imageio.v2 as imageio
import numpy as np
from PIL import Image
from imageio import imread
from scipy import ndimage
import numpy as np


def convolucao(im, k):
   
    
    return im

def main():
    print("Selecione a imagem: 1 , 2 ou 3")
    im = input()
    
    if im == '1':
        im1 = Image.open('lena_gray_512.tif')
    elif im == '2':
        im1 = Image.open('cameraman.tif')
    elif im == '3':
        im1 = Image.open('biel.png')
    else:
        im1 = Image.open('lena_gray_512.tif')
    
    
if __name__ == "__main__":
    main()
