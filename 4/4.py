import cProfile as cp


def main():

	valid_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
	valid_keys = sorted(valid_keys)

	optional_key = "cid"
	
	
	processed_input = []


	with open("4/Input.txt") as input_file:
		
		# prepare empty dict
		 batch_dict = {}

		# clean each line
		 for line in input_file.readlines():
			 line = line.strip()
			
			# if line is empty then end batch
			 if line == "":
				 processed_input.append(batch_dict)
				 batch_dict = {}
			
			# if line is not empty then read data to batch
			 else:
				 split_line = line.split()

				 for field in split_line:
					 dict_pair = field.split(":")

					 key = dict_pair[0]
					 value = dict_pair[1]
					 batch_dict[key] = value
		
		# End of file
		 else:
			 processed_input.append(batch_dict)
			 batch_dict = {}

	answer = validate_keys(processed_input, valid_keys, optional_key)
	print(answer)
	
	
	


def validate_keys(input_fields, valid_keys, optional_key):
	
	valid_passports_count = 0

	for batch in input_fields:

		keys = list(batch.keys())
		
		if optional_key in keys:
			keys.remove(optional_key)

		keys_sorted = sorted(keys)

		#print(valid_keys)
		#print(keys_sorted)

		if keys_sorted == valid_keys:
			
			valid_passports_count += 1

	return valid_passports_count



#main()
cp.run("main()")