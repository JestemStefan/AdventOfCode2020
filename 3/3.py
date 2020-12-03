def main():

    processed_input = []
    with open("3/Input.txt") as input_file:
        for line in input_file.readlines():
            line.strip()

            processed_input.append(line)

            #print(line)
    
    number_of_trees = slope_path(processed_input)
    print(number_of_trees)


def slope_path(input_map):

    char_index = 0
    
    tree_counter = 0

    for index, row in enumerate(input_map):
        char_index = 3 * index

        char_index = char_index % 31

        if input_map[index][char_index] == "#":
            tree_counter += 1

    return(tree_counter)




main()

