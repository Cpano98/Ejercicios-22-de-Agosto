#Autor: Carlos Pano Hernandez - A01066264
#Descripcion: Escribe un programa que lee la longitud de los catetos de un triangulo rectangulo e imprime la longitud de la hipotenusa.

#Paso 1:
catetoA = float(input("Introduce la longitud de tu cateto A(cm):"))
catetoB = float(input("Introduce la longitud de tu cateto B(cm):"))

#Paso 2:
hipotenusa = (catetoA**2+catetoB**2)**0.5

#Paso 3:
print("La hipotenusa de tu Triangulo es igual a:", hipotenusa)

