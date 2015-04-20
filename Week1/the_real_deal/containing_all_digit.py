def contains_digit(number,strList):
   numList=[]
   containing=True
   for x in strList:
   	if x.isdigit():
   		numList.append(x)
   if len(numList)==0:
   	return False
   else:
   	for x in numList:
   		if x not in str(number):
   			containing=False
   return containing
   
    
a=input("Enter number:")
b=input("Enter list of digits: ")
print(contains_digit(a,b))

