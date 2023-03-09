#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    length = len(argv)

    index = 1

    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
        print(f"1: {argv[index]}")
    else:
        print(f"{length - 1} arguments:")
        while index < length:
            print(f"{index}: {argv[index]}")
            index += 1
