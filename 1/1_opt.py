def main():


    with open("1/Input.txt") as input_file:

        desired_value = 2020

        input_numbers = []
        for line in input_file.readlines():
            input_numbers.append(int(line.strip()))

        input_numbers.sort()

        answer = search_for_number(input_numbers, desired_value)
        print(answer)

def search_for_number(input_numbers, desired_value):

    smallest_number = min(input_numbers)
    max_value_of_sum = desired_value - smallest_number

    for first_number in input_numbers:
        for second_number in input_numbers:

            sum_of_two = first_number + second_number

            if sum_of_two < max_value_of_sum:
                third_number = desired_value - (sum_of_two)

                if third_number in input_numbers:
                    return(first_number * second_number * third_number)

            else:
                break

main()