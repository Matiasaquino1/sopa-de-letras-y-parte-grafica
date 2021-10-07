import PySimpleGUI as sg



portada= "portada.png"
exit= "exit.png"
imagen2 = ["verbos.png","sustantivos.png","adjetivos.png"]



reset = False
output = 0




layout = [[sg.Text("***SOPA DE LETRAS HECHA POR MATIAS***")],
		   [sg.Button(key="-OUTPUT-", image_filename= portada), 
		   sg.Button("JUGAR", size=(40, 15), key="-JUGAR-"),
		   sg.Button(key="-EXIT-", image_filename= exit)],
		   [sg.InputText(key="-TEXT-", size=(50, 20)), 
		   ]]

window = sg.Window("Sopa de Letras", layout=layout)

while True:

	event, values = window.read()

	if event == sg.WIN_CLOSED:
		break
		
	if event == "-EXIT-":
			exit()
	elif event == "-OUTPUT-":
		if not reset:
			output = (output + 1) % 3
			window["-OUTPUT-"].update(image_filename=imagen2[output])
			window["-JUGAR-"].update("Escribe la palabra que encontraste", button_color=("White", "Blue"))

	elif event == "-JUGAR-":
		if output == 0 or output == 1 or output == 2:
			
			if event == "-JUGAR-" and values["-TEXT-"] == "casa":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "perro":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "plaza":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "ventilador":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "cocina":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "sillon":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "mouse":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "termo":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "auto":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "mesa":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "control":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "celular":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "amable":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "nuevo":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "divertido":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "alto":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "grande":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "flaco":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "feo":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "rojo":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "hermoso":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "feliz":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "pequeño":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "limpio":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "limpiar":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "mirar":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "estudiar":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "amar":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "jugar":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "cocinar":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "reir":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "dormir":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "saltar":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "hablar":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "correr":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))
			elif event == "-JUGAR-" and values["-TEXT-"] == "comer":
				window["-JUGAR-"].update("CORRECTO", button_color=("blue", "green"))																							
			
			else:
				window["-JUGAR-"].update("INCORRECTO", button_color=("blue", "red"))	


window.close()