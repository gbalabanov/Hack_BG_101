def sum_digits(n):
    return sum(int(x) for x in n)


def double_odd_digits(n):
    n = n[::-1]
    output = ""
    for x in range(0, len(n)):
        if x % 2 == 0:
            output += n[x]
        else:
            output += str(int(n[x]) * 2)
    return output[::-1]


def is_credit_card_valid(n):
    if len(n) % 2 == 0:
        return False
    if sum_digits(double_odd_digits(n)) % 10 == 0:
        return True
    else:
        return False


a = (input("Enter nuber: "))

print(is_credit_card_valid(a))

