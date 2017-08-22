#Autor: Carlos Pano Hernandez - A01066264
#Descripcion: El IMC (indice de masa corporal) es un numero que relaciona el peso y la estatura de una persona. Escribe un programa que lee el peso en kg. y la estatura en metros e imprime el IMC.

#Paso 1:
peso = float(input("Introduce tu peso (Kg):"))
estatura = float(input("Introduce tu estatura(m):"))

#Paso 2:
imc = peso/(estatura**2)

#Paso 3:

print("Tu IMC es de:", imc)