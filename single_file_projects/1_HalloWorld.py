import sys

def welcome():
    if len(sys.argv) > 1:
        name = sys.argv[1:]
        print("Hallo {}!".format(name))
    else:
        print(("Hallo world!"))

welcome()