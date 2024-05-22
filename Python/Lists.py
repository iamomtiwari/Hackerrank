if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for _ in range(N):
        command_line = input().split()
        command = command_line[0]
        
        if command == "append":
            arr.append(int(command_line[1]))
        elif command == "insert":
            arr.insert(int(command_line[1]), int(command_line[2]))
        elif command == "remove":
            arr.remove(int(command_line[1]))
        elif command == "pop":
            arr.pop()
        elif command == "sort":
            arr.sort()
        elif command == "reverse":
            arr.reverse()
        elif command == "print":
            print(arr)

