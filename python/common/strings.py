def is_palindrome(string):
    """Return whether the given string is a palindrome."""
    for i in range(len(string) // 2):
        if string[i] is not string[-i - 1]:
            return False
    else:
        return True