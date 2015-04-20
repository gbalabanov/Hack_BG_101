def fibonaci(num):
    fibs=[1,1,2]
    output=[]
    final=""
    
    for x in range(0,num):
        fibs.append(fibs[-1]+fibs[-2])
        output.append(fibs[x])
        final+=str(output[x])
    
    return int(final)

a=int(input("Enter n:"))
print(fibonaci(a))

