#Reading and pulling the deets from the textFile.
my_file = open('day1/input.txt', 'r')
floors = my_file.read()

#Function for solution
def answer(floors):
    elevator = 0
    for floor in floors:
        if floor == ')':
            elevator -= 1
        elif floor == '(':
            elevator += 1
    return elevator

print("The Final Floor is:", answer(floors)) 


