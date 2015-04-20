def max_consecutive(strlist):
    wordList=strlist.split(",")
    current=1
    best=1
    count=1
    for x in range(0,len(wordList)):
        if x==len(wordList)-1:
            break
        else:
            count+=1
            if wordList[x] == wordList [x+1]:
                current+=1
            else:
                current=1
        if current>best:
            best=current
    return best




a = input("Enter words:")
print(max_consecutive(a))

