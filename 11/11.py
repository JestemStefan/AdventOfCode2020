import cProfile

def main():

    processed_input = []

    with open("11/Input.txt") as input_file:
        
        for line in input_file.readlines():
            line = line.strip()

            processed_input.append(line)


    #for line in processed_input:
        #print(line)

    is_Stable = False
    game_input = processed_input

    while is_Stable != True:
    #for i in range(2):
        game_result = game_of_life(game_input)

        

        game_input = game_result[0]

        if game_result[1] == 0:
            is_Stable = True

    answer = 0

    for line in game_input:
        answer += line.count("#")

    
    print(answer)



def game_of_life(game_input):
    new_setup = []

    number_of_changes = 0

    for i in range(len(game_input)):

        new_line = ""

        for j in range(len(game_input[i])):

            seat_type = game_input[i][j]

            check_seats = ""
            check_seats = check_seats_func(game_input, i, j)


            empty_seat = check_seats.count("L")
            full_seat = check_seats.count("#")
            floors = check_seats.count(".")
            #print([empty_seat, full_seat, floors])

            
            if seat_type == "L" and full_seat == 0:
                new_line += "#"
                number_of_changes += 1

            elif seat_type == "#" and full_seat >= 4:
                new_line += "L"
                number_of_changes += 1
            
            else:
                new_line += seat_type

        new_setup.append(new_line)

    #print(number_of_changes)
    

    #for i, line in enumerate(new_setup):

        #print("row number: " + str(i) + " " + line)

    return[new_setup, number_of_changes]


def check_seats_func(seats, target_row, target_pos):
    surr_seats = ""
    prefix = ""
    suffix = ""

    if target_pos <= 0:
        pos_start = target_pos
        prefix = "."
    
    else:
        pos_start = target_pos - 1

    if target_pos >= len(seats[target_row]):
        pos_stop = target_pos + 1
        suffix = "."

    else:
        pos_stop = target_pos + 2


########################
    if target_row <= 0:
        top_row = "..."

    else:
        top_row = prefix + seats[target_row - 1][pos_start:pos_stop] + suffix

###########################

    middle_row = prefix + seats[target_row][pos_start:target_pos] + seats[target_row][target_pos + 1: pos_stop] + suffix

###########################
    if target_row > len(seats) - 2:
        bottom_row = "..."
    
    else:
        bottom_row = prefix + seats[target_row + 1][pos_start:pos_stop] + suffix

    #print(bottom_row)
###############################    

    surr_seats = top_row + middle_row + bottom_row
    #print(surr_seats)

    #print([target_row, target_pos])
    #print(surr_seats)
    return surr_seats
    
    

main()
#cProfile.run("main()")