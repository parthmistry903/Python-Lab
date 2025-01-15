#Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.
def to_lower_case(input_string):
    result = ''
    for char in input_string:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def to_upper_case(input_string):
    result = ''
    for char in input_string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def toggle_case(input_string):
    result = ''
    for char in input_string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

# Test functions
user_input = input("Enter a string: ")
print(f"Lower case: {to_lower_case(user_input)}")
print(f"Upper case: {to_upper_case(user_input)}")
print(f"Toggle case: {toggle_case(user_input)}")
