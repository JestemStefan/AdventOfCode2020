import cProfile

def main():

    processed_input = []

    with open("11/Input.txt") as input_file:
        
        for line in input_file.readlines():
            line = line.strip()

            processed_input.append(line)


    #for line in processed_input:
        #print(line)


    new_setup = []

    for line in processed_input:

        new_line = ""

        for char in line:
            if char == "L":
                char = "#"

            new_line += char

        new_setup.append(new_line)


    for line in new_setup:
        print(line)

main()
#cProfile.run("main()")