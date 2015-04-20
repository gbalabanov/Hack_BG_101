def factorial(a):
	fact=1
	for x in range(1,a+1):
		fact*=x
	return fact


def fact_digits(n):
	currentDigit=0
	fib=1
	sum=0
	while n:
		currentDigit=n%10
		sum+=factorial(currentDigit)
		n//=10
	return sum
	
n=int(input("Enter n:"))
print(int(fact_digits(n)))
