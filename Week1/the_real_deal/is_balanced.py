def is_number_balanced(n):
    count = 0
    revCount = 0
    n = abs(n)
    stringNum = str(n)
    delimiter = len(stringNum) // 2
    for x in range(0, delimiter):
        count += int(stringNum[x])
    for x in range(1, delimiter + 1):
        revCount += int(stringNum[-x])
    return (count == revCount)


n = int(input("Enter number: "))
print(is_number_balanced(n))

