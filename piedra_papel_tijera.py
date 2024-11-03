import random
import time


opcion1 = "piedra"
opcion2 = "papel"
opcion3 = "tijera"
lista_de_opciones = [opcion1, opcion2, opcion3]
contador_ronda = 0
contador_victorias_jugador1 = 0
contador_victorias_jugador2 = 0
contador_victoria_maquina = 0
contador_empates = 0
opciones_modo_juego = ["1","2"]
opciones_salida = ["s","n"]


def mostrar_victorias(contador_ronda,contador_victorias_jugador1,contador_victorias_jugador2, contador_victoria_maquina, contador_empates):

	print(f"\nSe han jugado un total de {contador_ronda} rondas.")
	print(f"\nEl jugador 1 ha ganado {contador_victorias_jugador1} rondas.")
	print(f"El jugador 2 ha ganado {contador_victorias_jugador2} rondas.")
	print(f"La máquina ha ganado {contador_victoria_maquina} rondas.")
	print(f"El total de empates es {contador_empates}.")


nombre_usuario = input("Hola, ¿cuál es tu nombre?: ")
print("\nBienvenido(a) a nuestro juego de piedra, papel o tijera,", nombre_usuario, ":)")


while True:

	try:
		
		eleccion_modo_juego = input("\nEscoge si deseas jugar contra la máquina u otro usuario. Ingresa 1 para máquina y 2 para otro usuario: ")
		
		if eleccion_modo_juego not in opciones_modo_juego:
			raise TypeError("Ups! Solo puedes ingresar las opciones mencionadas para el modo de juego")


		jugador1 = input("\nEs el turno del jugador 1, escoge: piedra, papel o tijera: ").lower()


		if eleccion_modo_juego == "1":
			print("La máquina está eligiendo")
			time.sleep(3)
			jugador2 = random.choice(lista_de_opciones)
			print(f"La máquina eligió: {jugador2}")


		elif eleccion_modo_juego == "2":
			jugador2 = input("\nEs el turno del jugador 2, escoge: piedra, papel o tijera: ").lower()


		if jugador1 not in lista_de_opciones and jugador2 not in lista_de_opciones:
			raise ValueError("Ups! Solo puedes ingresar las opciones mencionadas")


		if jugador1 == opcion1 and jugador2	== opcion3:
			print("\n¡Felicitaciones! Jugador 1 gana")
			contador_ronda += 1
			contador_victorias_jugador1 +=1
			mostrar_victorias(contador_ronda,contador_victorias_jugador1,contador_victorias_jugador2, contador_victoria_maquina, contador_empates)


		elif jugador1 == opcion1 and jugador2 == opcion2:
			if eleccion_modo_juego == "2": 
				print("\n¡Felicitaciones! Jugador 2 gana")
				contador_victorias_jugador2 +=1
			elif eleccion_modo_juego == "1":
				print("Ha ganado la máquina")
				contador_victoria_maquina += 1
			contador_ronda += 1
			mostrar_victorias(contador_ronda,contador_victorias_jugador1,contador_victorias_jugador2, contador_victoria_maquina, contador_empates)


		elif jugador1 == opcion2 and jugador2 == opcion3:
			if eleccion_modo_juego == "2": 
				print("\n¡Felicitaciones! Jugador 2 gana")
				contador_victorias_jugador2 +=1
			elif eleccion_modo_juego == "1":
				print("Ha ganado la máquina")
				contador_victoria_maquina += 1
			contador_ronda += 1
			mostrar_victorias(contador_ronda,contador_victorias_jugador1,contador_victorias_jugador2, contador_victoria_maquina, contador_empates)


		elif jugador1 == opcion2 and jugador2 == opcion1:
			print("\n¡Felicitaciones! Jugador 1 gana")
			contador_ronda += 1
			contador_victorias_jugador1 +=1
			mostrar_victorias(contador_ronda,contador_victorias_jugador1,contador_victorias_jugador2, contador_victoria_maquina, contador_empates)


		elif jugador1 == opcion3 and jugador2 == opcion2:
			print("\n¡Felicitaciones! Jugador 1 gana")
			contador_ronda += 1
			contador_victorias_jugador1 +=1
			mostrar_victorias(contador_ronda,contador_victorias_jugador1,contador_victorias_jugador2, contador_victoria_maquina, contador_empates)


		elif jugador1 == opcion3 and jugador2 == opcion1:
			if eleccion_modo_juego == "2": 
				print("\n¡Felicitaciones! Jugador 2 gana")
				contador_victorias_jugador2 += 1
			elif eleccion_modo_juego == "1":
				print("Ha ganado la máquina")
				contador_victoria_maquina += 1
			contador_ronda += 1
			mostrar_victorias(contador_ronda,contador_victorias_jugador1,contador_victorias_jugador2, contador_victoria_maquina, contador_empates)


		elif jugador1 == jugador2:
			print("\nEmpate")
			contador_ronda += 1
			contador_empates += 1
			mostrar_victorias(contador_ronda,contador_victorias_jugador1,contador_victorias_jugador2, contador_victoria_maquina, contador_empates)
				

		jugar_de_nuevo = input("\n¿Deseas volver a jugar? Ingresa S para sí o N para no: ").lower()

		if jugar_de_nuevo == "s":
			print("\nHas seleccionado la opción para seguir jugando")

		elif jugar_de_nuevo == "n":
			print("\nHas seleccionado la opción para salir del sistema. Muchas gracias por usar nuestro programa :)")
			break

		else:
			print("\nOpción no válida")
			jugar_de_nuevo = input("\n¿Deseas volver a jugar? Ingresa S para sí o N para no: ").lower()


	except TypeError as error:
		print(error)

	except ValueError as error:
		print(error)