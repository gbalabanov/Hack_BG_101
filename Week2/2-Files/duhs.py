import sys
import os


def duhs():
    path = sys.argv[1]
    output = 0
    counter=1
    total_size = 0
    currency = ""
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    if total_size in range(0,1024):
        return(str(total_size) + " B")
    if total_size in range(1025,1048576):
        return("{:.3} MB".format(total_size/1024))
    if total_size in range(1048576,1073741824):
        return("{:.4} MB".format(total_size/1024**2))
    if total_size >= 1073741824:
        return("{:.5} GB".format(total_size/1024**3))

print(duhs())
