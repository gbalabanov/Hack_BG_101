import sys
from io import IOBase
from random import randint


def generate_numbers():
    list_num = []
    a = int(sys.argv[2])
    filename = sys.argv[1]

    for x in range(0, a):
        list_num.append(str(randint(1, 1000)))
    try:
        myfile = open(filename, "r+")
        #myfile.truncate()
        myfile.write(" ".join(list_num))
    except IOBase as error:
        print(error)
    myfile.close()
    myfile = open(filename, "r")
    print(myfile.read())

print(generate_numbers())
