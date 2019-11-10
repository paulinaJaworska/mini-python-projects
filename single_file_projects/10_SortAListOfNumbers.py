'''numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]

print(numbers)
for i in range(1, len(numbers)):                       
    for j in range(len(numbers) - 1):                    
        if numbers[j] > numbers[j+1]:
            temp, numbers[j+1] = numbers[j+1], numbers[j]
            numbers[j] = temp             
else:
    print(numbers)'''


#MODIFIED AND STRUCTURED CODE:
'''Sorting problem docstring
    a simple sorting algorithm that repeatedly steps 
    through the list to be sorted, compares each pair 
    of adjacent items and swaps them if they are in 
    the wrong order.'''


def main():
    list_length = ask_for_list_length()
    numbers = ask_for_numbers_list(list_length)
    print_current_numbers_list(numbers)

    for i in range(1, len(numbers)):

        for j in range(len(numbers) - 1):   
            j = shuffle_the_numbers(j, numbers)
    else:
        print_current_numbers_list(numbers)



def ask_for_list_length():
    while True:
        try:
            list_length = int(input("Please enter how long your list of number is: "))
            if list_length > 0:
                break
        except ValueError:
            print("Only positive intigers are allowed to enter.")
        finally:
            print("Only positive intigers are allowed to enter.")

    return list_length

def ask_for_numbers_list(length_of_numbers_list):
    numbers = []
    while True:
        try:
            numbers.append(float(input("Please add the number to the list: ")))
            if len(numbers) == length_of_numbers_list:
                break
        except ValueError:
            print("Only numbers (intiger or float)!")

    return numbers

def print_current_numbers_list(list):
    print(list)

def shuffle_the_numbers(inside_list_iterator, list):
    if list[inside_list_iterator] > list[inside_list_iterator+1]:
        temp, list[inside_list_iterator+1] = list[inside_list_iterator+1], list[inside_list_iterator]
        list[inside_list_iterator] = temp
    else:                   
        inside_list_iterator += 1

if __name__ == "__main__":
    main()
