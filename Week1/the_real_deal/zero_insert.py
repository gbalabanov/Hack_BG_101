def zero_insert(stringNum):
    counter = 0
    output = ""
    output += stringNum[0]
    n1 = 0
    n2 = 0
    for x in range(0, len(stringNum) - 1):
        n1 = int(stringNum[x])
        n2 = int(stringNum[x + 1])
        if n1 == n2 or n1 + n2 == 10:
            output += "0"
            output += stringNum[x + 1]
        else:
            # output+=stringNum[x]
            output += stringNum[x + 1]
    return int(output)


a = (input("Enter number:"))
print(zero_insert(a))

