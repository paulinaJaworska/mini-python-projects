def fib(n):
    # produces Fibonacci sequence up to n position and prints enumarative result 
    result = []
    a = 0 
    b = 1
    j = 0
    for i in range(n):
        result.append(a)
        a, b = b, a+b 
    i = 1 
    k = len(str(result[-1])) + 4
    while i < n+1:
        final_result = "{0}. {1}"
        print(final_result.format(i, str(result[j]).rjust(k)))    # adds k spaces on the right of result
        i += 1
        j += 1
        if len(str(i)) - (len(str(i-1))) == 1:                    # dinamically adjusts spaces in between the values by changing k
            k -= 1

# input conditions
length = int(input("Enter the length of Fibonacci sequence: ")) 
if length > 0:
    fib(length)
elif length <= 0:
    print("The number has to be grater than zero.")
else:
    print("The number has to be an intiger.")