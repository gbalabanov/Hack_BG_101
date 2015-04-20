def is_prime(n):
    sumUp=0
    n=abs(int(n))
    divisors=[]
    for x in range(1,int(n)+1):
        if int(n)%x==0:
            divisors.append(int(x))
    #for x in divisors:
    #    sumUp+=x
    if len(divisors)==2:
    	return True
    else:
    	return False
    	
    
a=input("Enter number:")
print(is_prime(a))

