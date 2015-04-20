def is_prime(n):
    sumUp=0
    n=abs(int(n))
    divisors=[]
    count=0
    bol=True
    for x in range(1,int(n)+1):
        if int(n)%x==0:
            divisors.append(int(x))
    number=len(divisors)
    for x in range(1,number+1):
    	if number%x==0:
    		count+=1
    		if count>2:
    			bol=False 
    return bol	
    
a=input("Enter number:")
print(is_prime(a))

