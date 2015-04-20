def is_leap(n):
    n=int(n)
    if n%4==0 and n%4==0 and n%100!=0 :
        return True
    else:
        return False

def years_legit(a,b):
    return(len(str(a)) == 4 and len(str(b)) == 4)


a = input("Enter number:")
#b = input("Enter number:")
print(is_leap(a))

