def fibonacci(max):
    curr, prev = 1, 0
    while curr < max:
        yield curr
        curr, prev = curr + prev, curr

total = 0
for number in fibonacci(4000000):
    if not (number % 2):
        total += number
print(total)