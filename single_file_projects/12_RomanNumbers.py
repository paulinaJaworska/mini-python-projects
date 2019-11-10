arab_to_roman_units = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "XI"}
arab_to_roman_tens = {1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXX", 9: "XC"}
arab_to_roman_hundred = {1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
arab_to_roman_thousand = {1: "M", 2: "MM", 3: "MMM"}

list_of_dict = [arab_to_roman_units, arab_to_roman_tens, arab_to_roman_hundred, arab_to_roman_thousand]
while True:
    arabic_numeral = input("Please, enter the number to convert it into a Roman numeral: ")
    try:
        if int(arabic_numeral) < 4000 and int(arabic_numeral) > 0:
            break
        print("Please enter the number between 0 and 4000.")
    except ValueError:
        print("Please enter the NUMBER!")

    
'''if len(arabic_numeral) == 4:   # skrócić 
    unit = arab_to_roman_units.get(int(arabic_numeral[-1]))
    ten = arab_to_roman_tens.get(int(arabic_numeral[-2]))
    hundred = arab_to_roman_hundred.get(int(arabic_numeral[-3]))
    thousand = arab_to_roman_thousand.get(int(arabic_numeral[-4]))
    print(str(thousand) + str(hundred) + str(ten) + str(unit))
elif len(arabic_numeral) == 3:
    unit = arab_to_roman_units.get(int(arabic_numeral[-1]))
    ten = arab_to_roman_tens.get(int(arabic_numeral[-2]))
    hundred = arab_to_roman_hundred.get(int(arabic_numeral[-3]))
    print(str(hundred) + str(ten) + str(unit))
elif len(arabic_numeral) == 2:
    unit = arab_to_roman_units.get(int(arabic_numeral[-1]))
    ten = arab_to_roman_tens.get(int(arabic_numeral[-2]))
    print(str(ten) + str(unit))
elif len(arabic_numeral) == 1:
    unit = arab_to_roman_units.get(int(arabic_numeral[-1]))
    print(str(unit))'''

number = []
for i in range(1, len(arabic_numeral)+ 1):
    for l in list_of_dict:
        number.append(l.get(int(arabic_numeral[-i])))
print(number)