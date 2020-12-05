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

	answer = validate_keys2(processed_input, valid_keys, optional_key)
	print(answer)
	
	
	

# Task1
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


# Task2
def validate_keys2(input_fields, valid_keys, optional_key):

	batch_to_validate = []


	for batch in input_fields:

		keys = list(batch.keys())
		
		if optional_key in keys:
			keys.remove(optional_key)

		keys_sorted = sorted(keys)

		#print(valid_keys)
		#print(keys_sorted)

		

		if keys_sorted == valid_keys:
			
			batch_to_validate.append(batch)
		
	count_valid_fields = 0
	count_invalid_fields = 0

	#print("valid batches" + str(len(batch_to_validate)))

	valid_keys_unsorted = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

	
	for batch in batch_to_validate:
		if field_validation(batch, valid_keys_unsorted):
			count_valid_fields += 1
		else:
			count_invalid_fields += 1

	return count_valid_fields

		

def field_validation(batch, valid_keys):

	for key in valid_keys:

		if key == "byr":
			if 1920 <= int(batch[key]) <= 2002:
				#print(batch[key] + " is valid Birth Year")
				pass
			
			else:
				#print("Failed at: " + key + ": " + batch[key])
				return False


		elif key == "iyr":
			if 2010 <= int(batch[key]) <= 2020:
				#print(batch[key] + " is valid Issue Year")
				pass

			else:
				#print("Failed at: " + key + ": " + batch[key])
				return False


		elif key == "eyr":
			if 2020 <= int(batch[key]) <= 2030:
				#print(batch[key] + " is valid Expiration Year")
				pass

			else:
				return False


		elif key == "hgt":
			#print(batch[key][-3:])
			if batch[key][-2:] == "in":
				if 59 <= int(batch[key][:-2]) <= 76:
					#print(batch[key] + " is valid height")
					pass
				
				else:
					#print("Failed at: " + key + ": " + batch[key])
					return False

			elif batch[key][-2:] == "cm":
				if 150 <= int(batch[key][:-2]) <= 193:
					#print(batch[key] + " is valid height")
					pass

				else:
					#print("Failed at: " + key + ": " + batch[key])
					return False
		
		elif key == "hcl":
			if len(batch[key]) == 7 and batch[key][0] == "#":
				for char in batch[key][1:]:
					if char.isdigit() or char in ["a", "b", "c", "d", "e", "f"]:
						pass
						
					else:
						#print(batch[key][1:])
						#print("Failed at: " + key + ": " + batch[key])
						return False
					
				#print(batch[key] + " is valid hair color")
				pass

			else:
				#print("Failed at: " + key + ": " + batch[key])
				return False


		elif key == "ecl":
			if batch[key] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
				#print(batch[key] + " is valid eye color")
				pass

			else:
				#print("Failed at: " + key + ": " + batch[key])
				return False


		elif key == "pid":
			digit_count = 0
			for char in batch[key]:
				if char.isdigit():
					digit_count +=1
			
			if digit_count == 9:
				#print(batch[key] + " (" + str(digit_count) + ")" + " is valid Passport ID")
				pass

			else:
				#print("Failed at: " + key + ": " + batch[key])
				return False

	#print("VALID BATCH")
	return True

#main()
cp.run("main()")