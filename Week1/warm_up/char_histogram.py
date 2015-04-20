
def char_histogram(obj):
    list_letters=[]
    list_counts=[]
    count=0
    final={}
    for x in range(0,len(obj)):
    	if obj[x] not in list_letters:
    		list_letters.append(obj[x])
    for x in range(0,len(list_letters)):
    	for j in range(0,len(obj)):
    		if list_letters[x]==obj[j]:
    			count+=1
    	list_counts.append(count)
    	count=0
    for x in range(0,len(list_letters)):
    	final[list_letters[x]] = list_counts[x]
    return final

a=str(input("Enter string:"))
print(char_histogram(a))

