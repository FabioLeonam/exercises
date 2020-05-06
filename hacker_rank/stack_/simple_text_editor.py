if __name__ == '__main__':

    entry = int(input())
    my_string = ""
    history = []

    for i in range(entry):
        my_input = input().strip().split(' ')

        if my_input[0] == '1':
            history.append(my_string)
            print(my_string)
            my_string += my_input[1]
        
        elif my_input[0] == '2':
            history.append(my_string)
            del_pos = int(my_input[1])
            my_pos = len(my_string) - del_pos
            my_string = my_string[0:my_pos]

        elif my_input[0] == '3':
            my_pos = int(my_input[1]) - 1
            print(my_string[my_pos])
        
        else:
            my_string = history.pop()