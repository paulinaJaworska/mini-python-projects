# numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
numbers = [-5, 23, 0, "fghj", -9, 12, 99, [2, 44], None, 105, -43]

print(numbers)

for n in range(len(numbers)-1):   # sort the list form the smallest to the biggest number
        for i in range(len(numbers)-1):
                if numbers[i + 1] < numbers[i]:
                        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

max = numbers[-1]
min = numbers[0]

avg = 0
for i in range(len(numbers)):
        avg += numbers[i]
avg = avg / len(numbers)

print(("Max: {}").format(max))
print(("Min: {}"). format(min))
print(("Avg: {}").format(avg))