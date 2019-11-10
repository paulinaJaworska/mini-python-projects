import sys

def save_my_idea():
    with open("IdeaBank.txt", "a") as f:   # This method closes the file after it gets to the end of block.
        # ask for input from the user
        idea = (input("Enter your new idea: "))
        f.write(idea + "\n")
    with open("IdeaBank.txt", "r") as f:
        content = f.readlines()
        print("\nYour Ideabank:\n")    
        for line in range(1, len(content)):
            print(("{0}. {1}".format(line, content[line])), end="") 


if len(sys.argv) ==1:
    save_my_idea()
elif sys.argv[1] == "--list":
     with open("IdeaBank.txt", "r") as f:
        content = f.readlines()
        print("\nYour Ideabank:\n")    
        for line in range(1, len(content)):
            print(("{0}. {1}".format(line, content[line])), end="")
            
elif sys.argv[1] == "--delete":
    id = sys.argv[2]
    with open("IdeaBank.txt", "r") as f:
        content = f.readlines()
        print("\nYour Ideabank:\n")    
        for line in range(1, len(content)):
            print(("{0}. {1}".format(line, content[line])), end="") 
    with open("IdeaBank.txt", "w") as f:   
        for line in content:
            print("\nYour Ideabank:\n")
            for line in range(1, len(content)): 
                if line[0] != str(id):                           
                    print(("{0}. {1}".format(line, content[line])), end="")
            
           

# The above way is more efficient than the way if you want to read the whole file. 
# Reads line by line the whole file.
# f_content = f.readline()
# print(f_content, end='')  # end - no space between the each line'''

# f = open.("IdeaBank.txt", "w")
# f.close()