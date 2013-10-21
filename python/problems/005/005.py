from python.common.number_theory import lcm

result = 1
for number in range(1, 20):
    result = lcm(result, number)
print(result)