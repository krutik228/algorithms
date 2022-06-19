import re

def is_palindrome(string: str):
    forwards = ''.join(re.findall(r"[a-z]", string.lower()))
    return forwards == forwards[::-1]

def is_palindrome2(string: str):
    lst = [*filter(str.isalpha, string.lower())]
    return lst == lst[::-1]

if __name__ == '__main__':
    print(is_palindrome('Madam, I`m Adam!!!#21124'))
    print(is_palindrome('Hello world'))

    print(is_palindrome2('Madam, I`m Adam!!!#21124'))
    print(is_palindrome2('Hello world'))
