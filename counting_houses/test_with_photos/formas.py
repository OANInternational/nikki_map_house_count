# Cargar OpenCV
import cv2
import argparse
import imutils
# Sirve para operar con cualquier dato numérico
import numpy as np


 
# Leer las imágenes que vamos a comparar
# Imagen sobre la que vamos a detectar si existe otra imagen
img_rgb = cv2.imread('casas3.png')

# Imagen que comprobamos si existe en la imagen Todo

template = cv2.imread('detm.png')
template2= cv2.imread('det.png')
template3= cv2.imread('det2.png')
template4= cv2.imread('detm2.png')
template5= cv2.imread('detm3.png')

imageList = []
imageList.append(template)
imageList.append(template2)
imageList.append(template3)
imageList.append(template4)
imageList.append(template5)


height, width, channels = template.shape
rotated = img_rgb

#select method
girarImagen = False

if(girarImagen == True):
    for angle in np.arange(0,360,15):
        rotated = imutils.rotate(img_rgb, angle)
        height, width, channels = rotated.shape
    
    

        # Tamaño de la imagen 1.jpg
        w, h = template.shape[:-1]
 
       # Función que sirve para detectar si una imagen está contenida en otra
        res = cv2.matchTemplate(rotated, template, cv2.TM_CCOEFF_NORMED)
 
     # Umbral admitido
        threshold = .7
 
        # Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):  #  Cambiar columnas y filas
            cv2.rectangle(rotated, pt, (pt[0] + w, pt[1] + h), (0, 0, 0), 1)
    
        cv2.imshow("rotation",rotated)
        cv2.waitKey(0)
    

if(girarImagen == False):
    for template in imageList:
        w, h = template.shape[:-1]
 
        # Función que sirve para detectar si una imagen está contenida en otra
        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
 
        # Umbral admitido
        threshold = .7
 
        # Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):  #  Cambiar columnas y filas
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 0), 1)

        cv2.imshow("imagen", img_rgb)
        cv2.waitKey(0)

 
# Guardar el resultado
#cv2.imwrite('result.png', img_rgb)


