def camel_case(str):
    str_list = str.split()
    camel_case_string = ""
    for string in str_list:
        camel_case_string += string.title()
    return camel_case_string

print(camel_case("hello world"))
    

def camelCase(string):
    return string.title().replace(" ", "")

print(camelCase("hello world"))
