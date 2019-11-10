def gcd():
    '''
    Calculate the Grates Common Divisor
    gcd(a, b) = a, if b =0
    otherwise = gcd(b, a mod b)
    '''
    
    print("The Greates Common Divisor.")
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    if a > b:
        a, b = b, a
        
    for i in range (a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

print(str(gcd()))