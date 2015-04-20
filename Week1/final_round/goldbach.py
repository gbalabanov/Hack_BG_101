def is_prime(n):
    n = abs(int(n))
    divisors = []
    for x in range(1, int(n) + 1):
        if int(n) % x == 0:
            divisors.append(int(x))
    # for x in divisors:
    #    sumUp+=x
    if len(divisors) <= 2:
        return True
    else:
        return False


def goldbach(n):
    output = []
    sum=0
    delimiter=0
    n = abs(int(n))
    if n%2 != 0:
        return None
    prime_list = [x for x in range(1, n+1) if is_prime(x) and x>1]
    #del_list=[x for x in range(1,n+1) if n%x == 0]
    #del_list = del_list[::-1]
    for x in prime_list:
        for y in prime_list:
            if x+y==n:
                output.append((x,y))
    if len(output)%2==0:
        delimiter=len(output)//2
    else:
        delimiter=len(output)//2+1
    return output[:delimiter]





a = input("Enter number:")
print(goldbach  (a))

