#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    
    l = len(argv)

    index = 1

    if l == 1:
        print("0 arguments.")
    elif l == 2:
        print("1 argument:")
        print(f"1: {argv[index]}")
    else:
        print(f"{len(argv)} arguments:")
        while index != l:
            print(f"{index}: {argv[index]}")
            index += 1
