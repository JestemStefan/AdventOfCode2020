import cProfile as cp
import copy

def main():

    commands = []

    with open("8/Input.txt") as input_file:
        
        for line in input_file.readlines():
            
            line = line.strip().split()

            commands.append(line)

    switch_command_index = 0
    result = False

    while result == False:

        test_commands = copy.deepcopy(commands)

        command_to_switch = test_commands[switch_command_index][0]
        test_commands[switch_command_index][0] = switch_command(command_to_switch)

        switch_command_index += 1

        result = isInfiniteLoop(test_commands)

        #print(result)

    print(result)

def isInfiniteLoop(commands):

    command_index = 0
    accumulator = 0
    max_command_index = len(commands)
    visited_commands = {}

    loop = False

    for i in range(max_command_index):
        
        visited_commands[i] = 0
    

    while loop != True:

        if command_index >= max_command_index:
            return accumulator
        
        visited_commands[command_index] += 1
        
        if visited_commands[command_index] > 1:
            loop = True
            
        else:
            
            command_output = execute_commond(command_index, commands)

            command_index += command_output[0]
            accumulator += command_output[1]
    
    return False
    

def switch_command(command):
    #print("command to switch: " + str(command))

    if command == "jmp":
        #print("switched jmp to nop")
        return "nop"

    elif command == "nop":
        #print("switched nop to jmp")
        return "jmp"
    
    else:
        return command



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



cp.run("main()")

#main()