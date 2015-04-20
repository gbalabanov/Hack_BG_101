def is_an_bn(word):
    return (word[:len(word)//2] == 'a'*(len(word)//2) and word[len(word)//2::] == 'b'*(len(word)//2))

a=input("Enter word: ")
print(is_an_bn(a))



