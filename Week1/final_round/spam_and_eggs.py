def prepare_meal(n):
    output=""
    n=int(n)
    while n%3==0:
        output+="spam "
        n/=3
    if n%5==0 and len(output)==0:
        output+="eggs"
    else:
        if n%5==0:
            output+="and eggs"
    return output
        

a=input("Enter x: ")
print(prepare_meal(a))

