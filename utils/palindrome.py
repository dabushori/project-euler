def is_palindrome(s: str | int):
    return str(s) == str(s)[::-1]
