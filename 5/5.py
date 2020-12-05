def main():
	with open("5/Input.txt") as input_file:
		
		# clean each line
		for line in input_file.readlines():
			 print(line.strip())


main()