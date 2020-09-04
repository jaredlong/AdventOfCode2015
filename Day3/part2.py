#Reading and pulling the data from the textFile.
my_file = open('day3/input.txt', 'r')
directions = my_file.read()

path = ['0-0']
x = 0
y = 0
for index, direction in enumerate(directions):
    if index % 2 == 0:
            if direction == '^':
                y+=1
            elif direction == 'v':
                y-=1
            elif direction == ">":
                x+=1
            elif direction == '<':
                x-=1
            path.append(str(x) + '-' + str(y))

#reseting X and Y back to zero
x=0
y=0

for index, direction in enumerate(directions):
    if index % 2 != 0:
            if direction == '^':
                y+=1
            elif direction == 'v':
                y-=1
            elif direction == ">":
                x+=1
            elif direction == '<':
                x-=1
            path.append(str(x) + '-' + str(y))

removed_dup_list = set(path)
print('Santa and Robo Santa delivered to ' + str(len(removed_dup_list)) + ' houses')
