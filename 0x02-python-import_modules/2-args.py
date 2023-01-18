#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    length = len(argv)

    i = 1

    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument.")
        print(f"1:{argv[1]}")
    else:
        while(i != length):
            print(f"{i:d}:{argv[i]}")
            i += 1
