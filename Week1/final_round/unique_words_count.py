def unique_words(strlist):
    wordList=strlist.split(",")
    wordSet=set(wordList)
    wordList_new=list(wordSet)
    return len(wordList_new)


a = input("Enter words:")
print(unique_words(a))

