def palindrome(obj):
    if obj[::-1] == obj:
       return True
    else:
       return False
a=str(input("Enter string:"))
print(palindrome(a))

