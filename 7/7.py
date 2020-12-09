def main():

    processed_input = []

    with open("7/Input.txt") as input_file:
        bag_dict = {}
        
    
        for line in input_file.readlines():
            
            line = line.strip().split()

            pattern_and_color = ""

            # get pattern and save it to the dict
            pattern_and_color = line[0] + " " + line[1]

            len_line = len(line)

            inside_bags = []

            if len_line >= 8:

                inside_bag_pattern_color = line[5] + " " + line[6]
                inside_bags.append(inside_bag_pattern_color)

                if len_line >= 12:

                    inside_bag_pattern_color = line[9] + " " + line[10]
                    inside_bags.append(inside_bag_pattern_color)

                    if len_line >= 16:

                        inside_bag_pattern_color = line[13] + " " + line[14]
                        inside_bags.append(inside_bag_pattern_color)

                        if len_line >= 20:

                            inside_bag_pattern_color = line[17] + " " + line[18]
                            inside_bags.append(inside_bag_pattern_color)

            bag_dict[pattern_and_color] = inside_bags
            
            print(pattern_and_color)
            print(bag_dict[pattern_and_color])

        processed_input.append(line)


        #search_bags(pattern_dict, key, pattern_dict[key])


def search_bags(pattern_dictionary, pattern, color):

    pass
    #print(pattern)
    #print(pattern_dictionary[pattern])

    #bag_type = pattern_dictionary[pattern][color]

    #for i in bag_type:

        #print(i)





main()
