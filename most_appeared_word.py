def top_3_words(str):
    result = {}
    str_list = str.split()
    for letter in str_list:
        letter_occurance = str.count(letter)
        result[letter] = letter_occurance
    my_keys = sorted(result, key=result.get, reverse=True)[:3]
    return my_keys

print(top_3_words("In a village of La Mancha, the name of which I have no desire to call to\
mind, there lived not long since one of those gentlemen that keep a lance\
in the lance-rack, an old buckler, a lean hack, and a greyhound for\
coursing. An olla of rather more beef than mutton, a salad on most\
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra\
on Sundays, made away with three-quarters of his income."))
