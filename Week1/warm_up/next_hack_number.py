def is_palindrome(n):
    stringNum=str(n)
    if stringNum[::-1]==stringNum:
        return True
    else:
        return False

def has_odd_ones(n):
    stringNum=str(n)
    count=stringNum.count("1")
    if count%2==0:
        return False
    else:
        return True

def hack_represent(n):
    x=n
    k=[]
    while (n>0):
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2
    k.append(0)
    string=""
    for j in k[::-1]:
        string=string+str(j)
    return string[1:]

def next_hack(n):
    hack_num=hack_represent(n+1)
    counter=1
    while True:

            if is_palindrome(hack_num) and has_odd_ones(hack_num):
                return n
            else:
                n+=1
                counter+=1
                hack_num=hack_represent(n)


n=int(input("Enter number: "))
print(next_hack(n));

