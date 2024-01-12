def is_palindrome(s: str) -> bool:
    """
    Return whether a string is a palindrome or not.
    """
    return str(s) == str(s)[::-1]


def is_numeric_palindrome(number: int | str) -> bool:
    """
    Return whether a number is a palindrome or not, considering leading zeros.
    """
    # Remove 0 in the end as there are potentially infinite leading zeros in the beginning of the number
    return is_palindrome(str(number).rstrip('0'))
