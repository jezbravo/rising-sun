# la máquina jugará utilizando las 'X's;
# el usuario (por ejemplo, usted) jugará utilizando las 'O's;
# el primer movimiento es de la máquina - siempre coloca una 'X' en el centro del tablero;
# todos los cuadros están numerados comenzando con el 1.
# el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser válido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
# el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, usted gana, o la máquina gana;
# la máquina responde con su movimiento y se verifica el estado del juego;
# no se debe implementar algún tipo de inteligencia artificial - la máquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

from random import randrange

def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def enter_move(board):
	ok = False	# suposición falsa - necesaria para entrar en el bucle
	while not ok:
		move = input("Ingrese su jugada: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9'
		if not ok:
			print("Jugada errónea, ingrésala nuevamente")
			continue
		move = int(move) - 1 	# número de la celda, del 0 al 8
		row = move // 3 	# fila de la celda
		col = move % 3		# columna de la celda
		sign = board[row][col]	# marca el cuadro elegido
		ok = sign not in ['O','X'] 
		if not ok:	# está ocupado, ingrese una posición nuevamente
			print("¡Cuadro ocupado, ingrese otro valor!")
			continue
	board[row][col] = 'O' 	# colocar '0' al cuadro seleccionado

def make_list_of_free_fields(board):
	free = []	# la lista está vacía inicialmente
	for row in range(3): # itera a través de las filas
		for col in range(3): # iitera a través de las columnas
			if board[row][col] not in ['O','X']: # ¿Está la celda libre?
				free.append((row,col)) # sí, agrega una nueva tupla a la lista
	return free

def victory_for(board,sgn):
	if sgn == "X":	# ¿Estamos buscando X?
		who = 'me'	# Si, es la maquina
	elif sgn == "O": # ... ¿o estamos buscando O?
		who = 'you'	# Si, es el usuario
	else:
		who = None	# No se debe caer aquí.
	cross1 = cross2 = True  # para las diagonales
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # revisar la primera diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # revisar la segunda diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None

def draw_move(board):
	free = make_list_of_free_fields(board) # crea una lista de los cuadros vacios o libres
	cnt = len(free)
	if cnt > 0:	# si la lista no esta vacía, elegir un lugar para 'X' y colocarla
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crear un tablero vacío
board[1][1] = 'X' # colocar la primera 'X' en el centro
free = make_list_of_free_fields(board)
human_turn = True # ¿De quien es turno ahora?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("¡Ganaste!")
elif victor == 'me':
	print("¡Gané!")
else:
	print("¡Empate!")