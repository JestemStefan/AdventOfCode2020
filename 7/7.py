import cProfile as cp


def main():

    processed_input = []
    bag_dict = {}

    with open("7/Input.txt") as input_file:
        
        
    
        for line in input_file.readlines():
            
            line = line.strip().split()

            pattern_and_color = ""

            # get pattern and save it to the dict
            pattern_and_color = line[0] + " " + line[1]

            len_line = len(line)

            inside_bags = []

            if len_line >= 8:
                
                number_of_bags = line[4]
                inside_bag_pattern_color = line[5] + " " + line[6]
                inside_bags.append([number_of_bags, inside_bag_pattern_color])

                if len_line >= 12:
                    
                    number_of_bags = line[8]
                    inside_bag_pattern_color = line[9] + " " + line[10]
                    inside_bags.append([number_of_bags, inside_bag_pattern_color])

                    if len_line >= 16:
                        
                        number_of_bags = line[12]
                        inside_bag_pattern_color = line[13] + " " + line[14]
                        inside_bags.append([number_of_bags, inside_bag_pattern_color])

                        if len_line >= 20:
                            
                            number_of_bags = line[16]
                            inside_bag_pattern_color = line[17] + " " + line[18]
                            inside_bags.append([number_of_bags, inside_bag_pattern_color])

            bag_dict[pattern_and_color] = inside_bags


    ################## TASK 1 ###############################
    # find and remove empty bags
    #return_remove = find_empty_bags(bag_dict)
    #empty_bags_list = return_remove[0]
    #full_bags_dict = return_remove[1]

    # remove empty bags from sub bags
    #full_bags_dict = remove_empty_bags(full_bags_dict, empty_bags_list)

    #print(full_bags_dict)

    #list_of_bags_with_shiny_gold = []
    #for bag_pattern_color in full_bags_dict:

        #if search_shiny_gold(full_bags_dict, bag_pattern_color, "shiny gold"):
            #list_of_bags_with_shiny_gold.append(bag_pattern_color)


    #print(len(set(list_of_bags_with_shiny_gold)))

##################### END OF TASK 1 ######################################
    answer = 0

    for bags in bag_dict["shiny gold"]:
        answer += count_bags(bag_dict, bags)

    print(answer)



def count_bags(bag_dict, outer_bag):

    #print(outer_bag)
    number = int(outer_bag[0])
    suma = 0
    
    print(bag_dict[outer_bag[1]])

    for inside_bags in bag_dict[outer_bag[1]]:
        print(inside_bags)

        if bag_dict[outer_bag[1]] != []:
        
            number += int(inside_bags[0]) * count_bags(bag_dict, inside_bags)

        else:
            return 1

        

    return number

    


def find_empty_bags(bag_dict):

    empty_bag_list = []
    temp_bag_dict = list(bag_dict.keys())
    not_empty_bags = bag_dict

    for bag_pattern in temp_bag_dict:

        if len(bag_dict[bag_pattern]) == 0:

            empty_bag_list.append(bag_pattern)
            not_empty_bags.pop(bag_pattern)
        
        else:
            pass
    
    return [empty_bag_list, not_empty_bags]

def remove_empty_bags(bag_dict, empty_bags):

    full_bags_dict = {}

    # check each bag type
    for bag_pattern in bag_dict:
        
        # list of bags that can be inside this bag
        temp_bag_patterns = bag_dict[bag_pattern]

        full_bags = []

        # check what type of bags are inside
        for bag in temp_bag_patterns:

            # if bag in empty
            if bag in empty_bags:

                # remove bag from list
                # print(bag)
                pass
            
            # save bag back to dict
            else:
                full_bags.append(bag)

        full_bags_dict[bag_pattern] = full_bags

    return full_bags_dict

def search_shiny_gold(bag_dict, bag_pattern_color, desiered_bag):

    if desiered_bag in bag_dict[bag_pattern_color]:
        return True

    else:
        for bag in bag_dict[bag_pattern_color]:

            if search_shiny_gold(bag_dict, bag, "shiny gold"):
                return True




main()
#cp.run("main()")
