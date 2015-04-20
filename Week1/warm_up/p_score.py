def reverseSum(number):
    stringNum=str(number)
    return int(stringNum)+int(stringNum[::-1])
    
    
def is_palindrome(number):
    stringNum=str(number)
    if stringNum[::-1]==stringNum:
        return True
    else:
        return False
    
    
def p_Score(pal):
    score=1
    if is_palindrome(pal)==True:
        return score
    else:
        while is_palindrome(pal) != True:
            score+=1
            pal=reverseSum(pal)
    return score
    
a=input("Enter number: ")
print(p_Score(a))

