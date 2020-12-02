def main():

    proccessed_input = []
    with open("2/Input.txt") as input_file:
        for line in input_file.readlines():

            input_line = line.strip().split()
            valid_range = input_line[0].split("-")
            valid_key = input_line[1].replace(":","")
            password = input_line[2]

            proccessed_input.append([valid_range, valid_key, password])
        
        print(proccessed_input)


def count_letters(s, key, range_min, range_max):

    count = 0

    if key in s:
        count +=1

    print(count)
        


main()