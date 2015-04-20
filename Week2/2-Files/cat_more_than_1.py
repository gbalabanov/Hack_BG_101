import sys


def read_files():
    if len(sys.argv) > 1:
        for x in range(1,len(sys.argv)):
            with open(sys.argv[x], "r") as obj:
                print(obj.read())
                #print("\n")
    else:
        print("Type a file names !")

print(read_files())
