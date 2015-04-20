def to_digits(num):
	lst=[]
	output=[]
	while num:
			s=num%10
			lst.append(s)
			num//=10
	return lst[::-1]


n=int(input("Enter number:"))
print(to_digits(n))
