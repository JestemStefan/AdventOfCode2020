def main():

    processed_input = []
    with open("3/Input.txt") as input_file:
        for line in input_file.readlines():
            line.strip()

            processed_input.append(line)

            #print(line)

    #Task1
    number_of_trees = slope_path(processed_input)

    print("Task 1 answer is " + str(number_of_trees))


    # Task2
    answer = 1

    for slope_dimensions in [[1,1], [1,3], [1,5], [1,7], [2,1]]:
        
        #                             v---Map           v--- Slope length   v--- Slope height (tilt)
        number_of_trees = slope_path2(processed_input, slope_dimensions[1], slope_dimensions[0])

        answer *= number_of_trees

    print("Task 2 answer is " + str(answer))
        


# Task 1
def slope_path(input_map):

    char_index = 0
    tree_counter = 0

    for index, row in enumerate(input_map):

        char_index = (3 * index) % 31 

        if row[char_index] == "#":
            tree_counter += 1

    return(tree_counter)


# Task2
def slope_path2(input_map, slope_length, slope_height):


    char_index = 0
    tree_counter = 0

    for row_index in range(0, len(input_map), slope_height):

        current_row = input_map[row_index]
        row_length = len(current_row) - 1

        # check if character in this position is a tree ("#")
        if current_row[char_index] == "#":
            tree_counter += 1

        # move down the slope
        char_index = (char_index + slope_length) % row_length
        
    return(tree_counter)



main()

