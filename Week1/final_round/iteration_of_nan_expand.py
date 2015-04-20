def iteration_of_nan_expand(n):
    if n[-3:]=="NaN":
        return (n.count("Not a"))
    else:
        return False

a = input("Enter number:")
print(iteration_of_nan_expand(a))

