#!/usr/bin/env python3
#1157px = 10 cm con una resolucion de 300 ppp
from PIL import Image
dies_cm = 1157
imagen = Image.open("0.png")
imagen_nueva = None

#toma:
#tamaño final(el tamaño que queremos como resultado)
#tamaño cambiar (el tamaño que nos interesa que se modifique a tal tamaño)
#tamaño scalable (tamaño que nos interesa que se modifique proporcional mente)
def proporcion (tamaño_final,tamaño_cambiar,tamaño_scalable):
   return  int((tamaño_scalable * tamaño_final) / tamaño_cambiar)

#toma la imagen a modificar y el tamaño deciado
#y lo redimenciona y guarda
def redimencionado(image,tamaño):
    ancho, alto = imagen.size
    if ancho > alto:
        imagen_nueva = imagen.resize(
					(tamaño,
					proporcion(tamaño,ancho,alto))
					)
        imagen_nueva.save("redimencionado.png","png")

    else:
        imagen_nueva = imagen.resize(
					(proporcion(tamaño,alto,ancho),
					tamaño)
					)
        imagen_nueva.save("redimencionado.png","png")


redimencionado(imagen,dies_cm)
