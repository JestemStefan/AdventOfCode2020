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
    max_search_index = number_index + preamble - 1

    #print([max_search_index, invalid_number])


    num_input_list = processed_input[:max_search_index]
    num_input_list.reverse()

    loop = False
    number_index = 0
    for idx, number in enumerate(num_input_list):

        return_value = find_continous_sum(num_input_list, idx, invalid_number)

        if return_value:
            print("Answer: " + str(min(return_value) + max(return_value)))

    


        



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
    

def find_continous_sum(num_input, start_index, target):
    #print("target: " + str(target))

    end_index = start_index + 1

    continous_sum = 0

    while continous_sum != target:

        continous_sum = sum(num_input[start_index:end_index])
    
        if continous_sum > target:
            return 0

        elif continous_sum < target:
            end_index += 1


    return num_input[start_index:end_index]



cp.run("main()")
#main()