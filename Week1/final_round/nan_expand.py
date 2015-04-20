def nan_expand(n):
    output = ""
    n = abs(int(n))
    if n > 0:
        while n > 0:
            output += "Not a "
            n -= 1
        output += "NaN"
    return output

a = input("Enter number:")
print(nan_expand(a))

