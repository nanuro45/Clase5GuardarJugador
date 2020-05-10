import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json #Utilizo Json por una mayor comidad a la hora de trabajar con archivos, me parece mucho mas facil de usar. 


archivo = 'Guardado.txt'

Dik={}# en mi caso voy a utilizar un diccionario donde las claves sean los jugadores y dentro de los elementos contenga un diccionario con los juegos jugados y la cantidad de veces que lo jugo 
with open(archivo,'w')as f:
    json.dump(Dik,f)

def Guardar_juego(archivo,jugador,juego):
	with open(archivo,'r') as j: #abro el archivo en modo lectura para saber que contiene el archivo
		Dik=json.load(j) #Cargo lo que tiene el archivo en el diccionario
		if jugador in Dik.keys(): #verifico si el jugador esta en el diccionario
			 i=Dik[jugador] #Paso lo que tiene el diccionario en la posicion del jugador a una variable auxiliar
			 if juego in i.keys(): #verifico si el juego ya fue jugado 
				 i[juego]=i[juego]+1 #aumento en uno la cantidad de veces que se jugo
			 else:
			     i.setdefault(juego,1)#en caso de no haber jugado al juego anteriormente se crea el una posicion del diccionario y con la cantidad de veces jugadas en 1 para avisar que ya jugo
		else:
			dic_a={juego:1} #en caso de que no exista ya el jugador , utilizo una variable auxiliar para cargar el juego y la cantidad de veces que jugo
			Dik.setdefault(jugador,dic_a)#agrego un elemento al diccionario con el jugador, el juego que jugo y la cantidad de veces que lo jugo		
	with open(archivo,'w') as j:
		json.dump(Dik,j) #se utiliza esta instruccion para almacenar lo que contiene el diccionario en el archivo TXT
		print (Dik) #de uso opcional debido a que muestra el diccionario completo		
	
			
	
def main(args):
	sg.theme('DarkBlue')
		
	opcion = ['Ahorcado','Ta-Te-TI','Otello']

	layout = [[sg.Text('Ingrese Nombre Del Jugador',size=(15,2))],[sg.Input(key='jugador')],
			  [sg.Text('Juegos Disponibles: ')],
			  [sg.Listbox(opcion,size=(30,10),key='opcion')],
			  [sg.Button('SALIR'),sg.Button('OK')]]	

	window = sg.Window('Catalogo De Juegos ',layout)
	
	sigo_jugando = True
	
	while sigo_jugando:
		
		event, values = window.read()

		if event == 'SALIR':
			break	
		if event == 'OK':
			jugador=values['jugador']
			juego=values['opcion']
			if juego[0] == 'Ahorcado' :
				hangman.main()
			elif juego[0] == 'Ta-Te-TI':
				tictactoeModificado.main()
			elif juego[0] == 'Otello':
				reversegam.main()
			Guardar_juego(archivo,jugador,juego[0])
	window.close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
	
