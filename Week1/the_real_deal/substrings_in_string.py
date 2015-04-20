def count_substring(main,sub):
    count=0
    iterator=main.find(sub)
    while(iterator != -1):
        count+=1
        iterator=main.find(sub,iterator+len(sub))
    return count




a=(input("Enter string: "))
b=(input("Enter substring: "))
print(count_substring(a,b));

