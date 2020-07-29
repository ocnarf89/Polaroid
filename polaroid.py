#1157px = 10 cm con una resolucion de 300 ppp
from PIL import Image
dies_cm = 1157 
imagen = Image.open("1.png")
imagen_nueva = None
ancho, alto = imagen.size

def proporcion(tamaño_final,tamaño_cambiar,tamaño_scalable):
   return  int((tamaño_scalable * tamaño_final) / tamaño_cambiar)
   #return imagen.resize((dies_cm,int(proporcional)))

def redimencionado(image,):
   if ancho > alto:
      imagen_nueva = imagen.resize(
					(dies_cm,
					proporcion(dies_cm,ancho,alto))
					)
      imagen_nueva.save("redimencionado.png","png")

   else:
      imagen_nueva = imagen.resize(
					(proporcion(dies_cm,alto,ancho),
					dies_cm)
					)
      imagen_nueva.save("redimencionado.png","png")

   


  

