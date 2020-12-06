def main():


    with open("6/Input.txt") as input_file:

        answers_groups = []
        batch = []

        for line in input_file.readlines():

            line = line.strip()

            if line != "":
                batch.append(set(line))


            else:
                answers_groups.append(batch)
                #print(batch)
                batch = []

        else:
            answers_groups.append(batch)
            #print(batch)
            batch = []


        task2_answer = 0

        for group in answers_groups:
            task2_answer += len(set.intersection(*group))

        print(task2_answer)

    #task1_answer = 0

    #for answers in answers_groups:
        #task1_answer += len(set(answers))

    #print(task1_answer)


main()