import cProfile as cp

def main():

    commands = []

    with open("8/Input.txt") as input_file:
        
        for line in input_file.readlines():
            
            line = line.strip().split()

            commands.append(line)



    command_index = 0
    accumulator = 0

    loop = False
    visited_commands = {}

    for i in range(len(commands)):
        
        visited_commands[i] = 0
    

    while loop != True:
        
        visited_commands[command_index] += 1

        if visited_commands[command_index] > 1:
            loop = True
            #print(accumulator)
        
        else:

            command_output = execute_commond(command_index, commands)
            command_index += command_output[0]
            accumulator += command_output[1]
    
    print(accumulator)



def execute_commond(command_index, commands_input):

    command = commands_input[command_index][0]
    variable = int(commands_input[command_index][1])

    if command == "jmp":

        next_index = variable
        acc_change = 0
        return [next_index, acc_change]

    elif command == "acc":

        next_index = 1
        acc_change = variable
        return [next_index, acc_change]

    else:

        next_index = 1
        acc_change = 0
        return [next_index, acc_change]


#cp.run("main()")

main()