def main():

    valid_pasword_count = 0
    with open("2/Input.txt") as input_file:
        for line in input_file.readlines():

            input_line = line.strip().split()
            valid_range = input_line[0].split("-")
            range_min = ''.join(filter(str.isdigit, valid_range[0]))
            range_max = ''.join(filter(str.isdigit, valid_range[1]))
            valid_key = input_line[1].replace(":","")
            password = input_line[2]

            #valid = is_valid_password(password, valid_key, int(range_min), int(range_max) + 1)
            valid = is_valid_password2(password, valid_key, int(range_min)-1, int(range_max)-1)
            
            if valid:
                valid_pasword_count += 1

    print("Amount of valid password: " + str(valid_pasword_count))
        

def is_valid_password(s, key, range_min, range_max):
    #print([s,key, range_min, range_max])
    counter = s.count(key)

    if counter in range(range_min, range_max):
        return True
    else:
        return False


def is_valid_password2(s, key, pos1, pos2):
    return (s[pos1] == key) ^ (s[pos2] == key)



main()