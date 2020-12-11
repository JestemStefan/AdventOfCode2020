def main():

    #processed_input = []

    with open("10/Input.txt") as input_file:
        
        for line in input_file.readlines():
            line = line.strip()
            print(line)
            #processed_input.append(int(line))

main()