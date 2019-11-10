'''Write a program which prints the top 25 three-digit 
natural numbers divisible by 7 or by 9. Each number 
should be displayed in a separate line.'''

l = []
for num in range(100, 1000):
    if num%7 == 0 or num%9 == 0:
        l.append(num)
for i in l[-25:]:
    print(i)