def group(cons):
    output=[]
    tempList=[]
    consList=cons.split(",")
    counter=1
    if len(cons)%2==0:
        consList.pop()
    for x in range(0,len(consList)-1):
        if consList[x] == consList[x+1]:
            tempList.append(consList[x+1])
            isAlone=False
            if x!=len(consList)-2:
                continue
        else:
            tempList.append(consList[x])
            isAlone=True
        output.append(tempList)
        tempList=[]
    if consList[len(consList)-1] == consList[len(consList)-2]:
        output[len(output)-1].append(consList[len(consList)-1])
    else:
        output.append([consList[len(consList)-1]])
       
    return output
    

a=input("Enter elements:")
print(group(a))

