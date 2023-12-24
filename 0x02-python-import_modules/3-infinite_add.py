if __name__ == "__main__":
    from sys import argv

    length = len(argv)
    si = 0

    if length == 1:
        print("{:d}".format(si))
    else:
        for i in range(1, length):
            si = si + int(argv[i])

        print("{:d}".format(si))
