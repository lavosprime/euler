sum = 0
for number in range(1000):
    if not (number % 3 and number % 5):
        sum = sum + number
print(sum)
