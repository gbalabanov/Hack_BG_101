def sum_of_divisors(n):
    sumUp=0
    divisors=[]
    for x in range(1,int(n)+1):
        if int(n)%x==0:
            divisors.append(int(x))
    for x in divisors:
        sumUp+=x
    return sumUp
    
a=input("Enter number:")
print(sum_of_divisors(a))

