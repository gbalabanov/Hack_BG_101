import sys


def sum_numbers():
    list_nums = []
    filename = sys.argv[1]
    myfile = open(filename, "r")
    list_nums = myfile.read().split(" ")
    print(list_nums)
    return sum(int(x) for x in list_nums)

print(sum_numbers())
