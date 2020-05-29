if __name__ == '__main__':
    N = int(input())
    arr = []
    number_1 = 0
    number_2 = 0
    for i in range(N):
        command = input()
        command = command.split()

        if command[0] == "insert":
            number_1 = int(command[1])
            number_2 = int(command[2])
            arr.insert(number_1, number_2)
        elif command[0] == "print":
            print(arr)
        elif command[0] == "remove":
            number_1 = int(command[1])
            arr.remove(number_1)
        elif command[0] == "append":
            number_1 = int(command[1])
            arr.append(number_1)
        elif command[0] == "sort":
            arr.sort()
        elif command[0] == "pop":
            arr.pop()
        elif command[0] == "reverse":
            arr.reverse()