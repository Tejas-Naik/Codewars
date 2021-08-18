def last_digit(n1, n2):
    if n1 == 0 or n2 == 0:
        return 1
    elif n1 == 10 or n2 == 10:
        return 10
    if len(str(n1)) > 2:
        n1 = str(n1)[-1]
    if len(str(n2)) > 2:
        n2 = str(n1)[-1:]
    result = str(int(n1) ** int(n2))[-1]
    return int(result)

print(last_digit(9, 7))

# Other solution
def lastDigit(n1, n2):
    if n2 == 0:
        return 1

    last_digits = []

    step = 1
    while True:
        number = pow(n1, step)
        step += 1
        last_digit = int(str(number)[-1])

        if last_digit in last_digits:
            break

        last_digits.append(last_digit)

    print(last_digits)
    last_digit_index = n2 % len(last_digits) - 1

    return last_digits[last_digit_index]

# Or how about this one
def last_digit(n1, n2):
    return pow(n1, n2, 10)