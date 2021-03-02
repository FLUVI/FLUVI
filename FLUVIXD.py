import os
import sys

os.system("clear")

def XD():
	os.system("cd sherlock","pip3 install -r requeriments.txt")
	print("requeriments sucesfully instaled!!!")

while True:
	print("Buenas mi pequeno skid que elegiras el dia de hoy?")
	opcion = input("\n-1. Instalar sherlock\n-2. Salir\n")

	if opcion == '1':
		XD()

	else:
		print("Saliendo...")
		sys.exit()
