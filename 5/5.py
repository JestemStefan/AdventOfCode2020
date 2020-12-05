import cProfile as cp

def main():
	with open("5/Input.txt") as input_file:
		
		directions = []

		for line in input_file.readlines():

			 line = line.strip()
			 row_position = line[:-3]
			 seat_position = line[-3:]

			 directions.append([row_position, seat_position])
		

		row_ID = []
		for i in range(128):
			row_ID.append(i)

		seat_ID = []
		for j in range(8):
			seat_ID.append(j)


		ID_list = []

		for input in directions:
			calculated_ID = get_row_ID(input[0], row_ID) * 8 + get_seat_number(input[1], seat_ID)
			ID_list.append(calculated_ID)
		
		ID_list = sorted(ID_list)

		answer = search_missing_ID(ID_list)
		print(answer)

		
		
def get_row_ID(row_pos, row_ID):

	ID = row_ID

	for letter in row_pos:
		half = len(ID)//2

		lower_half = ID[:half]
		upper_half = ID[-half:]

		if letter == "F":
			ID = lower_half

		else:
			ID = upper_half

	return ID[0]

def get_seat_number(seat_dir, seat_ID):

	ID = seat_ID

	for letter in seat_dir:
		half = len(ID)//2

		lower_half = ID[:half]
		upper_half = ID[-half:]

		if letter == "L":
			ID = lower_half

		else:
			ID = upper_half

	return ID[0]


def search_missing_ID(ID_list):

	for i, id in enumerate(ID_list):
		if i == 0:
			pass

		else:

			if (id - 1) == ID_list[i-1]:
				pass
				
			else:
				return (id - 1)


#main()
cp.run("main()")