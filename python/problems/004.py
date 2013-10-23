from python.common.strings import is_palindrome

result = 0
for a in range(100, 1000):
    for b in range(a, 1000):
        p = a * b
        if is_palindrome(str(p)) and p > result:
            result = p
print(result)