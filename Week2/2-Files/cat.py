import sys
from io import IOBase


def read_file():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        textfile = open(filename, "r")
        return textfile.read()
        textfile.close()

    else:
        print("Type a file name !")

print(read_file())
