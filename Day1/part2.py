#Reading and pulling the deets from the textFile.
my_file = open('day1/input.txt', 'r')
floors = my_file.read()

#Function for solution
def answer(floors):
    elevator = 0
    pos = 0
    for floor in floors:
           if elevator >= 0:
               if floor == ')':
                   elevator -= 1
                   pos +=1
               elif floor == '(':
                   elevator += 1
                   pos+=1
    return pos

print("The position is:", answer(floors)) 


