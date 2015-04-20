def contains_digit(number,digit):
    return (str(digit) in str(number))
    
a=input("Enter number:")
b=input("Enter digit: ")
print(contains_digit(a,b))

