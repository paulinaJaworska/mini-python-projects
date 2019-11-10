''' You have 100 doors in a hallway in a row that are all initially closed. You make 100 passes by the doors.
The first time through, you visit every door and toggle the door (if the door is closed, you open it; if 
it is open, you close it). The second time you only visit every 2nd door (door #2, #4, #6, ...). 
The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.'''

''' Write a script that lists the number (the name) of the open doors after you visited 
all the 100 doors 100 times. This is an individual assignment but of course, you can get help from the others.'''

doors = [0]*100
for x in range (1,101):
    for y in range (x-1,100,x):
        if doors[y]== 0:
            doors[y] = 1
        elif doors[y]==1:
            doors[y] = 0
opendoors = []
for i, value in enumerate(doors):
    if value == 1:
            opendoors.append(i+1)
print('the following doors are open: ', opendoors)