import cProfile


def main():

    processed_input = []

    with open("10/Input.txt") as input_file:
        
        for line in input_file.readlines():
            line = line.strip()
            
            processed_input.append(int(line))

    processed_input.append(max(processed_input) + 3)
    processed_input = sorted(processed_input)

    amount_of_one_jolts = 0
    amount_of_three_jolts = 0

    for i, adapter in enumerate(processed_input):
        print(adapter)
        difference = 0

        if i == 0:
            difference = adapter

        else:
            difference = (adapter - processed_input[i-1])

        if difference < 3:
            amount_of_one_jolts += 1
            
        else:
            amount_of_three_jolts += 1

    print("Answer: " + str(amount_of_one_jolts) + " * " + str(amount_of_three_jolts) + " = " + str(amount_of_one_jolts * amount_of_three_jolts))
    #print(amount_of_one_jolts * amount_of_three_jolts)



cProfile.run("main()")
#main()