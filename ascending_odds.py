def ascending_odds(list):
    even_list = []
    odd_numbers = []
    for number in list:
        if number % 2 == 0:
            even_list.append((number, list.index(number)))
        else:
            odd_numbers.append(number)
    odd_numbers.sort()
    for m in even_list:
        (number, index) = m
        odd_numbers.insert(index, number)
    return odd_numbers

print(ascending_odds([1,8,9,7,5,2]))