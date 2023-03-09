#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    index = 1

    sum_ = 0

    length = len(argv)

if length == 1:
    print(0)
else:
    while index != length:
        sum_ += int(argv[index])
        index += 1
    print(sum_)
