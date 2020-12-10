import cProfile as cp

def main():

    processed_input = []

    with open("9/Input.txt") as input_file:
        
        for line in input_file.readlines():
            line = line.strip()

            processed_input.append(int(line))

    loop = False
    preamble = 25
    number_index = 0

    

    while loop != True:

        loop = check_if_NOT_sum(processed_input, number_index, preamble)
        number_index += 1

    invalid_number = processed_input[number_index + preamble - 1] 
    print(invalid_number)


        



def check_if_NOT_sum(number_input, number_index, preamble):

    test_number = number_input[number_index + preamble]
    #print(test_number)

    find_sum_here = number_input[number_index:preamble + number_index]

    for num in find_sum_here:

        reminder_num = abs(test_number - num)
        #print(reminder_num)

        if reminder_num in find_sum_here:
            return False

    else:
        return True
    
    
#cp.run("main()")
main()