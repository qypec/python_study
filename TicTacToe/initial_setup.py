def print_field():
	print("---------")
	print("|" + "".join(field[0]) +  "|")
	print("|" + "".join(field[1]) +  "|")
	print("|" + "".join(field[2]) +  "|")
	print("---------")

def make_a_move(coordinates):
	number_of_x = 0
	number_of_o = 0
	for i in range(3):
		for symb in field[i]:
			if symb == "X":
				number_of_x += 1
			if symb == "O":
				number_of_o += 1

	marker = "X"
	if number_of_x > number_of_o:
		marker = "O"
	field[3 - coordinates[1]][coordinates[0] - 1] = marker
	print_field()

	for i in range(3):
		vertical_column = [[symb for symb in field[j][i]] for j in range(3)]
		if field[i].count("X") == 3 or vertical_column.count("X") == 3:
			print("X wins")
			return 
		elif field[i].count("O") == 3 or vertical_column.count("O") == 3:
			print("O wins")
			return 
		elif field[0].count(' ') == 0 and field[1].count(' ') == 0 and field[2].count(' ') == 0:
			print("Draw")
			return
			
	print("Game not finished")

def error_processing(coordinates):
	if not coordinates:
		print("You should enter numbers!")
		return (False)
	elif (coordinates[0] > 3 or coordinates[0] < 1) or (coordinates[1] > 3 or coordinates[1] < 1):
		print("Coordinates should be from 1 to 3!")
		return (False)
	elif field[3 - coordinates[1]][coordinates[0] - 1] != ' ':
		print("This cell is occupied! Choose another one!")
		return (False)

	return (True)

field = str(input("Enter cells: "))
field = [[symb for symb in field[(i * 3):((i + 1) * 3)].replace('_', ' ')] for i in range(3)]
print_field()

end_of_game = None
while True:
	coordinates = input("Enter the coordinates: ").split()
	try:
		coordinates = [int(num) for num in coordinates if type(int(num)) == int]
	except ValueError:
		coordinates = []
	is_error = error_processing(coordinates)
	if is_error:
		break

make_a_move(coordinates)