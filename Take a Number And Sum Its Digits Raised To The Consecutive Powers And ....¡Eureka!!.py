# get the 2 numbers to get the range
# we convert the number to string



## Theory: 
# In effect: 89 = 8^1 + 9^2
# The next number in having this property is 135.
# See this property again: 135 = 1^1 + 3^2 + 5^3
def sum_dig_pow(n1, n2):
    result = []
    for a in range(n1, n2+1):
        square_numbers = []
        b = str(a)
        for letter in b:
            square_numbers.append(int(letter) ** int(b.index(letter) + 1))
        if a == sum(square_numbers):
            result.append(a)
    return result

print(sum_dig_pow(191, 2673))

# This is another solution
def sum_dig_pow(a, b): 
    my_sum = 0 
    my_list = []
    for item in range(a,b+1):
        j = str(item)
        _length = len(j)
        n = 1
        for k in range(0,_length):
            my_sum += pow(int(j[k]),n)
            n += 1
        if item == my_sum:
            my_list.append(item)
        my_sum = 0
    my_list.sort()
    return my_list