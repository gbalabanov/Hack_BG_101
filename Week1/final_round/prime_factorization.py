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

def time_dell(big,small):
    count=0
    big=int(big)
    small=int(small)
    while big%small==0:
        count+=1
        big//=small
    return count


def prime_factorization(n):
    output = []
    n = abs(int(n))
    summ=0
    temp=n
    prime_list = [x for x in range(2, n+1) if is_prime(x)]
    del_list=[x for x in prime_list if n%x == 0]
    del_list = del_list[::-1]
    for x in del_list:
        if time_dell(n,x) and temp>0:
            summ+=(x**time_dell(n,x))
            temp-=summ
            output.append((x,time_dell(n,x)))
    return output







a = input("Enter number:")
#b = input("Enter number:")
print(prime_factorization  (a))

