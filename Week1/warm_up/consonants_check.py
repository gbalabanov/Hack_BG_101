
def count_vowels(string1):
    counter=0
    string=str(string1).lower()
    vowels=['a','e','i','o','u','y']
    for x in range(0,len(string)):
        if str(string[x]) not in vowels and str(string[x]).isalpha():
            counter+=1
    return counter

a=input("Enter string:")
print(count_vowels(a))

