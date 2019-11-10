from math import sqrt, fabs

# Jak wrócić znowu do wpisywania a po wpisaniu złej wartości?
'''a, b, c, d, e, f = None, None, None, None, None, None

def collect_coordinates(letter_value, ax, verticle):    
    while True:
        try:
            input_querry = ("Please specify coordinate {0} of a verticle {1}: ").format(ax, verticle)
            global value_of_input
            value_of_input = letter_value
            letter_value = float(input(input_querry))
            if letter_value < 100 and letter_value > -100:
                break
            print("Please enter the number between -100 and 100")
        except ValueError:
            print("Please enter the NUMBER!")

a = collect_coordinates(a, "X", "A")
b = collect_coordinates(b, "Y", "A")
c = collect_coordinates(c, "X", "B")
d = collect_coordinates(d, "Y", "B")
e = collect_coordinates(e, "X", "C")
f = collect_coordinates(f, "Y", "C")'''

while True:
        try:
            a = float(input("Please specify coordinate X of vertice A: "))
            if a < 100 and a > -100:
                break
            print("Please enter the number between -100 and 100")
        except ValueError:
            print("Please enter the NUMBER!")

while True:
        try:
            b = float(input("Please specify coordinate Y of vertice A: "))
            if a < 100 and a > -100:
                break
            print("Please enter the number between -100 and 100")
        except ValueError:
            print("Please enter the NUMBER!")

while True:
        try:
            c = float(input("Please specify coordinate X of vertice B: "))
            if a < 100 and a > -100:
                break
            print("Please enter the number between -100 and 100")
        except ValueError:
            print("Please enter the NUMBER!")

while True:
        try:
            d = float(input("Please specify coordinate Y of vertice B: "))
            if a < 100 and a > -100:
                break
            print("Please enter the number between -100 and 100")
        except ValueError:
            print("Please enter the NUMBER!")

while True:
        try:
            e = float(input("Please specify coordinate X of vertice C: "))
            if a < 100 and a > -100:
                break
            print("Please enter the number between -100 and 100")
        except ValueError:
            print("Please enter the NUMBER!")

while True:
        try:
            f = float(input("Please specify coordinate Y of vertice C: "))
            if a < 100 and a > -100:
                break
            print("Please enter the number between -100 and 100")
        except ValueError:
            print("Please enter the NUMBER!")

# quick check
'''a = 0
b = 0
c = 2
d = 2
e = 4
f = 0'''

side_A = round(sqrt(fabs(a - c)**2 + fabs(b - d)**2), 2)
side_B = round(sqrt(fabs(c - e)**2 + fabs(d - f)**2), 2)
side_C = round(sqrt(fabs(e - a)**2 + fabs(f - b)**2), 2) 

if (side_A < side_B + side_C) or (side_B < side_A + side_C) or (side_C < side_B + side_A):
    # Heron's formula
    half_circumference = (side_A + side_B + side_C) / 2
    triangle_area = round(sqrt(half_circumference * (half_circumference-side_A) * (half_circumference-side_B) * (half_circumference-side_C)), 2)
    print(triangle_area)
else:
    print("Ooops! Your triangle is a line!")

