def main():

    processed_input = []

    with open("7/Input.txt") as input_file:
        pattern_dict = {}
        color_dict = {}

        for line in input_file.readlines():

            line = line.strip().split()

            # get pattern and save it to the dict
            pattern = line[0]
            color = line[1]
            color_dict[color] = []

            pattern_dict[pattern] = color_dict

            processed_input.append(line)


    for line in processed_input:
        print(line)

    for key in pattern_dict.keys():
        pass
        #print(key)
        #print(pattern_dict[key])



main()
