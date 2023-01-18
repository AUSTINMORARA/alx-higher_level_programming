if __name__ == '__main__':
    from sys import argv

length = len(argv)

result = 0

if length == 1:
    print(f"{result:d}")
else:
    for i in range(1, length):
        result += int(argv[i])
    print(f"{result:d}")
    
