import random
import time
import PySimpleGUI


def menu():
	print("""
		
			***Bienvenidos a sopa de letras***
			 1.¿Quieres jugar?
			 2.Salir
			 """)

	opcionmenu1 = int(input("elegir opcion: "))

	if opcionmenu1 == "2":
			print("Salir del programa")
			exit()

	elif opcionmenu1 == "1":
			print("Seleccione modo de juego")


def menu2():
	print('a- Sopa de letras con sustantivos')
	print('b- Sopa de letras con Adjetivos')
	print('c- Sopa de letras con verbos')

	opcionmenu2= input("Insertar una letra para elegir tema de juego")

	if opcionmenu2 == "a":
		print("""[["v", "e", "n", "t", "i", "l", "a", "d", "o", "r", "w", "f", "p"],
							 ["t", "p", "o", "q", "s", "i", "l", "l", "o", "n", "h", "p", "w"],
							 ["v", "j", "y", "v", "s", "a", "l", "v", "u", "n", "f", "y", "e"],
						 	 ["k", "a", "i", "ñ", "c", "o", "n", "t", "r", "o", "l", "p", "s"],
							 ["r", "p", "w", "e", "p", "l", "a", "z", "a", "j", "s", "i", "w"],
							 ["o", "o", "c", "a", "s", "a", "r", "z", "P", "e", "r", "r", "o"],								
							 ["z", "q", "c", "o", "c", "i", "n", "a", "e", "u", "k", "p", "s"],]""")
		inicio = time.time()
		while True:
			preg = input("Ingrese el Adjetivo que encontro:  ")
			if preg == "casa":
				print("La encontraste!. Segui así")
			elif preg == "perro":
				print("La encontraste!. Segui así")
			elif preg == "plaza":
				print("La encontraste!. Segui así")
			elif preg == "ventilador":
				print("La encontraste!. Segui así")
			elif preg == "COCINA":
				print("La encontraste!. Segui así")
			elif preg == "SILLON":
				print("La encontraste!. Segui así")
			elif preg == "MOUSE":
				print("La encontraste!. Segui así")
			elif preg == "termo":
				print("La encontraste!. Segui así")
			elif preg == "auto":
				print("La encontraste!. Segui así")
			elif preg == "mesa":
				print("La encontraste!. Segui así")
			elif preg == "control":
				print("La encontraste!. Segui así")
			elif preg == "celular":
				print("La encontraste!. Segui así")						
			else:
				print("La palabra no se encuentra en la sopa de letras, segui buscando")
				final = time.time()
				if final - inicio >= 200:
						print("")
						print("se te acabo el tiempo")

				elif opcionmenu2 == "b":
					print("""			 [["a", "m", "a", "b", "l", "e", "a", "r", "o", "i", "l", "n", "u", "e", "v", "o"],	
										  ["b", "s", "d", "ñ", "c", "k", "p", "d", "i", "v", "e", "r", "t", "i", "d", "o"],	
										  ["c", "t", "a", "l", "t", "o", "r", "q", "s", "c", "t", "s", "a", "a", "e", "q"],	
										  ["o", "s", "v", "w", "g", "i", "o", "p", "b", "a", "r", "v", "g", "s", "y", "e"],	
										  ["p", "g", "r", "a", "n", "d", "e", "i", "f", "l", "y", "ñ", "r", "o", "j", "o"],	
										  ["r", "p", "h", "e", "r", "m", "o", "s", "o", "h", "f", "l", "a", "c", "o", "w"],	
										  ["a", "o", "u", "d", "f", "g", "r", "z", "r", "s", "a", "d", "w", "g", "i", "r"],	
										  ["k", "f", "e", "o", "g", "x", "t", "a", "e", "u", "h", "c", "y", "r", "c", "l"],	
										  ["f", "e", "l", "i", "z", "u", "y", "p", "e", "q", "u", "e", "ñ", "o", "i", "u"],
										  ["q", "a", "l", "i", "m", "p", "i", "o", "t", "a", "w", "t", "r", "x", "z", "j"],]""")

					inicio= time.time()
					while True:
								preg = input("Ingrese el Adjetivo que encontro:  ")
								if preg == "AMABLE":
									print("La encontraste!. Segui así")
								elif preg == "nuevo":
									print("La encontraste!. Segui así")
								elif preg == "divertido":
									print("La encontraste!. Segui así")
								elif preg == "alto":
									print("La encontraste!. Segui así")
								elif preg == "grande":
									print("La encontraste!. Segui así")
								elif preg == "rojo":
									print("La encontraste!. Segui así")
								elif preg == "flaco":
									print("La encontraste!. Segui así")
								elif preg == "hermoso":
									print("La encontraste!. Segui así")
								elif preg == "feo":
									print("La encontraste!. Segui así")
								elif preg == "feliz":
									print("La encontraste!. Segui así")
								elif preg == "PEQUEÑO":
									print("la encontraste!. Segui así")
								elif preg == "limpio":
									print("la encontraste!. Segui así")							
								else:
									print("La palabra no se encuentra en la sopa de letras, segui buscando")
								final= time.time()
								if final - inicio >= 200:
									print("")
									print("se termino el tiempo")

				elif opcionmenu2 == "c":
					print("""			   [["a", "l", "i", "m", "p", "i", "a", "r", "o", "t", "q", "g", "f", "l", "k", "d"],
										  	["b", "x", "r", "u", "q", "a", "x", "c", "h", "l", "m", "i", "r", "a", "r", "ñ"],
							   			  	["c", "t", "e", "s", "t", "u", "d", "i", "a", "r", "j", "a", "e", "h", "i", "p"],
											["o", "s", "v", "w", "g", "i", "o", "p", "b", "s", "x", "ñ", "d", "k", "l", "u"],
											["w", "ñ", "a", "c", "p", "a", "t", "y", "z", "s", "a", "l", "t", "a", "r", "u"],
											["z", "l", "h", "a", "b", "l", "a", "r", "b", "j", "y", "u", "v", "n", "j", "i"],]""")

					inicio = time.time()
					while True:
							preg = input("Ingrese el Adjetivo que encontro:  ")
							if preg == "limpiar":
								print("La encontraste!. Segui así")
							elif preg == "mirar":
								print("La encontraste!. Segui así")
							elif preg == "estudiar":
								print("La encontraste!. Segui así")
							elif preg == "amar":
								print("La encontraste!. Segui así")
							elif preg == "jugar":
								print("La encontraste!. Segui así")
							elif preg == "cocinar":
								print("La encontraste!. Segui así")
							elif preg == "reir":
								print("La encontraste!. Segui así")
							elif preg == "dormir":
								print("La encontraste!. Segui así")
							elif preg == "saltar":
								print("La encontraste!. Segui así")
							elif preg == "hablar":
								print("La encontraste!. Segui así")
							elif preg == "correr":
								print("la encontraste!. Segui así")
							elif preg == "comer":
								print("la encontraste!. Segui así")	
							else:
								print("La palabra no se encuentra en la sopa de letras, segui buscando")
								final = time.time()
								if final - inicio >=200:
									print("")
									print("se te termino el tiempo")


								while op != "A" and op != "B" and op != "C":
									print ("Opcion incorrecta, ingrese una opcion valida")
								op = input("Ingrese una opción: ->  ")

	elif  opcionmenu2 == "2": #aquí es opcionmenu
		print("Saliste de la Sopa de Letras")
		print("Intentalo Pronto!!!!")

		exit()
#aqui debes si o si llamar a tus menus que definiste arriba
menu()
menu2()