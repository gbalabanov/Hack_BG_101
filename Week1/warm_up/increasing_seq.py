def is_increasing(num):
	nums=num.split(",")
	list_nums=[]
	count=1
	increasing=True
	nums[0]=nums[0].replace("[","")
	nums[len(nums)-1]=nums[len(nums)-1].replace("]","")
	for x in range(0,len(nums)):
		list_nums.append(int(nums[x]))
	#while count < len(list_nums)-2:
	for x in range(0,len(num)):
		if count==len(list_nums):
			break
		count+=1
		if list_nums[x] >= list_nums[x+1]:
			increasing=False
			break
	return increasing


a=((input("Enter numbers:")))
print(is_increasing(a))

