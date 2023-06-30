#!/usr/bin/python3

# By: IsmaRG99

import sys
import os

# System call
os.system("")

# Clase para estilos de colores
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'




print(style.CYAN + "----------- COMIENZA EL TEST ------------\n" + style.RESET)

i = 1
tema = input("Introducir número del tema: ")
archivo ="test" + tema + ".txt"

num_quest = int(input("Introducir número de preguntas totales: "))

# Comprobación del archivo -> print (archivo)
# Comprobación del numero de preguntas totales -> print(num_quest)

with open(archivo, 'a') as test_file:
	while (i <= num_quest):
		q = input("[" + str(i) +"]: ")
		test_file.write("[" + str(i) + "]: " + q + "\n")
		i = i + 1

print(style.CYAN + "----------- CORRIGE EL TEST ------------\n" + style.RESET)

i = 1

with open(archivo, 'r') as test_file:
	lines = test_file.readlines()
	while (i <= num_quest):
		for index, line in enumerate(lines):
			print ("\nLa respuesta a a la pregunta: " + line)
			r = input("Es correcta? (s/n): ")
			lines[index] = line.strip() + "\n" + "Solucion: " + r + "\n"
			i = i + 1
with open(archivo, 'w') as test_file:
	for line in lines:
		test_file.write(line)

print(style.CYAN + "\n----------- RESULTADOS ------------\n" + style.RESET)

with open(archivo, 'r') as test_file:
	checkacierto = 's'
	aciertos = 0
	for line in lines:
		if line.find(checkacierto) != -1:
			aciertos += 1
	print(style.GREEN + str(aciertos) + style.RESET, "aciertos y", style.RED + str(len(lines)-aciertos) + style.RESET, "fallos \n")
total = (aciertos / len(lines)) * 100
if total >= 70:
	print(style.GREEN + "APROBADO\n" + style.RESET)
	print("Porcentaje obtenido: ", style.GREEN + str(total) + style.RESET, "%\n")
	with open(archivo, 'a') as test_file:
		test_file.write(style.CYAN + "\n------- RESULTADOS -------\n" + style.RESET)
		test_file.write(style.GREEN + "APROBADO\n" + style.RESET)
		test_file.write("Porcentaje obtenido: " + style.GREEN + str(total) + style.RESET + "%\n")
else:
	print(style.RED + "SUSPENSO\n" + style.RESET)
	print("Porcentaje obtenido: ", style.RED + str(total) + style.RESET, "%\n")
	with open(archivo, 'a') as test_file:
		test_file.write(style.CYAN + "\n------- RESULTADOS -------\n" + style.RESET)
		test_file.write(style.RED + "SUSPENSO\n" + style.RESET)
		test_file.write("Porcentaje obtenido: " + style.RED + str(total) + style.RESET + "%\n")



