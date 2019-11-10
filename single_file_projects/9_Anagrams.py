'''Write the anagram recogniser that accepts a file 
name from the user provided as the command line 
argument of the script, reads each line of that 
file, and displays those pairs of words which are 
anagrams in separated lines. '''
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    with open(filename, "r") as f:
        for line in f:
            pairs = line.lower().split(", ")
            first_to_check = pairs[0]
            second_to_check = pairs[1]
            first_word = first_to_check.replace(" ", "").split().sort()
            second_word = second_to_check.replace(" ", "").split().sort()
            if first_word == second_word:
                print(first_to_check + " = " + second_to_check)
else:
    print("Please specify the file.")