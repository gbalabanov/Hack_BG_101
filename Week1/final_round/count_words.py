def count_words(strlist):
    wordList=strlist.split(",")
    wordSet=set(wordList)
    wordList_new=list(wordSet)
    output={x:wordList.count(x) for x in wordList_new}
    return output


a = input("Enter words:")
print(count_words(a))

