'''mySum = 0      
num = 1 
while num <= 10: 
    mySum += num 
    num += 1    
print mySum '''

'''states = [ 'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming' ]
# prints only the states which start with 'M'

for state in states:
    if state[0] == 'M':
        print(state)'''

'''s = "My lucky number is %d, what is yours?" % 7   # dlaczego tak? - combining text and numbers 1
print(s)

s = "My lucky number is " + str(7) + ", what is yours?" # combining text and numbers 2
print(s)'''
'''
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
'''
'''x = 1
def test():
    x = 2
test()
print(x)
'''

'''x = [1]
def test():
    x = [2]
test()
print(x)
'''

'''x = 1
def test():
    global x
    x = 2
test()
print(x)'''

'''x = [1]
def test():
    global x
    x = [2]
test()
print(x)'''

x = [1]
def test():
    x[0] = 2
test()
print(x)



