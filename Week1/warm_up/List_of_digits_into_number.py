def to_digits(num):
	list_nums=[]
	output=0
	for x in range(0,len(num)):
		if num[x].isdigit():
			list_nums.append(num[x])
	for x in range(0,len(list_nums)):
		current=int(list_nums[x])*10**int(len(list_nums)-(x+1))
		output+=current
	return output

n=(input("Enter number:"))
print(to_digits(n))
