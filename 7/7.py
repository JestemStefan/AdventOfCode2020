def main():

    processed_input = []

    with open("7/Input.txt") as input_file:

        for line in input_file.readlines():

            line = line.strip()
            #line = line.replace("/n", "")
            #print("line: " + line)
            processed_input.append(line)

    processed_input_sorted = sorted(processed_input)

    for line in processed_input:
        print(line)



main()