def sum_of_digits(n):
	sum=0
	if n<=0:
		return 1
	if n>=1 and n<=9:
		return n
	else:
		while n:
			sum+=n%10
			n//=10
		return sum
n=int(input("Enter n:"))
print(int(sum_of_digits(n)))
